-- 1. Insert GymFacility Records


-- 2. Insert Instructor Records


-- 3. Insert Membership Plan Records


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
