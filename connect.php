<?php
    $host = 'localhost';
    $user = 'root';
    $password = "";
    $database = "POM";

    $connect = mysqli_connect($host. $user,
    $password, $database)
    or die ('connection failed'0)

?>