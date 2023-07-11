<?php
$file_name = $_FILES['file']['name'];
$file_tmp = $_FILES['file']['tmp_name'];
move_uploaded_file($file_tmp,'/home/srsssmsc/grading.srs-ssms.com/public/img/ffb/');
echo "file uploaded"
?>
