import sqlite3
from sqlite3 import Error
import sys

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("[INFO] Connection Established: " + sqlite3.version)
    except Error as e:
        print(e)

    return conn

def close_connection(conn):
    conn.close

def select_query(conn, query):
    cur = conn.cursor()
    cur.execute(query)

    rows = cur.fetchall()

    for row in rows:
        print(row)

def main():
    if len(sys.argv) != 2:
        print("Please ensure you are selecting the appropriate query number when running the file.")
        sys.exit(1)
    
    query_number = int(sys.argv[1])

    db_path = "XYZGym.sqlite"

    queries = {
        1: """
            SELECT Member.name, Member.email, Member.age, MembershipPlan.planType
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
            WHERE classId = 4;
        """,
        4: """
            SELECT *
            FROM Equipment
            WHERE type = 'Strength';
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
            WHERE instructorId = 5;
        """,
        7: """
            SELECT 
                CASE 
                    WHEN Member.membershipEndDate >= DATE('now') THEN 'Active'
                    ELSE 'Expired'
                END AS membership_status,
                AVG(Member.age) AS average_age
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
            WHERE NOT EXISTS (
                SELECT *
                FROM Class
                WHERE classType = 'Weights' AND NOT EXISTS (
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
        select_query(conn, queries[query_number])
    except Exception as e:
        print("An error occurred: {e}")
    finally:
        close_connection(conn)
    
if __name__ == "__main__":
    main()