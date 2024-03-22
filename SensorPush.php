
<?php
/*  
In this script, replace your_server_name, your_username, your_password, your_db_name, -- DONE
your_table, and column_name 
 with your actual database details. The script gets data from the Arduino via a GET request and inserts it into the database.  
 You would then make HTTP requests from your Arduino to this PHP script’s URL to send data. 
 The PHP script would then insert the data into the MySQL database.
*/

$servername = "sql5.freesqldatabase.com";
$username = "sql5692834";
$password = "XGap5HZ8V9";
$dbname = "sql5692834";

// Create connection
$conn = new mysqli($db_host, $db_username, $db_password, $db_name);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Get data from POST request
$sensor_id = $_POST['sensor_id'];
$mean = $_POST['mean'];
$median = $_POST['median'];
$timestamp = $_POST['timestamp'];

// Insert data into database
$sql = "INSERT INTO SensorReadings (Sensor_ID, MeanReading, MedianReading, Timestamp)
VALUES ('$sensor_id', '$mean', '$median', '$timestamp')";

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>