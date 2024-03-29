use devices;

INSERT INTO Users (comments) VALUES ('someone registered with Google OAuth');
INSERT INTO Users (comments) VALUES ('someone registered with Google OAuth');
INSERT INTO Users (comments) VALUES ('someone registered with Google OAuth');
INSERT INTO Users (comments) VALUES ('someone registered with Google OAuth');
COMMIT;

INSERT INTO Registered_Devices (model, owner, x_position, y_position) VALUES (1, 1, 10, 10);
INSERT INTO Registered_Devices (model, owner, x_position, y_position) VALUES (2, 1, -10, -7);
INSERT INTO Registered_Devices (model, owner, x_position, y_position) VALUES (3, 1, 10, 10);
INSERT INTO Registered_Devices (model, owner, x_position, y_position) VALUES (4, 1, -10, -15);

INSERT INTO Registered_Devices (model, owner, x_position, y_position) VALUES (5, 2, 5.5, 10.5);
INSERT INTO Registered_Devices (model, owner, x_position, y_position) VALUES (6, 2, -10.1, -7.2);
INSERT INTO Registered_Devices (model, owner, x_position, y_position) VALUES (7, 2, 10, 10);
INSERT INTO Registered_Devices (model, owner, x_position, y_position) VALUES (8, 2, -10, -15);

INSERT INTO Registered_Devices (model, owner, x_position, y_position) VALUES (1, 3, 10, 10);
INSERT INTO Registered_Devices (model, owner, x_position, y_position) VALUES (3, 3, 10, 10);

INSERT INTO Registered_Devices (model, owner, x_position, y_position) VALUES (6, 4, -10.1, -7.2);
INSERT INTO Registered_Devices (model, owner, x_position, y_position) VALUES (8, 4, -10, -15);
COMMIT;

