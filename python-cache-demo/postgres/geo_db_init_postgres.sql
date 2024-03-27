CREATE DATABASE geolocation_microservice;
set schema 'geolocation_microservice';

CREATE TABLE Users(
	id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY
	, comments VARCHAR(1000)
);

CREATE TABLE Registered_Devices (
	id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY
	, owner INT NOT NULL
	, x_position DOUBLE PRECISION
	, y_position DOUBLE PRECISION
	, comments VARCHAR(1000)	
);
	
ALTER TABLE Registered_Devices
	ADD CONSTRAINT regdev_user_fk
	FOREIGN KEY (owner) REFERENCES Users(id);