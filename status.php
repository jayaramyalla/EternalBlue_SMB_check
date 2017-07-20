<html>
<body>
 
 
<?php
$con = mysql_connect("localhost","root","");
if (!$con)
  {
  die('Could not connect: ' . mysql_error());
  }
 
mysql_select_db("ebs", $con);
 
$sql="INSERT IGNORE INTO db (hostname, uname, ip, os, status) VALUES ('$_POST[hostname]', '$_POST[uname]', '$_POST[ip]', '$_POST[os]', '$_POST[status]')";
 
if (!mysql_query($sql,$con))
  {
  die('Error: ' . mysql_error());
  }
echo "1 record added";
 
mysql_close($con)
?>
</body>
</html>
