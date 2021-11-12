<?php

// Inialize session
session_start();

// Include database connection settings
include('config.inc');
if (!$mysql_connection) {
    echo "Error: Unable to connect to MySQL." . PHP_EOL;
    echo "Debugging errno: " . mysqli_connect_errno() . PHP_EOL;
    echo "Debugging error: " . mysqli_connect_error() . PHP_EOL;
    exit;
}
// Retrieve username and password from database according to user's input
$login = mysqli_query($mysql_connection, "SELECT * FROM user WHERE (username = '" . $_POST['username'] . "') and (password = '" . md5($_POST['password']) . "')");
// Check username and password match
if (mysqli_num_rows($login) == 1) {
	$row = mysqli_fetch_array($login);
        // Set username session variable
        $_SESSION['username'] = $_POST['username'];
	$_SESSION['Name'] = $row['Name'];
	$_SESSION['account'] = $row['account'];
	$_SESSION['balance'] = $row['balance'];
	$_SESSION['security_q_1'] = $row['security_q_1'];
	$_SESSION['security_a_1'] = $row['security_a_1'];
	$_SESSION['security_q_2'] = $row['security_q_2'];
	$_SESSION['security_a_2'] = $row['security_a_2'];
        // Jump to secured page
        header('Location: securedpage.php');
}
else {
        // Jump to login page
        header('Location: index.php');
}

?>
