<?php

// Inialize session
session_start();

// Check, if user is already login, then jump to secured page
if (isset($_SESSION['username'])) {
        header('Location: securedpage.php');
}

?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Bank of Oceanic</title>
<link href="style.css" rel="stylesheet" type="text/css" />
</head>

<body>
<div id="topbar">
<div id="TopSection">
<h1 id="sitename"><span><a href="#">Bank of Oceanic</a></h1>
<div class="clear"></div>
<ul id="topmenu">
<li class="active"><a href="index.php">Login</a></li>
<li><a href="securedpage.php">My Account</a></li>
<li><a href="transfer.php">Money Transfer</a></li>
</ul>
</div>
</div>

<div id="wrap">
<div id="header">
</div>

<div id="homecontents"> 
<h2>Please login to your bank account</h2>
<form method="POST" action="loginproc.php">
<div class="contactform">
<p>
<input class="textfield" name="username" type="text" />
<label for="username">Username</label></p>
<p>
<input class="textfield" name="password" type="password" />
<label for="password">Password</label></p>
<p>
<label for="Submit"><span class="hide">Login</span></label>
<input name="Submit" type="submit" class="button" value="Login" />

</div>
</form>


</div>

<div class="clear"></div>

</div>

</div>
</body>
</html>
