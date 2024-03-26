# ArduinoTraining
Repo for teaching myself how to gather sensor data with Arduino, posting the data, and retrieving it for analysis.

## First-Attempt
The first-attempt branch used a random number generated built into the arduino to generate simulated sensor data.  With the raw sensor measurement, the Arduino script would calculate the mean and the median measurement once every second.  The Python script (both the Jupyter notebook and Python script) read the serial output, parse the data, adds the timestamp, and commits it to a MySQL database.  

## sensor-output
The next steps of the project is to connect an actual sensor to Arduino to determine what the raw output is.  Once the raw output can be determnined, a calibration procedure can be drafted, executed, and the bias/scale factor can be added to the sensor table to allow for proper conversion from raw measurements to physical measurements to be used for analysis.

## Raspberry Pi
Once a sensor can be read from an Arduino, interpreted through Python, and recorded on a MySQL server the last step will be to connect this to a Raspberry Pi to allow for continuous monitoring without the need of a laptop.  

## Brooker Technology
The last step of this project is still not well understood, but I would like to integrate brooker technology to understand how the publish/subscribe technology works.  

# Summary
All of these steps should generate new ideas and projects that will allow me to develop my IIoT understanding along with allowing me to become a rudimentary integrator. 