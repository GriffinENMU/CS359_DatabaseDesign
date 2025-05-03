from util.prompt import prompt_enter, prompt_option
from util.validators import isPositiveInteger, recordExists

VALID_TYPES = ["Yoga", "Zumba", "HIIT", "Weights"]
CLASS_FIELDS = [
    "className",
    "classType",
    "duration",
    "classCapacity",
    "instructorId",
    "gymId",
]


def classes(conn):
    while True:
        print("\nCLASSES MENU")
        print("1) List classes and attendance")
        print("2) Add new class")
        print("3) Update class")
        print("4) Delete class (with member transfer option)")
        print("5) Find members by class")
        print("0) Go back")

        selection = prompt_option(5)

        match selection:
            case 1:
                listClassAttendance(conn)
            case 2:
                addClass(conn)
            case 3:
                updateClass(conn)
            case 4:
                deleteClass(conn)
            case 5:
                findMembersClassID(conn)
            case 0:
                break


def listClassAttendance(conn):
    curse = conn.cursor()
    curse.execute(
        """
                  SELECT Class.classId, Class.className, Class.classType, Class.duration, Class.classCapacity, COUNT(Attends.memberId) AS numberOfAttendees
                  FROM Class
                  LEFT JOIN Attends ON Class.classId = Attends.classId
                  GROUP BY Class.classId
                  """
    )
    rows = curse.fetchall()
    print("\nClasses and Attendance:")
    for row in rows:
        print(row)
    prompt_enter()


def addClass(conn):
    name = input("Class Name (Max 50 Characters): ")[:50]
    while not name.strip():
        print("Class name cant be empty")
        name = input("Class Name (Max 50 Characters): ")[:50]
    classType = input(f"Class type ({VALID_TYPES}): ")
    if classType not in VALID_TYPES:
        print("Invalid class type.")
        return

    duration = input("Duration (minutes): ")
    if not isPositiveInteger(duration):
        print("Invalid entry for duration")
        return

    capacity = input("Capacity: ")
    if not isPositiveInteger(capacity):
        print("Invalid entry for capacity.")
        return

    instructorId = input("Instructor ID: ")
    if not recordExists(conn, "Instructor", "instructorId", instructorId):
        print("Invalid instructor ID.")
        return

    gymId = input("Gym ID: ")
    if not recordExists(conn, "GymFacility", "gymId", gymId):
        print("Invalid Gym ID.")
        return

    curse = conn.cursor()
    curse.execute(
        """
                  INSERT INTO Class (className, classType, duration, classCapacity, instructorId, gymId)
                  VALUES (?, ?, ?, ?, ?, ?)
                  """,
        (name, classType, int(duration), int(capacity), int(instructorId), int(gymId)),
    )
    conn.commit()
    print("Class Added.")
    prompt_enter()


def updateClass(conn):
    classId = input("Class ID to update: ")
    if not recordExists(conn, "Class", "classId", classId):
        print("Class ID does not exist.")
        return

    updateField = input(f"Field to update: {CLASS_FIELDS}: ")
    if updateField not in CLASS_FIELDS:
        print("Invalid entry for field type.")
        return

    value = input("New Value: ")
    if updateField == "className" and not value.strip():
        print("Class Name can't be empty")
        return

    if updateField in ("duration", "classCapacity") and not isPositiveInteger(value):
        print("Value must be a positive number.")
        return

    if updateField == "classType" and value not in VALID_TYPES:
        print("Invalid class type.")
        return

    if updateField == "instructorId" and not recordExists(
        conn, "Instructor", "instructorId", value
    ):
        print("Invalid instructor ID")
        return

    if updateField == "gymId" and not recordExists(conn, "GymFacility", "gymId", value):
        print("Invalid Gym ID.")
        return

    curse = conn.cursor()
    curse.execute(
        f"UPDATE Class SET {updateField} = ? WHERE classId = ?", (value, classId)
    )
    conn.commit()
    print("Class updated.")
    prompt_enter(to="go back")


def deleteClass(conn):
    classId = input("Class ID to Delete: ")
    if not recordExists(conn, "Class", "classId", classId):
        print("Class not found.")
        return

    curse = conn.cursor()
    curse.execute("SELECT COUNT(*) FROM Attends WHERE classId = ?", (classId,))
    attendeeCount = curse.fetchone()[0]

    if attendeeCount > 0:
        print(f"Class has {attendeeCount} registered members.")
        move = input("Move them to another class? (y/n): ").lower()
        if move == "y":
            newClassId = input("New Class ID: ")
            if not recordExists(conn, "Class", "classId", newClassId):
                print("Class ID doesn't exist.")
                return
            curse.execute(
                "UPDATE Attends SET classId = ? WHERE classId = ?",
                (newClassId, classId),
            )
        else:
            print("Cancelled deletion.")

    curse.execute("DELETE FROM Class WHERE classId = ?", (classId,))
    conn.commit()
    print("Class has been deleted.")
    prompt_enter()


def findMembersClassID(conn):
    classId = input("Class ID: ")
    if not recordExists(conn, "Class", "classId", classId):
        print("Class not found.")
        return

    curse = conn.cursor()
    curse.execute(
        """
                   SELECT DISTINCT Member.memberId, Member.name, Member.email, Member.phone
                   From Member
                   JOIN Attends ON Member.memberId = Attends.memberId
                   Where Attends.classId = ?
                   """,
        (classId,),
    )
    rows = curse.fetchall()
    print("\nMembers in class: ")
    for row in rows:
        print(row)
    prompt_enter()
