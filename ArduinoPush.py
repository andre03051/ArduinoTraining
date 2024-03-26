import serial
import mysql.connector
import urllib.parse
import time
from datetime import datetime

# Set up the serial connection
ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with your port number and '9600' with your baud rate

# Set up the MySQL connection
db = mysql.connector.connect(
  host="sql5.freesqldatabase.com",  # Replace with your host
  user="sql5692834",  # Replace with your username
  password="XGap5HZ8V9",  # Replace with your password
  database="sql5692834"  # Replace with your database
)

# Create a cursor object
cursor = db.cursor()

while True:
  # Add a delay to gather data
  time.sleep(1)
  
  # Read data from Arduino
  data = ser.readline().decode('utf-8').strip()
  
  # Get the current date and time
  now = datetime.now()
  
  # Parse the data
  params = urllib.parse.parse_qs(data)
  sensor_id = params['sensor_id'][0] 
  mean = params['mean'][0]
  median = params['median'][0]
  
  # Get the current date and time
  now = datetime.now()

  # Execute an SQL query
  sql = "INSERT INTO SensorReadings (Sensor_ID, MeanReading, MedianReading, Timestamp) VALUES (%s, %s, %s, %s)"
  val = (sensor_id, mean, median, now.strftime("%Y-%m-%d %H:%M:%S"))
  cursor.execute(sql, val)

  # Commit the transaction
  db.commit()