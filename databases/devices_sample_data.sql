use devices;

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
INSERT INTO Models (manufacturer, category, name) VALUES (1, 1, 'PS-T-Sensor-01');
INSERT INTO Models (manufacturer, category, name) VALUES (1, 1, 'PS-T-Sensor-02');
INSERT INTO Models (manufacturer, category, name) VALUES (1, 2, 'PS-T-Pred-A01');
INSERT INTO Models (manufacturer, category, name) VALUES (1, 2, 'PS-T-Pred-A02');
INSERT INTO Models (manufacturer, category, name) VALUES (1, 3, 'PS-Rain-Sensor-R01');
INSERT INTO Models (manufacturer, category, name) VALUES (1, 3, 'PS-Rain-Sensor-R01 Pro');
INSERT INTO Models (manufacturer, category, name) VALUES (1, 4, 'PS-Rain-Pred-RP01');
INSERT INTO Models (manufacturer, category, name) VALUES (1, 4, 'PS-Rain-Pred-RP01 Pro');
INSERT INTO Models (manufacturer, category, name) VALUES (1, 5, 'PS-M-Sensor-M01');
INSERT INTO Models (manufacturer, category, name) VALUES (1, 6, 'PS-Door-Bell-SDB01');

-- for iHome IoT
INSERT INTO Models (manufacturer, category, name) VALUES (2, 1, 'iTemperature 10');
INSERT INTO Models (manufacturer, category, name) VALUES (2, 1, 'iTemperature 20');
INSERT INTO Models (manufacturer, category, name) VALUES (2, 2, 'iTemperaturePreditor 10');
INSERT INTO Models (manufacturer, category, name) VALUES (2, 2, 'iTemperaturePreditor 10');
INSERT INTO Models (manufacturer, category, name) VALUES (2, 3, 'iRainfall 10 Fluid');
INSERT INTO Models (manufacturer, category, name) VALUES (2, 3, 'iRainfall 20 Fluid');
INSERT INTO Models (manufacturer, category, name) VALUES (2, 4, 'iRainfallPredictor 10 Pro');
INSERT INTO Models (manufacturer, category, name) VALUES (2, 4, 'iRainfallPredictor 20 Pro');

-- for DYI Systems
INSERT INTO Models (manufacturer, category, name) VALUES (3, 5, 'MS M01AB100');
INSERT INTO Models (manufacturer, category, name) VALUES (3, 6, 'SDB S01CD200');
COMMIT;

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
