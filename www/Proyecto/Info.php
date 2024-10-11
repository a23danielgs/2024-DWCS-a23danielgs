<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel='stylesheet' type='text/css' media='screen' href='Info.css'>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Dosis">
</head>

<body>
    <header>
        <div id="Header1">
            <a href=""><img src="img/Zorrito.png" title="Mascot" alt="Mascota" width="250" height="260" /></a>
            <div id="Header2">
                <h1>Campament Settlement</h1>
                <section>
                    <ul>
                        <li><a href="#">Main</a></li>
                        <li><a href="#">Form</a></li>
                        <li><a href="#">Info</a></li>
                        <li><a href="#">Photos</a></li>
                        <li>
                            <p>|</p>
                        </li>
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
</body>

</html>