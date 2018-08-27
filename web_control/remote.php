<?php
    if (isset($_POST['button1']))
    {
       system("gpio mode 0 out");
       system("gpio write 0 1");
	   system("gpio mode 1 out");
       system("gpio write 1 1");
	   system("gpio mode 3 out");
       system("gpio write 3 0");
	   system("gpio mode 4 out");
       system("gpio write 4 0");
    }
    if (isset($_POST['button2']))
    {
       system("gpio mode 0 out");
       system("gpio write 0 0");
	   system("gpio mode 1 out");
       system("gpio write 1 0");
	   system("gpio mode 3 out");
       system("gpio write 3 1");
	   system("gpio mode 4 out");
       system("gpio write 4 1");
    }
	if (isset($_POST['button4']))
    {
       system("gpio mode 0 out");
       system("gpio write 0 0");
	   system("gpio mode 1 out");
       system("gpio write 1 1");
	   system("gpio mode 3 out");
       system("gpio write 3 1");
	   system("gpio mode 4 out");
       system("gpio write 4 0");
    }
    if (isset($_POST['button3']))
    {
       system("gpio mode 0 out");
       system("gpio write 0 1");
	   system("gpio mode 1 out");
       system("gpio write 1 0");
	   system("gpio mode 3 out");
       system("gpio write 3 0");
	   system("gpio mode 4 out");
       system("gpio write 4 1");
    }
	if (isset($_POST['button5']))
    {
       system("gpio mode 0 out");
       system("gpio write 0 0");
	   system("gpio mode 1 out");
       system("gpio write 1 0");
	   system("gpio mode 3 out");
       system("gpio write 3 0");
	   system("gpio mode 4 out");
       system("gpio write 4 0");
    }
?>
<html>
<body>
    <form method="post">
    <table align="center">
	<tr><td></td><td><button name="button1">Forward</button></td></tr>
	<tr><td>  </td><td>  </td></tr>
	<tr><td><button name="button3">Right</button></td><td><button name="button5">Reverse</button></td><td><button name="button4">Left</button></td></tr>
	<tr><td>  </td><td>  </td></tr>
	<tr><td></td><td><button name="button5">Stop</button></td></tr>
    </table>
    </form>
</body>
