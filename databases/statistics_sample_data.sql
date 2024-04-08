use statistics;

INSERT INTO Metrics (name) VALUES ('temperature [C]');
INSERT INTO Metrics (name) VALUES ('temperature [K]');
INSERT INTO Metrics (name) VALUES ('temperature [F]');
INSERT INTO Metrics (name) VALUES ('temperature [mmHg]');
INSERT INTO Metrics (name) VALUES ('rainfall [mm]');
COMMIT;

-- for Prime Sensors
# INSERT INTO Models_Metrics (metric_id, model_id) VALUES (1, 1);
# INSERT INTO Models_Metrics (metric_id, model_id) VALUES (2, 1);
# INSERT INTO Models_Metrics (metric_id, model_id) VALUES (3, 1);
# INSERT INTO Models_Metrics (metric_id, model_id) VALUES (1, 2);
# INSERT INTO Models_Metrics (metric_id, model_id) VALUES (2, 2);
# INSERT INTO Models_Metrics (metric_id, model_id) VALUES (3, 2);
# INSERT INTO Models_Metrics (metric_id, model_id) VALUES (1, 3);
# INSERT INTO Models_Metrics (metric_id, model_id) VALUES (2, 3);
# INSERT INTO Models_Metrics (metric_id, model_id) VALUES (3, 3);
# INSERT INTO Models_Metrics (metric_id, model_id) VALUES (1, 4);
# INSERT INTO Models_Metrics (metric_id, model_id) VALUES (2, 4);
# INSERT INTO Models_Metrics (metric_id, model_id) VALUES (3, 4);
# INSERT INTO Models_Metrics (metric_id, model_id) VALUES (5, 5);
# INSERT INTO Models_Metrics (metric_id, model_id) VALUES (5, 6);
# INSERT INTO Models_Metrics (metric_id, model_id) VALUES (5, 7);
# INSERT INTO Models_Metrics (metric_id, model_id) VALUES (5, 8);

-- for iHome IoT
# INSERT INTO Models_Metrics (metric_id, model_id) VALUES (1, 11);
# INSERT INTO Models_Metrics (metric_id, model_id) VALUES (2, 11);
# INSERT INTO Models_Metrics (metric_id, model_id) VALUES (3, 11);
# INSERT INTO Models_Metrics (metric_id, model_id) VALUES (1, 12);
# INSERT INTO Models_Metrics (metric_id, model_id) VALUES (2, 12);
# INSERT INTO Models_Metrics (metric_id, model_id) VALUES (3, 12);
# INSERT INTO Models_Metrics (metric_id, model_id) VALUES (1, 13);
# INSERT INTO Models_Metrics (metric_id, model_id) VALUES (2, 13);
# INSERT INTO Models_Metrics (metric_id, model_id) VALUES (3, 13);
# INSERT INTO Models_Metrics (metric_id, model_id) VALUES (1, 14);
# INSERT INTO Models_Metrics (metric_id, model_id) VALUES (2, 14);
# INSERT INTO Models_Metrics (metric_id, model_id) VALUES (3, 14);
# INSERT INTO Models_Metrics (metric_id, model_id) VALUES (5, 15);
# INSERT INTO Models_Metrics (metric_id, model_id) VALUES (5, 16);
# INSERT INTO Models_Metrics (metric_id, model_id) VALUES (5, 17);
# INSERT INTO Models_Metrics (metric_id, model_id) VALUES (5, 18);
COMMIT;