import sqlite3
from sqlite3 import Error
import sys

def create_connection(db_file):
    """
    Create a database connection to the SQLite database specified by db_file.

    Parameters
    ----------
    db_file : str
        The path to the SQLite database file.

    Returns
    -------
    value : sqlite3.Connection
        Connection object or None if the connection fails.
    """

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("[INFO] Connection Established: " + sqlite3.sqlite_version)
    except Error as e:
        print(e)

    return conn

def close_connection(conn):
    """
    Close the database connection.

    Parameters
    ----------
    conn : sqlite3.Connection
        The connection object to close.
    """

    conn.close()

def select_query(conn, query, extra_param, query_number):
    """
    Execute a SELECT query on the database and print the results.
    Queries 3, 4, 6, and 9 require an extra parameter.
    For query 10, it formats the results into a specific table format.

    Parameters
    ----------
    conn : sqlite3.Connection
        The connection object to the database.
    query : str
        The SQL SELECT query to execute.
    extra_param : str or None
        An optional parameter for the SQL query.
    query_number : int
        The number identifying the specific query.
    """

    cur = conn.cursor()

    if "?" not in query:
        cur.execute(query)
    elif extra_param is None:
        print("This query requires an extra parameter.")
        sys.exit(1)
    elif query_number == 9:
        cur.execute(query, (extra_param, extra_param))
    else:
        cur.execute(query, (extra_param,))

    rows = cur.fetchall()
    if query_number == 10:
        rows = attendance_table(rows)

    # pull the title and headers from the dictionary for the query
    formatting = query_formatting(query_number)
    if formatting:
        #prints the formatted title and divider
        print(f"\n{formatting['title']}\n" + "-" * len(formatting['title']))
        #prints the results using the headers from the dictionary
        print_results(cur, rows, formatting['headers'])

def attendance_table(rows):
    """
    Format the results of the attendance query into a more readable format.
    It groups the results by member name and aggregates the number of attendances,
    classes attended, and class types.

    Parameters
    ----------
    rows : list of tuples
        The result set from the SQL query.

    Returns
    -------
    value : list of tuples
        The formatted result set.
    """

    # dictionary to hold attendance data for each member
    att_records = {}

    for row in rows:
        # add each member only once to the dictionary
        if att_records.get(row[0]) is None:
            att_records[row[0]] = AttendanceData()

        att_data = att_records[row[0]]
        att_data.attendances += 1
        # use sets to avoid duplicates
        att_data.classes.add(row[1])
        att_data.class_types.add(row[2])

    formatted_rows = []
    for name in att_records:
        att_data = att_records[name]
        formatted_rows.append(
            (
                name,
                att_data.attendances,
                ", ".join(att_data.classes),
                ", ".join(att_data.class_types)
            )
        )

    return formatted_rows

def query_formatting(query_number):
    """ Method that holds the dictionary for formatted method titles and headers. """
    formatting = {
        1: {
            "title": "All Gym Members",
            "headers": ["Member Name", "Email", "Age", "Plan Type"]
        },
        2: {
            "title": "Number of Classes Available at Each Gym",
            "headers": ["Gym Location", "Class Count"]
        },
        3: {
            "title": "Members Attending a Specific Class",
            "headers": ["Member Name"]
        },
        4: {
            "title": "Equipment by Type",
            "headers": ["Equipment ID", "Equipment Name", "Type", "Quantity", "Gym ID"]
        },
        5: {
            "title": "Members with Expired Memberships",
            "headers": ["Member ID", "Member Name", "Membership End Date"]
        },
        6: {
            "title": "Instructor Class Schedule",
            "headers": ["Instructor Name", "Phone", "Class Name", "Class Type", "Duration", "Class Capacity"]
        },
        7: {
            "title": "Active/Expired Member Average Age",
            "headers": ["Membership Status", "Average Age"]
        },
        8: {
            "title": "Top 3 Instructors by Class Count",
            "headers": ["Instructor ID", "Instructor Name", "Class Count"]
        },
        9: {
            "title": "Members Attending All Classes of a Specified Type",
            "headers": ["Member ID", "Name", "Email", "Phone", "Address", "Age", "Membership Start Date", "Membership End Date"]
        },
        10: {
            "title": "Recent Class Attendance",
            "headers": ["Member Name", "Total Classes Attended", "Classes Attended", "Class Types"]
        }
    }
    return formatting.get(query_number)

def print_results(cursor, rows, custom_headers=None):
    """ Method to format the result from each query. It uses a dictionary to produce formatted titles and headers for the results.
    """
    if not rows:
        print("[INFO] No results found.")
        return

    # extract header names from the query result
    db_headers = [desc[0] for desc in cursor.description]
    headers=custom_headers
        # change data to strings
    str_rows = [tuple(str(item) for item in row) for row in rows]
        # join the headers and find the length of the row
    all_rows = [headers] + str_rows
    col_widths = [max(len(row[i]) for row in all_rows) for i in range(len(headers))]
    # construct the header
    header_line = "  ".join(f"{headers[i]:<{col_widths[i]}}" for i in range(len(headers)))
    separator = "=" * len(header_line)
    print(header_line)
    print(separator)
    # for loop to print the data from the query
    for row in str_rows:
        row_line = "  ".join(f"{row[i]:<{col_widths[i]}}" for i in range(len(row)))
        print(row_line)

class AttendanceData:
    """
    The attendance data for each member, which is used to format the results of
    the attendance query.

    Attributes
    ----------
    attendances : int
        The number of times a member has attended a class.
    classes : set
        A set of classes attended by the member.
    class_types : set
        A set of class types attended by the member.
    """

    def __init__(self):
        """
        Initialize the AttendanceData object with default values.
        """

        self.attendances = 0
        self.classes = set()
        self.class_types = set()

def main():
    if len(sys.argv) < 2:
        print("Please ensure you are selecting the appropriate query number when running the file.")
        sys.exit(1)

    query_number = int(sys.argv[1])

    try:
        extra_param = sys.argv[2]
    except IndexError:
        extra_param = None

    db_path = "XYZGym.sqlite"

    queries = {
        1: """
            SELECT DISTINCT Member.name, Member.email, Member.age, MembershipPlan.planType
            FROM Member
            INNER JOIN Payment ON Member.memberId = Payment.memberId
            INNER JOIN MembershipPlan ON Payment.planId = MembershipPlan.planId;
        """,
        2: """
            SELECT GF.location, COUNT(C.classId) AS class_count
            FROM GymFacility GF
            LEFT JOIN Class C ON GF.gymId = C.gymId
            GROUP BY GF.gymId;
        """,
        3: """
            SELECT DISTINCT name
            FROM Member
            NATURAL JOIN Attends
            WHERE classId = ?;
        """,
        4: """
            SELECT *
            FROM Equipment
            WHERE LOWER(type) = LOWER(?);
        """,
        5: """
            SELECT memberId, name, membershipEndDate
            FROM Member
            WHERE membershipEndDate < DATE('now');
        """,
        6: """
            SELECT Instructor.name, phone, className, classType, duration, classCapacity
            FROM Instructor
            NATURAL JOIN Class
            WHERE instructorId = ?;
        """,
        7: """
            SELECT
                CASE
                    WHEN Member.membershipEndDate >= DATE('now') THEN 'Active'
                    ELSE 'Expired'
                END AS membership_status,
                CAST(AVG(Member.age) AS INT) AS average_age
            FROM Member
            GROUP BY membership_status;
        """,
        8: """
            SELECT I.instructorId, I.name, COUNT(C.classId) AS class_count
            FROM Instructor I
            JOIN Class C ON I.instructorId = C.instructorId
            GROUP BY I.instructorId
            ORDER BY class_count DESC
            LIMIT 3;
        """,
        9: """
            SELECT *
            FROM Member
            WHERE EXISTS (
                SELECT *
                FROM Class
                WHERE LOWER(classType) = LOWER(?)
            ) AND NOT EXISTS (
                SELECT *
                FROM Class
                WHERE LOWER(classType) = LOWER(?) AND NOT EXISTS (
                    SELECT *
                    FROM Attends
                    WHERE Attends.classId = Class.classId AND Attends.memberId = Member.memberId)
            );
        """,
        10: """
            SELECT Member.name, Class.className, Class.classType
            FROM Attends
            INNER JOIN Member ON Attends.memberId = Member.memberId
            INNER JOIN Class ON Attends.classId = Class.classId
            WHERE Attends.attendanceDate >= DATE('now','-1 month');
        """
    }

    if query_number not in queries:
        print("Invalid query number. Choose between 1 and 10.")
        sys.exit(1)

    conn = create_connection(db_path)
    try:
        select_query(conn, queries[query_number], extra_param, query_number)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        close_connection(conn)

if __name__ == "__main__":
    main()
