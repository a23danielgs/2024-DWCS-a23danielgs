<?php
session_start();
?>
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel='stylesheet' type='text/css' media='screen' href='Main.css?v=2'>
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
                    <li id="Main"><a id="MainLink" href="#">Main</a></li>
                    <li id="Form"><a href="Form.php">Form</a></li>
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
    </header>
    <div id="Text">
        <?php
        if (isset($_SESSION['usuario'])) {
        ?>
            <h2>Welcome back!</h2>
            <h2><br>summer has ended, we can´t wait to see you all next summer, right now we are working on preparing the camp for next´s year we will thank all our campers to fill the <a href="Form.php">form</a> so we can know what to improve! :] </h2>
        <?php
        } else {
        ?>

            <h2>Hello! <br>summer has ended, we can´t wait to see you all next summer, right now we are working on preparing the camp for next´s year we will thank all our campers to fill the <a href="Form.php">form</a> so we can know what to improve! :] </h2>
        <?php
        }
        ?>
    </div>
    <footer>

    </footer>
</body>

</html>