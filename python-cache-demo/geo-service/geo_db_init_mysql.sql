CREATE DATABASE IF NOT EXISTS geolocation;
use geolocation;

-- CREATE TABLE Users(
-- 	id INT AUTO_INCREMENT PRIMARY KEY
-- 	, comments VARCHAR(1000)
-- );

-- this table will be cached in statistics microservice
-- CREATE TABLE Registered_Devices (
-- 	id INT AUTO_INCREMENT PRIMARY KEY
-- 	, model INT NOT NULL
-- 	, owner INT NOT NULL
-- 	, x_position FLOAT
-- 	, y_position FLOAT
-- 	, comments VARCHAR(1000)	
-- );
	
-- ALTER TABLE Registered_Devices
-- 	ADD CONSTRAINT regdev_user_fk
-- 	FOREIGN KEY (owner) REFERENCES Users(id);


CREATE TABLE Devices_Locations (
    device_id INT
    , timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- if we need to serve a location history
	, x_position FLOAT
	, y_position FLOAT
    , comments VARCHAR(1000)
    , PRIMARY KEY (device_id, timestamp)
);

-- ALTER TABLE Devices_Locations
--     ADD CONSTRAINT devloc_regdev_fk
--     FOREIGN KEY (device_id) REFERENCES Registered_Devices(id);


INSERT INTO Devices_Locations (device_id, x_position, y_position) VALUES (1, 2.5, 6.4);
INSERT INTO Devices_Locations (device_id, x_position, y_position) VALUES (2, 17.9, 11.3);
COMMIT;