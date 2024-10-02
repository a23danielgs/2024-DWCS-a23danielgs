<?php          
    function test_input($data) {
        $data = trim($data);
        $data = stripslashes($data);
        $data = htmlspecialchars($data);
        return $data;
    }
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .error {color: #FF0000;}
    </style>
</head>
<body>
    <?php
        $name = $email = "";
        $nameErr = $emailErr = "";
        if($_SERVER["REQUEST_METHOD"] == "POST"){
            if(empty($_POST["name"])){
                $nameErr = "Name is required";
            }else{
                $name = test_input($_POST["name"]);
            }

            if(empty($_POST["email"])){
                $emailErr = "Email is required";
            }else{
                $email = test_input($_POST["email"]);
            }
        }
    ?>
    <p><span class="error">* required field</span></p>
    <form method="POST" action ="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
        Name <input value="<?php echo $name?>" type ="text" name="name"/><span class="error">*<?php echo $nameErr;?></span>
        <br>Email <input value="<?php echo $email?>" type="text" name="email"/><span class="error">*<?php echo $emailErr;?></span>
        <br><input type ="submit"/>
    </form>
    <?php
    if($_SERVER["REQUEST_METHOD"] == "POST"){
        if($nameErr==""){
            if($emailErr==""){
                echo "<h2>Your Input:</h2>";
                echo "<p>Welcome $name</p>";
                echo "<p>Your email : $email</p>";
            }
        }
    }               
    ?>
</body>
</html>