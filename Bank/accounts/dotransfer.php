<?php

// Inialize session
session_start();

// Check, if username session is NOT set then this page will jump to login page
if (!isset($_SESSION['username'])) {
        header('Location: index.php');
}

?>
<html>

<head>
  <title>Welcome to Bank Of Antartica</title>

</head>

<body>


<h3>Transfer Money</h3>

<p>Hello <b><?php echo $_SESSION['Name']; ?></b><br>
<br>In order to transfer $<?php echo $_POST['amount']; ?> to   <?php echo $_POST['acc_owner']; ?> in <?php echo $_POST['acc_bank']; ?>  (account number <?php echo $_POST['acc_num']; ?>) 
you have to answer the following security question:
<br><br>

<table border="0">
<form method="POST" action="dotransferverify.php">
<tr><td>


<?php
$_SESSION['last_transfer_amount'] = $_POST['amount'];
$_SESSION['last_transfer'] =   $_POST['amount'] . " to ".    $_POST['acc_owner']. " in ". $_POST['acc_bank']. "  (account number ". $_POST['acc_num']. ")";
if (rand(1,2) == 1)
{
  echo $_SESSION['security_q_1'] , '</td><td>:</td><td><input type="text" name="sec_q_1" size="30"></td></tr>';
}
else
{
echo $_SESSION['security_q_2'] , '</td><td>:</td><td><input type="text" name="sec_q_2" size="30"></td></tr>';
}
?>


<tr><td>&nbsp;</td><td>&nbsp;</td><td><input type="submit" value="Make Transfer"></td></tr>
</form>
</table>




<p><a href="logout.php">Logout</a></p>

</body>

</html>
