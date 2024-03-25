CREATE DATABASE IF NOT EXISTS statistics_microservice;
use statistics_microservice;
-- it seems that a copy of the devices DB might be the best option here

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
	, name VARCHAR(200) NOT NULL
	, comments VARCHAR(1000)
);

ALTER TABLE Models
	ADD CONSTRAINT mod_man_fk
	FOREIGN KEY (manufacturer) REFERENCES Manufacturers(id);
	
ALTER TABLE Models
	ADD CONSTRAINT mod_cat_fk
	FOREIGN KEY (category) REFERENCES Devices_Categories(id);


CREATE TABLE Metrics (
	id INT AUTO_INCREMENT PRIMARY KEY
	, name VARCHAR(100) UNIQUE NOT NULL
	, comments VARCHAR(1000)
);

CREATE TABLE Models_Metrics (
	metric_id INT NOT NULL
	, model_id INT NOT NULL
	, value FLOAT
	, PRIMARY KEY(metric_id, model_id)
);

ALTER TABLE Models_Metrics
	ADD CONSTRAINT modmetr_met_fk
	FOREIGN KEY (metric_id) REFERENCES Metrics(id);

ALTER TABLE Models_Metrics
	ADD CONSTRAINT modmetr_mod_fk
	FOREIGN KEY (model_id) REFERENCES Models(id);


CREATE TABLE Users(
	id INT AUTO_INCREMENT PRIMARY KEY
	, comments VARCHAR(1000)
);

CREATE TABLE Registered_Devices (
	id INT AUTO_INCREMENT PRIMARY KEY
	, model INT NOT NULL
	, owner INT NOT NULL
	, x_position FLOAT	-- simplified version of longitude
	, y_position FLOAT	-- simplified version of latitude
	, comments VARCHAR(1000)	
);

ALTER TABLE Registered_Devices
	ADD CONSTRAINT regdev_mod_fk
	FOREIGN KEY (model) REFERENCES Models(id);
	
ALTER TABLE Registered_Devices
	ADD CONSTRAINT regdev_user_fk
	FOREIGN KEY (owner) REFERENCES Users(id);