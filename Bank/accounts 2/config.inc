<?php

$hostname = 'localhost';        // Your MySQL hostname. Usualy named as 'localhost', so you're NOT necessary to change this even this script has already online on the internet.
$dbname   = 'bank'; // Your database name.
$username = 'bankuser';             // Your database username.
$password = '';                 // Your database password. If your database has no password, leave it empty.

// Let's connect to host
$mysql_connection = mysqli_connect($hostname, $username, $password, $dbname);
?>
