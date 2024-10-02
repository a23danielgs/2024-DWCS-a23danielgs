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
    <title>Form II</title>
    <style>
        .message{color:#77DD77;}
        .error {color: #FF0000;}
        #Block{
            display: flex;
            flex-direction: row;
            align-items: center;
            margin-top: 30px;
        }
        #Buttons{
            display: flex;
            flex-direction: column;
        }
        #ButtonsText{
            display: flex;
            flex-direction: row;
        }
        #Barr{
            margin-bottom: 5px;
        }
    </style>
</head>
<body>
    <?php
        $name = $pass = $city = $server = $role = $sign1 = $sign2 = $sign3 ="";
        $nameErr = $passErr = $cityErr = $serverErr= $roleErr = $signErr ="";
        if($_SERVER["REQUEST_METHOD"] == "POST"){
            if(empty($_POST["name"])){
                $nameErr = "Username is required";
            }else{
                $name = test_input($_POST["name"]);
            }

            if(empty($_POST["password"])){
                $passErr = "Password is required";
            }else{
                $pass = test_input($_POST["password"]);
            }

            if(empty($_POST["city"])){
                $cityErr = "City of employment is required";
            }else{
                $city = test_input($_POST["city"]);
            }

            if(empty($_POST["server"])){
                $serverErr = "You must choose a server";
            }else{
                $server = ($_POST["server"]);
            }

            if(empty($_POST["role"])){
                $roleErr = "Role is required";
            }else{
                $role = $_POST["role"];
            }

            if(empty($_POST["sign1"])){
            }else{
                $sign1 = test_input($_POST["sign1"]);
            }

            if(empty($_POST["sign2"])){
            }else{
                $sign2 = test_input($_POST["sign2"]);
            }

            if(empty($_POST["sign3"])){
            }else{
                $sign3 = test_input($_POST["sign3"]);
            }

            if(empty($_POST["sign1"])){
                if(empty($_POST["sign2"])){
                    if(empty($_POST["sign3"])){
                        $signErr = "A type of Sign-on is required";
                    }
                }
            }
            
        }
    ?>

    <h1>Novell Services Login</h1>
    <form method="POST" action ="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
        Username:&emsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <input required id="Barr" type="text" name="name" value="<?php echo $name?>">
        <span class="error"><?php echo $nameErr ?></span><br>

        Password:&emsp;&emsp;&nbsp;&nbsp;
        <input required id="Barr" type="text" name="password" value="<?php echo $pass?>">
        <span class="error"><?php echo $passErr ?></span><br>

        City of<br>Employment:&emsp;&nbsp;
        <input id="Barr" type="text" name="city" value="<?php echo $city?>">
        <span class="error"><?php echo $cityErr ?></span><br>

        Web server:&emsp;&emsp;
        <select name="server">
            <option value="">-- Choose a server --</option>
            <option value="Server 1" <?php if (isset($server) && $server=="Server 1") echo "selected";?>>Apache</option>
            <option value="Server 2" <?php if (isset($server) && $server=="Server 2") echo "selected";?>>Engine X</option>
        </select>
        <span class="error"><?php echo $serverErr ?></span><br>


        <div id="Block">
            Please specify<br>your role:&emsp;&emsp;&nbsp;&nbsp;&nbsp;
            <div id="Buttons">
                <div id="ButtonsText">
                    <input type="radio" name="role" <?php if (isset($role) && $role=="Admin") echo "checked";?> 
                    value="Admin">Admin
                </div>
                <div id="ButtonsText">
                    <input type="radio" name="role" <?php if (isset($role) && $role=="Engineer") echo "checked";?> 
                    value="Engineer">Engineer
                </div>
                <div id="ButtonsText">
                    <input type="radio" name="role" <?php if (isset($role) && $role=="Manager") echo "checked";?> 
                    value="Manager">Manager
                </div>
                <div id="ButtonsText">
                    <input type="radio" name="role" <?php if (isset($role) && $role=="Guest") echo "checked";?>
                    value="Guest">Guest
                </div>
                    <span class="error"><?php echo $roleErr;?></span><br>
            </div>
        </div>

        <div id="Block">
            Single Sign-on<br>to the following:
            <div id="Buttons">
                <div id="ButtonsText">
                    <input type="checkbox" name="sign1" <?php if (isset($sign1) && $sign1=="Mail") echo "checked"; ?> 
                    value="Mail">Mail
                </div>
                <div id="ButtonsText">
                    <input type="checkbox" name="sign2" <?php if (isset($sign2) && $sign2=="Payroll") echo "checked"; ?> 
                    value="Payroll">Payroll
                </div>
                <div id="ButtonsText">
                    <input type="checkbox" name="sign3" <?php if (isset($sign3) && $sign3=="Self-service") echo "checked"; ?> 
                    value="Self-service">Self-service               
                </div>
                <?php
                    if(empty($sign1)){
                        if(empty($sign2)){
                            if(empty($sign3)){
                                echo "<span class = \"error\">$signErr</span>";
                            }
                        }
                    }
                ?>
            </div>
        </div>

        <input type="submit" value="Login">
        <input type="reset" value="Reset">

    </form>
    <?php
        if($_SERVER["REQUEST_METHOD"] == "POST"){
            if($nameErr==""){
                if($passErr==""){
                    if($cityErr==""){
                        if($serverErr==""){
                            if($roleErr==""){
                                if($signErr==""){
                                    echo "<p class=\"message\">El formulario fue envidao sin errores</p>";
                                }
                            }
                        }
                    }
                }
            }
        }
    ?>
</body>
</html>
