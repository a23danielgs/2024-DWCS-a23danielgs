<?php          
    function test_input($data) {
        $data = trim($data);
        $data = stripslashes($data);
        $data = htmlspecialchars($data);
        return $data;
    }
?>
<html>
    <body>
        <?php
            $name = $email = "";
            if ($_SERVER["REQUEST_METHOD"] == "POST") {
              $name = test_input($_POST["name"]);
              $email = test_input($_POST["email"]);

            }
        ?>
        Welcome <?php echo$name?><br>
        Your email address is: <?php echo$email?> 
    </body>
</html>