<?php
//session_start();

//session_unset();

//session_destroy();

//header('Location: Main.php');
//exit; 

session_start();
// remove all session variables
session_unset();

// destroy the session
session_destroy();
header("Location: Main.php");
?>
<!DOCTYPE html>
<html>

<body>

</body>

</html>