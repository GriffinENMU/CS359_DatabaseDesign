-- 1. Insert GymFacility Records
INSERT INTO GymFacility (location,phone,manager)
VALUES
('Portales, NM','+1 575-562-1011','Mark Otto'),
('Las Cruces, NM','+1 575-646-0111','Jacob Thornton'),
('Albuquerque, NM','+1 505-277-0111','Larry Page'),
('Farmington, NM','+1 505-327-3420','Emma Thomas'),
('Roswell, NM','+1 575-622-1360','John Doe');

-- 2. Insert Instructor Records
INSERT INTO Instructor (name, specialty, phone, email)
VALUES
('Steve Rogers', 'Strength Training', '+1 555 554-001', 'steve@avengers.com'),
('Natasha Romanoff', 'HITT & Combat Training', '+1 555 554-0002', 'natasha@shield.com'),
('Tony Stark', 'Advanced Weightlifting', '+1 555 554-0003', 'tony@starkindustries.com'),
('Barry Allen', 'Speed & Endurance Training', '+1 555 554-0004', 'barry@ccpd.com'),
('Selina Kyle', 'Flexibility & Agility', '+1 555 554-0005', 'selina@gothamcity.com');

-- 3. Insert Membership Plan Records
INSERT INTO MembershipPlan (planType, cost)
VALUES
('Monthly', 8.99),
('Annual', 99.99),
('Monthly', 12.99),
('Annual', 80.99),
('Monthly', 10.99);

-- 4. Insert Member Records
INSERT INTO Member (name, email, phone, address, age, membershipStartDate, membershipEndDate)
VALUES 
('Bruce Wayne', 'bruce@wayneenterprises.com', '+1 555 555-0001', '1007 Mountain Dr, Gotham', 35, '2025-01-01', '2026-01-01'),
('Wally West', 'peter@centralcity.gov', '+1 555 555-0002', '502 Bradford Street, Central City, MS', 22, '2025-02-01', '2026-02-01'),
('Diana Prince', 'diana@themyscira.com', '+1 555 555-0003', 'Themyscira, Aegean Sea', 30, '2025-03-01', '2026-03-01'),
('Clark Kent', 'clark@dailyplanet.com', '+1 555 555-0004', '344 Clinton St, Metropolis', 33, '2025-04-01', '2026-04-01'),
('J’onn J’onzz', 'martian@watchtower.com', '+1 555-1955', 'Watchtower, Earth Orbit', 350, '2025-01-01', '2026-01-01');

-- 5. Insert Class Records
INSERT INTO Class (className, classType, duration, classCapacity, instructorId, gymId)
VALUES
('Zen Yoga', 'Yoga', 60, 15, 5, 1),
('High-Intensity Spin Class', 'HIIT', 45, 20, 2, 2),
('Zumba Dance Party', 'Zumba', 50, 25, 5, 1),
('Strength Training Basics', 'Weights', 75, 12, 1, 2),
('Weekend Bootcamp', 'Weights', 60, 18, 1, 2);

-- 6. Insert Payment Records
INSERT INTO Payment (memberId,planId,amountPaid,paymentDate)
VALUES
(1,2,99.99,'2025-01-13'),
(4,2,99.99,'2025-01-20'),
(3,3,12.99,'2025-01-20'),
(2,1,8.99,'2025-01-27'),
(3,3,12.99,'2025-02-20');

-- 7. Insert Attendance Records
INSERT INTO Attends (memberId,classId,attendanceDate)
VALUES
(1,4,'2025-01-13'),
(1,4,'2025-01-15'),
(1,4,'2025-01-17'),
(4,5,'2025-01-18'),
(1,5,'2025-01-18');

-- 8. Insert Equipment Records
INSERT INTO Equipment (name, type, quantity, gymId)
VALUES
('Speed Force Treadmill', 'Cardio', 10, 2),
('Bat Dumbbells', 'Strength', 15, 2),
('Amazonian Training Mats', 'Flexibility', 30, 1),
('Kryptonian Rowing Machine', 'Cardio', 5, 2),
('Mjolnir Kettlebells', 'Strength', 12, 2);