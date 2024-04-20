CREATE DATABASE IF NOT EXISTS devices;
use devices;

CREATE TABLE Manufacturers (
    id INT AUTO_INCREMENT PRIMARY KEY
    , name VARCHAR(100) NOT NULL
    , comments VARCHAR(1000)
);

CREATE TABLE Devices_Categories (
	id INT AUTO_INCREMENT PRIMARY KEY
	, name VARCHAR(100) UNIQUE NOT NULL
	, comments VARCHAR(1000)
);

CREATE TABLE Models (
	id INT AUTO_INCREMENT PRIMARY KEY
	, manufacturer INT NOT NULL
	, category INT NOT NULL
    , energy_consumption FLOAT NOT NULL
	, name VARCHAR(200) NOT NULL
	, comments VARCHAR(1000)
);

ALTER TABLE Models
	ADD CONSTRAINT mod_man_fk
	FOREIGN KEY (manufacturer) REFERENCES Manufacturers(id);
	
ALTER TABLE Models
	ADD CONSTRAINT mod_cat_fk
	FOREIGN KEY (category) REFERENCES Devices_Categories(id);


CREATE TABLE Users(
	id INT AUTO_INCREMENT PRIMARY KEY
	, comments VARCHAR(1000)
);

CREATE TABLE Registered_Devices (
	id INT AUTO_INCREMENT PRIMARY KEY
	, model INT NOT NULL
	, owner INT NOT NULL
	, name VARCHAR(200)
	, comments VARCHAR(1000)	
);

ALTER TABLE Registered_Devices
	ADD CONSTRAINT regdev_mod_fk
	FOREIGN KEY (model) REFERENCES Models(id);
	
ALTER TABLE Registered_Devices
	ADD CONSTRAINT regdev_user_fk
	FOREIGN KEY (owner) REFERENCES Users(id);

INSERT INTO Manufacturers (name) VALUES ('Prime Sensors');
INSERT INTO Manufacturers (name) VALUES ('iHome IoT');
INSERT INTO Manufacturers (name) VALUES ('DYI Systems');
INSERT INTO Manufacturers (name) VALUES ('Prime Sensors');
INSERT INTO Manufacturers (name) VALUES ('SmartSensors');
COMMIT;

INSERT INTO Devices_Categories (name) VALUES ('temperature sensor');
INSERT INTO Devices_Categories (name) VALUES ('temperature predictor');
INSERT INTO Devices_Categories (name) VALUES ('rainfall sensor');
INSERT INTO Devices_Categories (name) VALUES ('rainfall predictor');
INSERT INTO Devices_Categories (name) VALUES ('movement sensor');
INSERT INTO Devices_Categories (name) VALUES ('smart door bell');
COMMIT;

-- for Prime Sensors
INSERT INTO Models (manufacturer, category, name, energy_consumption) VALUES (1, 1, 'PS-T-Sensor-01', 0.5);
INSERT INTO Models (manufacturer, category, name, energy_consumption) VALUES (1, 1, 'PS-T-Sensor-02', 0.5);
INSERT INTO Models (manufacturer, category, name, energy_consumption) VALUES (1, 2, 'PS-T-Pred-A01', 1);
INSERT INTO Models (manufacturer, category, name, energy_consumption) VALUES (1, 2, 'PS-T-Pred-A02', 1);
INSERT INTO Models (manufacturer, category, name, energy_consumption) VALUES (1, 3, 'PS-Rain-Sensor-R01', 2);
INSERT INTO Models (manufacturer, category, name, energy_consumption) VALUES (1, 3, 'PS-Rain-Sensor-R01 Pro', 2);
INSERT INTO Models (manufacturer, category, name, energy_consumption) VALUES (1, 4, 'PS-Rain-Pred-RP01', 1.5);
INSERT INTO Models (manufacturer, category, name, energy_consumption) VALUES (1, 4, 'PS-Rain-Pred-RP01 Pro', 1.5);
INSERT INTO Models (manufacturer, category, name, energy_consumption) VALUES (1, 5, 'PS-M-Sensor-M01', 1);
INSERT INTO Models (manufacturer, category, name, energy_consumption) VALUES (1, 6, 'PS-Door-Bell-SDB01', 1);

-- for iHome IoT
INSERT INTO Models (manufacturer, category, name, energy_consumption) VALUES (2, 1, 'iTemperature 10', 0.75);
INSERT INTO Models (manufacturer, category, name, energy_consumption) VALUES (2, 1, 'iTemperature 20', 1.75);
INSERT INTO Models (manufacturer, category, name, energy_consumption) VALUES (2, 2, 'iTemperaturePreditor 10', 2);
INSERT INTO Models (manufacturer, category, name, energy_consumption) VALUES (2, 2, 'iTemperaturePreditor 10', 2.25);
INSERT INTO Models (manufacturer, category, name, energy_consumption) VALUES (2, 3, 'iRainfall 10 Fluid', 1.5);
INSERT INTO Models (manufacturer, category, name, energy_consumption) VALUES (2, 3, 'iRainfall 20 Fluid', 1);
INSERT INTO Models (manufacturer, category, name, energy_consumption) VALUES (2, 4, 'iRainfallPredictor 10 Pro', 5);
INSERT INTO Models (manufacturer, category, name, energy_consumption) VALUES (2, 4, 'iRainfallPredictor 20 Pro', 5);

-- for DYI Systems
INSERT INTO Models (manufacturer, category, name, energy_consumption) VALUES (3, 5, 'MS M01AB100', 3);
INSERT INTO Models (manufacturer, category, name, energy_consumption) VALUES (3, 6, 'SDB S01CD200', 3);
COMMIT;

use devices;

INSERT INTO Users (comments) VALUES ('someone registered with Google OAuth');
INSERT INTO Users (comments) VALUES ('someone registered with Google OAuth');
INSERT INTO Users (comments) VALUES ('someone registered with Google OAuth');
INSERT INTO Users (comments) VALUES ('someone registered with Google OAuth');
COMMIT;

INSERT INTO Registered_Devices (model, owner, name) VALUES (1, 1, 'Strawberry');
INSERT INTO Registered_Devices (model, owner) VALUES (2, 1);
INSERT INTO Registered_Devices (model, owner) VALUES (3, 1);
INSERT INTO Registered_Devices (model, owner) VALUES (4, 1);

INSERT INTO Registered_Devices (model, owner) VALUES (5, 2);
INSERT INTO Registered_Devices (model, owner) VALUES (6, 2);
INSERT INTO Registered_Devices (model, owner) VALUES (7, 2);
INSERT INTO Registered_Devices (model, owner) VALUES (8, 2);

INSERT INTO Registered_Devices (model, owner) VALUES (1, 3);
INSERT INTO Registered_Devices (model, owner) VALUES (3, 3);

INSERT INTO Registered_Devices (model, owner) VALUES (6, 4);
INSERT INTO Registered_Devices (model, owner) VALUES (8, 4);
COMMIT;

