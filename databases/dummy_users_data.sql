use devices;

INSERT INTO Users (comments) VALUES ('someone registered with Google OAuth');
INSERT INTO Users (comments) VALUES ('someone registered with Google OAuth');
INSERT INTO Users (comments) VALUES ('someone registered with Google OAuth');
INSERT INTO Users (comments) VALUES ('someone registered with Google OAuth');
COMMIT;

INSERT INTO Registered_Devices (model, owner) VALUES (1, 1);
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

