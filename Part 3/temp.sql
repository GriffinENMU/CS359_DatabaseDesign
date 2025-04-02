-- Using this as the baseline SQL queries to match the requirements in Part 3.

-- 1.) Tested to ensure it returns all members.
SELECT Member.name, Member.email, Member.age, MembershipPlan.planType
FROM Member
INNER JOIN Payment ON Member.memberId = Payment.memberId
INNER JOIN MembershipPlan ON Payment.planId = MembershipPlan.planId;
-- 2.) Return the number of classes at each facility.
SELECT GF.location, COUNT(C.classId) AS class_count
    FROM GymFacility GF
    LEFT JOIN Class C ON GF.gymId = C.gymId
    GROUP BY GF.gymId;

-- 3.) Returns unique names that have at least one `Attends` for the given classId
SELECT DISTINCT name
FROM Member
	NATURAL JOIN Attends
WHERE classId = 4;

-- 4.) Confirmed it returns all details for the Equipment, will need to modify to accept Type information.
SELECT *
FROM Equipment
WHERE type = 'Strength';

-- 5.) Returns members with expired memberships.
SELECT memberId, name, membershipEndDate
    FROM Member
    WHERE membershipEndDate < DATE('now');


-- 6.) Returns the info exactly as requested
SELECT Instructor.name, phone, className, classType, duration, classCapacity
FROM Instructor
	NATURAL JOIN Class
WHERE instructorId = 5;

-- 7.) Creates a loop where it checks their end date and assigns it as either Active or Expired, then averages and displays both (currently only have Active memberships)
SELECT 
    CASE 
        WHEN Member.membershipEndDate >= DATE('now') THEN 'Active'
        ELSE 'Expired'
    END AS membership_status,
    AVG(Member.age) AS average_age
FROM Member
GROUP BY membership_status;

-- 8.) Returns the top three instructors who teach the most classes and the count of classes 

    SELECT I.instructorId, I.name, COUNT(C.classId) AS class_count
    FROM Instructor I
    JOIN Class C ON I.instructorId = C.instructorId
    GROUP BY I.instructorId
    ORDER BY class_count DESC
    LIMIT 3;
-- 9.) Tested, it works (please ask me if you have any questions about how this works)
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

-- 10.) Tested and it returned 0 results, increased end item from '-1 month' to '-2 month' and confirmed received all Attends data that was relevant.
SELECT Member.name, Class.className, Class.classType
FROM Attends
INNER JOIN Member ON Attends.memberId = Member.memberId
INNER JOIN Class ON Attends.classId = Class.classId
WHERE Attends.attendanceDate >= DATE('now','-1 month');
