<?php

// Inialize session
session_start();

// Check, if username session is NOT set then this page will jump to login page
if (!isset($_SESSION['username'])) {
        header('Location: index.php');
}

?>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Bank of Kamk</title>
<link href="style.css" rel="stylesheet" type="text/css" />
</head>

<body>
<div id="topbar">
<div id="TopSection">
<h1 id="sitename"><span><a href="#">Bank of Oceanic</a></h1>
<div class="clear"></div>
<ul id="topmenu">
<li><a href="logout.php">Logout</a></li>
<li><a href="securedpage.php">My Account</a></li>
<li><a href="transfer.php">Money Transfer</a></li>
</ul>
</div>
</div>

<div id="wrap">

<div id="homecontents"> 
<h2>Security confirmation</h2>
<h3>Hello, <b><?php echo $_SESSION['Name']; ?></b></h3>
<br>
<h3>In order to keep your account secured and safe, please answer the following security question:
</h3>


<form method="POST" action="dotransferverify.php">
<div class="contactform">
<p>

<input class="textfield" name=

<?php
$_SESSION['last_transfer_amount'] = $_POST['amount'];
$_SESSION['acc_bank'] = $_POST['acc_bank'];
$_SESSION['acc_owner'] = $_POST['acc_owner'];
$_SESSION['amount'] = $_POST['amount'];
$_SESSION['acc_num'] = $_POST['acc_num'];


$_SESSION['last_transfer'] =   $_POST['amount'] . " to ".    $_POST['acc_owner']. " in ". $_POST['acc_bank']. "  (account number ". $_POST['acc_num']. ")";
if (rand(1,1) == 1)
{
  echo '"sec_q_1"  type="text" /> <label for="sec_q_1">' ,    $_SESSION['security_q_1'] ;
}
else
{
echo '"sec_q_2"  type="text" /> <label for="sec_q_2">' ,    $_SESSION['security_q_2'] ;
}
?>


</label></p>
<p>
<label for="Submit"><span class="hide">Login</span></label>
<input name="Submit" type="submit" class="button" value="Submit" />

</div>
</form>


</div>

<div class="clear"></div>

</div>

</div>
</body>
</html>

