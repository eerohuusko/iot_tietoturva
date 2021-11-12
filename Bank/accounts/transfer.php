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
<h1 id="sitename"><span><a href="#">Bank of Kamk</a></h1>
<div class="clear"></div>
<ul id="topmenu">
<li><a href="logout.php">Logout</a></li>
<li><a href="#">My Account</a></li>
<li class="active"><a href="#">Money Transfer</a></li>
</ul>
</div>
</div>

<div id="wrap">

<div id="contents">
<div id="left">
<h2><a href="#">Hello, <b><?php echo $_SESSION['Name']; ?></b></a></h2>
  <h3> Your current balance</h3>
 <table cellspacing="0" cellpadding="3">
  <tr>
    <th scope="col">Account number</th>
    <th scope="col">Balance</th>
  </tr>
  <tr class="alttr1">
    <th scope="row"><?php echo $_SESSION['account']; ?></th>
    <td>$<?php echo $_SESSION['balance']; ?></td>
    </tr>
 </table>


<h3>Where do you want to transfer money?</h3>
<form method="POST" action="securitycheck.php">
<div class="contactform">
<p>
<input class="textfield" name="acc_owner" type="text" />
<label for="acc_owner">Account owner</label></p>
<p>
<input class="textfield" name="acc_bank" type="text" />
<label for="acc_bank">Bank name</label></p>
<p>
<input class="textfield" name="acc_num" type="text" />
<label for="acc_num">Account number</label></p>
<p>
<input class="textfield" name="amount" type="text" />
<label for="amount">Amount to transfer</label></p>
<p>

<label for="Submit"><span class="hide">Transfer</span></label>
<input name="Submit" type="submit" class="button" value="Transfer" />

</div>
</form>


</div>
</div>
</div>


</body>

</html>

