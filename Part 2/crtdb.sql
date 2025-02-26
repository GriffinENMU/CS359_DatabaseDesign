CREATE TABLE GymFacility (
	gymId INTEGER PRIMARY KEY AUTOINCREMENT,
	location VARCHAR(100),
	phone VARCHAR(50),
	manager VARCHAR(50)
);

CREATE TABLE Payment (
	paymentId INTEGER PRIMARY KEY AUTOINCREMENT,
	memberId INTEGER,
	planId INTEGER,
	amountPaid REAL NOT NULL,
	paymentDate DATE NOT NULL,
	
	FOREIGN KEY (memberId) REFERENCES Member,
	FOREIGN KEY (planId) REFERENCES MembershipPlan
);

CREATE TABLE Attends (
	memberId INTEGER NOT NULL,
	classId INTEGER NOT NULL,
	attendanceDate DATE NOT NULL,
	
	PRIMARY KEY (memberId, classId, attendanceDate),
	FOREIGN KEY (memberId) REFERENCES Member,
	FOREIGN KEY (classId) REFERENCES Class
);

CREATE TABLE Member(
	memberId INTEGER PRIMARY KEY AUTOINCREMENT,
	name VARCHAR(50) NOT NULL,
	email VARCHAR(50) NOT NULL UNIQUE,
	phone VARCHAR(15),
	address VARCHAR(100),
	age INTEGER NOT NULL CHECK(age>=15),
	membershipStartDate DATE NOT NULL,
	membershipEndDate DATE NOT NULL CHECK(membershipEndDate>=membershipStartDate)

);

CREATE TABLE Class(
	classId INTEGER PRIMARY KEY AUTOINCREMENT,
	className VARCHAR(50) NOT NULL,
	classType VARCHAR(20) NOT NULL CHECK(classType IN ('Yoga','Zumba','HIIT','Weights')),
	duration INTEGER NOT NULL,
	classCapacity INTEGER NOT NULL,
	instructorId INTEGER,
	gymId INTEGER,
	
	FOREIGN KEY (instructorId) REFERENCES Instructor(instructorId),
	FOREIGN KEY (gymId) REFERENCES GymFacility(gymId)
);

CREATE TABLE Instructor (
	instructorId INTEGER PRIMARY KEY AUTOINCREMENT,
	name VARCHAR(50) NOT NULL,
	specialty VARCHAR(50) NOT NULL,
	phone VARCHAR(15),
	email VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE Equipment (
	equipmentId INTEGER PRIMARY KEY AUTOINCREMENT,
	name VARCHAR(50) NOT NULL,
	type VARCHAR(30) NOT NULL CHECK(type IN ('Cardio', 'Strength', 'Flexibility', 'Recovery')),
	quantity INTEGER(30) NOT NULL CHECK(quantity>=0),
	gymId INTEGER,
	
	FOREIGN KEY (gymId) REFERENCES GymFacility(gymId)
);

CREATE TABLE MembershipPlan (
	planId INTEGER PRIMARY KEY AUTOINCREMENT,
	planType VARCHAR(20) NOT NULL CHECK(planType IN ('Monthly', 'Annual')),
	cost NUMERIC(10,2) NOT NULL CHECK(cost>=0 AND cost = ROUND(cost, 2))
);