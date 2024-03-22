import serial
import requests

# Open the serial port
ser = serial.Serial('COM3', 9600)  # replace 'COM3' with your serial port

while True:
    # Read a line from the serial port
    line = ser.readline().decode('utf-8').strip()

    # Parse the line into a dictionary
    data = {}
    for item in line.split('&'):
        parts = item.split('=')
        if len(parts) == 2:
            data[parts[0]] = parts[1]

    # Send a POST request to the PHP server
    response = requests.post('http://dentarduino.atwebpages.com/SensorPush.php', data=data)

    # Print the server's response
    print(response.text)
