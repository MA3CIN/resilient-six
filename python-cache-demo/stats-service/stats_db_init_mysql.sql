CREATE DATABASE IF NOT EXISTS statistics;
use statistics;
-- it seems that a copy of the devices DB might be the best option here

-- # this table will be cached in statistics microservice
-- CREATE TABLE Models (
-- 	id INT AUTO_INCREMENT PRIMARY KEY
-- 	, manufacturer INT NOT NULL
-- 	, category INT NOT NULL
--     , energy_consumption FLOAT NOT NULL
-- 	, name VARCHAR(200) NOT NULL
-- 	, comments VARCHAR(1000)
-- );


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

-- ALTER TABLE Models_Metrics
-- 	ADD CONSTRAINT modmetr_met_fk
-- 	FOREIGN KEY (metric_id) REFERENCES Metrics(id);

-- ALTER TABLE Models_Metrics
-- 	ADD CONSTRAINT modmetr_mod_fk
-- 	FOREIGN KEY (model_id) REFERENCES Models(id);

-- # this table will be cached in statistics microservice
-- CREATE TABLE Registered_Devices (
-- 	id INT AUTO_INCREMENT PRIMARY KEY
-- 	, model INT NOT NULL
-- 	, owner INT NOT NULL
-- 	, comments VARCHAR(1000)	
-- );

-- ALTER TABLE Registered_Devices
-- 	ADD CONSTRAINT regdev_mod_fk
-- 	FOREIGN KEY (model) REFERENCES Models(id);


CREATE TABLE Observed_Values (
    device_id INT NOT NULL
    , metric_id INT NOT NULL
    , timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    , value FLOAT NOT NULL
    , comments VARCHAR(1000)
    , PRIMARY KEY(device_id, metric_id, timestamp)
);

-- ALTER TABLE Observed_Values
--     ADD CONSTRAINT obsval_regdev_fk
--     FOREIGN KEY (device_id) REFERENCES Registered_Devices(id);

-- ALTER TABLE Observed_Values
--     ADD CONSTRAINT  obsval_metrics_fk
--     FOREIGN KEY (metric_id) REFERENCES Metrics(id);

INSERT INTO Metrics (name) VALUES ('temperature [C]');
INSERT INTO Metrics (name) VALUES ('temperature [K]');
INSERT INTO Metrics (name) VALUES ('temperature [F]');
INSERT INTO Metrics (name) VALUES ('temperature [mmHg]');
INSERT INTO Metrics (name) VALUES ('rainfall [mm]');
COMMIT;

-- for Prime Sensors
INSERT INTO Models_Metrics (metric_id, model_id) VALUES (1, 1);
INSERT INTO Models_Metrics (metric_id, model_id) VALUES (2, 1);
INSERT INTO Models_Metrics (metric_id, model_id) VALUES (3, 1);
INSERT INTO Models_Metrics (metric_id, model_id) VALUES (1, 2);
INSERT INTO Models_Metrics (metric_id, model_id) VALUES (2, 2);
INSERT INTO Models_Metrics (metric_id, model_id) VALUES (3, 2);
INSERT INTO Models_Metrics (metric_id, model_id) VALUES (1, 3);
INSERT INTO Models_Metrics (metric_id, model_id) VALUES (2, 3);
INSERT INTO Models_Metrics (metric_id, model_id) VALUES (3, 3);
INSERT INTO Models_Metrics (metric_id, model_id) VALUES (1, 4);
INSERT INTO Models_Metrics (metric_id, model_id) VALUES (2, 4);
INSERT INTO Models_Metrics (metric_id, model_id) VALUES (3, 4);
INSERT INTO Models_Metrics (metric_id, model_id) VALUES (5, 5);
INSERT INTO Models_Metrics (metric_id, model_id) VALUES (5, 6);
INSERT INTO Models_Metrics (metric_id, model_id) VALUES (5, 7);
INSERT INTO Models_Metrics (metric_id, model_id) VALUES (5, 8);

-- for iHome IoT
INSERT INTO Models_Metrics (metric_id, model_id) VALUES (1, 11);
INSERT INTO Models_Metrics (metric_id, model_id) VALUES (2, 11);
INSERT INTO Models_Metrics (metric_id, model_id) VALUES (3, 11);
INSERT INTO Models_Metrics (metric_id, model_id) VALUES (1, 12);
INSERT INTO Models_Metrics (metric_id, model_id) VALUES (2, 12);
INSERT INTO Models_Metrics (metric_id, model_id) VALUES (3, 12);
INSERT INTO Models_Metrics (metric_id, model_id) VALUES (1, 13);
INSERT INTO Models_Metrics (metric_id, model_id) VALUES (2, 13);
INSERT INTO Models_Metrics (metric_id, model_id) VALUES (3, 13);
INSERT INTO Models_Metrics (metric_id, model_id) VALUES (1, 14);
INSERT INTO Models_Metrics (metric_id, model_id) VALUES (2, 14);
INSERT INTO Models_Metrics (metric_id, model_id) VALUES (3, 14);
INSERT INTO Models_Metrics (metric_id, model_id) VALUES (5, 15);
INSERT INTO Models_Metrics (metric_id, model_id) VALUES (5, 16);
INSERT INTO Models_Metrics (metric_id, model_id) VALUES (5, 17);
INSERT INTO Models_Metrics (metric_id, model_id) VALUES (5, 18);
COMMIT;

INSERT INTO Observed_Values (device_id, metric_id, value) VALUES (1, 1, 15.5);
INSERT INTO Observed_Values (device_id, metric_id, value) VALUES (1, 3, 59.9);
INSERT INTO Observed_Values (device_id, metric_id, value) VALUES (2, 1, 12.4);
INSERT INTO Observed_Values (device_id, metric_id, value) VALUES (3, 1, 13.1);
INSERT INTO Observed_Values (device_id, metric_id, value, timestamp) VALUES (1, 1, 20.1, TIMESTAMP("2017-07-23",  "13:10:11"));
COMMIT;