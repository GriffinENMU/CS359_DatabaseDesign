-- 1. Insert GymFacility Records


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
('Justice League Tier', 99.99),
('Avengers Assemble', 79.99),
('Gotham Night Pass', 49.99),
('Speedster Plan', 29.99),
('Mutant Academy Special', 24.99);

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
-- NULL placeholder vales need to be update when other tables are complete
('Zen Yoga', 'Yoga', 60, 15, NULL, NULL),
('High-Intensity Spin Class', 'HIIT', 45, 20, NULL, NULL),
('Zumba Dance Party', 'Zumba', 50, 25, NULL, NULL),
('Strength Training Basics', 'Weights', 75, 12, NULL, NULL),
('Weekend Bootcamp', 'Weights', 60, 18, NULL, NULL);

-- 6. Insert Payment Records


-- 7. Insert Attendance Records

-- 8. Insert Equipment Records
INSERT INTO Equipment (name, type, quantity, gymId)
VALUES
-- NULL Placeholders pending full implementation
('Speed Force Treadmill', 'Cardio', 10, NULL),
('Bat Dumbbells', 'Strength', 15, NULL),
('Amazonian Training Mats', 'Flexibility', 30, NULL),
('Kryptonian Rowing Machine', 'Cardio', 5, NULL),
('Mjolnir Kettlebells', 'Strength', 12, NULL);