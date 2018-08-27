<?php
$page = $_SERVER['PHP_SELF'];
$sec = "2";
?>
<html>
    <head>
    <meta http-equiv="refresh" content="<?php echo $sec?>;URL='<?php echo $page?>'">
    </head>
    <body>
    <?php
	$resp=array();
	$r1=array("|","+");
	$r2=array("Physical","Pi 3"," ");
	$r3=array("Physical||Physical","|Pi 3|","");
        exec('gpio readall',$resp);
	echo "<style>table,td{padding:5px;border:2px solid black;border-collapse:collapse;} ";
	echo "tr:nth-child(even){background-color:#dddddd;}";
        echo "td:nth-child(3){background:#ffe653}";
        echo "td:nth-child(4){background:#96e7cf}";
        echo "td:nth-child(6){background:#8ed861}";
	echo "td:nth-child(12){background:#96e7cf}";
	echo "td:nth-child(10){background:#8ed861}";
        echo "td:nth-child(13){background:#ffe653}";
	echo "td:nth-child(15){display:none}";
	echo "td:nth-child(1){display:none}";
        echo "";
        echo "";
        echo "tr:nth-child(3){display:none}";
        echo "tr:nth-child(24){display:none}";
        echo "tr:nth-child(26){display:none}";
        echo "tr:nth-child(2){background:#ee5133}";
        echo "tr:nth-child(25){background:#ee5133}";
	echo "</style>";
	echo"<table style='width:auto' align='center'>";
	foreach($resp as $line){
	$q1=str_replace($r2,$r3,$line);
	$lk=str_replace($r1,"</td>\n<td>",$q1);
	echo "<p><tr><td>$lk</td></tr></p>";}
	echo"</table>";
    ?>
    </body>
</html>
