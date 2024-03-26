CREATE DATABASE IF NOT EXISTS geolocation_microservice;
use geolocation_microservice;

CREATE TABLE Users(
	id INT AUTO_INCREMENT PRIMARY KEY
	, comments VARCHAR(1000)
);

CREATE TABLE Registered_Devices (
	id INT AUTO_INCREMENT PRIMARY KEY
-- 	, model INT NOT NULL -- need to think whether we need it or not
	, owner INT NOT NULL
	, x_position FLOAT
	, y_position FLOAT
	, comments VARCHAR(1000)	
);

-- need to think whether we need it or not
-- ALTER TABLE Registered_Devices
-- 	ADD CONSTRAINT regdev_mod_fk
-- 	FOREIGN KEY (model) REFERENCES Models(id);
	
ALTER TABLE Registered_Devices
	ADD CONSTRAINT regdev_user_fk
	FOREIGN KEY (owner) REFERENCES Users(id);