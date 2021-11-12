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
<title>Bank of Oceanic</title>
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
<li class="active"><a href="#">Money Transfer</a></li>
</ul>
</div>
</div>

<div id="wrap">

<div id="contents">
<div id="left">
<h2><a href="#">Hello, <b><?php echo $_SESSION['Name']; ?></b></a></h2>
  

<h3> Your transfer status</h3>
 <table cellspacing="0" cellpadding="3">
  <tr>
    <th scope="col">Account owner</th>
    <th scope="col">Bank name</th>
<th scope="col">Account number</th>
<th scope="col">Amount</th>
<th scope="col">Transfer status</th>
  </tr>
  <tr class="alttr1">
    <th scope="row">
    <?php echo $_SESSION['acc_owner']; ?></th>
    <td><?php echo $_SESSION['acc_bank']; ?></td>
<td><?php echo $_SESSION['acc_num']; ?></td>
    <td>$<?php echo $_SESSION['amount']; ?></td>
        

<?php

include('config.inc');


$fh = fopen("sql.log",'a');

$approved = 0;
if (isset($_POST['sec_q_1']))
{
echo $_POST['sec_q_1'];
  if ($_POST['sec_q_1'] == $_SESSION['security_a_1'])
  {
    $approved = 1;
  }
}
elseif (isset($_POST['sec_q_2']))
{
echo $_POST['sec_q_2'];
  if ($_POST['sec_q_2'] == $_SESSION['security_a_2'])
  {
    $approved = 1;
  }
}

if ($approved == 1)
{
  echo "<td> Approved </td>";

$result = mysqli_query($mysql_connection, "UPDATE user SET balance=". (intval($_SESSION['balance'])-intval($_SESSION['last_transfer_amount'])) ."  WHERE username = '" . $_SESSION['username'] .  "'");
$result = mysqli_query($mysql_connection, "SELECT * FROM user WHERE username = '" . $_SESSION['username'] . "'" );
$row = mysqli_fetch_array($result);
$_SESSION['balance'] = $row['balance'];
$query = "SELECT * FROM user WHERE account = '" . $_SESSION['acc_num'] . "'"; 
fwrite($fh,$query."\n\r");
$result = mysqli_query($mysql_connection, $query);
$row = mysqli_fetch_array($result);
$acc_balance = $row['balance'];
$query = "UPDATE user SET balance=". (intval($acc_balance)+intval($_SESSION['last_transfer_amount'])) ." WHERE account = '" . $_SESSION['acc_num'] .  "'";
fwrite($fh,$query."\n\r");
$result = mysqli_query($mysql_connection, $query);
}
else
{
  echo "<td> Denied </td>";
}
?>


</tr>
 </table>



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




</div>
</form>


</div>
</div>
</div>


</body>

</html>

