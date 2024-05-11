CREATE DATABASE IF NOT EXISTS statistics;
use statistics;
-- it seems that a copy of the devices DB might be the best option here

-- this table will be cached in statistics microservice
CREATE TABLE Models (
	id INT AUTO_INCREMENT PRIMARY KEY
	, manufacturer INT NOT NULL
	, category INT NOT NULL
    , energy_consumption FLOAT NOT NULL
	, name VARCHAR(200) NOT NULL
	, comments VARCHAR(1000)
);


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

-- this table will be cached in statistics microservice
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


CREATE TABLE Observed_Values (
    device_id INT NOT NULL
    , metric_id INT NOT NULL
    , timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    , value FLOAT NOT NULL
    , comments VARCHAR(1000)
    , PRIMARY KEY(device_id, metric_id, timestamp)
);

ALTER TABLE Observed_Values
    ADD CONSTRAINT obsval_regdev_fk
    FOREIGN KEY (device_id) REFERENCES Registered_Devices(id);

ALTER TABLE Observed_Values
    ADD CONSTRAINT  obsval_metrics_fk
    FOREIGN KEY (metric_id) REFERENCES Metrics(id);