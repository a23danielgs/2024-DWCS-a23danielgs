<?php
session_start();
?>
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel='stylesheet' type='text/css' media='screen' href='Form.css?v=2'>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Dosis">
</head>

<body>
    <header>
        <div id="Header1">
            <div id="Header2">
                <img src="img/Zorrito.png" title="Mascot" alt="Mascota" width="150" height="150" />

                <h1>Campament Settlement</h1>
            </div>
            <section>
                <ul>
                    <li id="Main"><a href="#">Main</a></li>
                    <li id="Form"><a id="MainLink" href="Form.php">Form</a></li>
                    <li id="Info"><a href="#">Info</a></li>
                    <li id="Photos"><a href="#">Photos</a></li>
                    <li>
                        <?php
                        if (isset($_SESSION['usuario'])) {
                            echo "<p>Bienvenido!&emsp;<a href=\".\Logout.php\">Logout</a></p>";
                        } else {
                            echo "<a href=\".\Login.php\">Login</a>";
                        }
                        ?>
                    </li>
                </ul>

            </section>

        </div>
        </div>
    </header>
    <div id="Formulario">
        <?php
        if (isset($_SESSION['usuario'])) {
        ?>
            <form method="POST" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
                <div id="Block">
                    What activities did you enjoy the most during camp?
                    <select name="server" size="">
                        <option value=""></option>
                        <option value="1">Team Sports</option>
                        <option value="2">Outdoor Movie Night</option>
                        <option value="3">Campfire Cooking</option>
                        <option value="4">Arts and Crafts</option>
                        <option value="5">Obstacle Course</option>
                        <option value="6">DIY Tie-Dye</option>
                    </select>
                    <span class="error"></span><br>
                </div>
                <div id="Block">
                    How would you rate the food at camp?
                    <div id="Buttons">
                        <div id="ButtonsText">
                            <input type="radio" name="role" <?php if (isset($role) && $role == "Admin") echo "checked"; ?>
                                value="Admin">Admin
                        </div>
                        <div id="ButtonsText">
                            <input type="radio" name="role" <?php if (isset($role) && $role == "Engineer") echo "checked"; ?>
                                value="Engineer">Engineer
                        </div>
                        <div id="ButtonsText">
                            <input type="radio" name="role" <?php if (isset($role) && $role == "Manager") echo "checked"; ?>
                                value="Manager">Manager
                        </div>
                        <div id="ButtonsText">
                            <input type="radio" name="role" <?php if (isset($role) && $role == "Guest") echo "checked"; ?>
                                value="Guest">Guest
                        </div>
                        <span class="error"><?php echo $roleErr; ?></span><br>
                    </div>
                </div>


                <input type="submit" value="Login">
                <input type="reset" value="Reset">

            </form>


        <?php
        } else {
        ?>
            <h2>Please<a href="./Login.php"> Login</a> to fill the form</h2>
        <?php
        }
        ?>
    </div>
    <footer>

    </footer>
</body>

</html>