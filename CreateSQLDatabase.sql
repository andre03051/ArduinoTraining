-- Active: 1710901428162@@sql5.freesqldatabase.com@3306@sql5692834
CREATE TABLE Sensors (
    Sensor_ID INT AUTO_INCREMENT PRIMARY KEY,
    Sensor_Name VARCHAR(255),
    Sensor_Type VARCHAR(255),
    Sensor_Units VARCHAR(255),
    Sensor_PartNum VARCHAR(255),
    Sensor_Supplier VARCHAR(255),
    Sensor_Location VARCHAR(255)
);

CREATE TABLE SensorReadings (
    Reading_ID INT AUTO_INCREMENT PRIMARY KEY,
    Sensor_ID INT,
    Reading FLOAT NOT NULL,
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (Sensor_ID) REFERENCES Sensors(Sensor_ID)
);