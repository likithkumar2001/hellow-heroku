<?php
$conn = 'example';
$temp = exec("python print.py .$conn");
echo $temp;
?>