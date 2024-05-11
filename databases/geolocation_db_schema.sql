CREATE DATABASE IF NOT EXISTS geolocation;
use geolocation;

CREATE TABLE Devices_Locations (
    device_id INT
    , timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP  # if we need to serve a location history
	, x_position FLOAT
	, y_position FLOAT
    , comments VARCHAR(1000)
    , PRIMARY KEY (device_id, timestamp)
);
