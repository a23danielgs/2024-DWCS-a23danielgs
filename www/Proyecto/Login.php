<?php
session_start();
//Check the user input so that it is safe
function test_input($data)
{
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}
/*Login form
If the user and password are correct it stores the user name and redirects to principal.php 
if the user and password are not correct it shows an error message */
function comprobar_usuario($nombre, $clave)
{
    if ($nombre === "usuario" and $clave === "1234") {
        $usu['nombre'] = "usuario";
        $usu['rol'] = 0;
        return $usu;
    } elseif ($nombre === "admin" and $clave === "1234") {
        $usu['nombre'] = "admin";
        $usu['rol'] = 1;
        return $usu;
    } else return false;
}
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $usuario = test_input($_POST['usuario']);
    $clave = test_input($_POST['clave']);
    $usu = comprobar_usuario($usuario, $clave);
    if ($usu == false) {
        $err = true;
        $usuario = $_POST['usuario'];
    } else {
        $_SESSION['usuario'] = $usuario;
        header("Location: Main.php");
    }
}
?>
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel='stylesheet' type='text/css' media='screen' href='Login.css'>
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
                        <li><a href="./Main.php">Main</a></li>
                        <li><a href="./Form.php">Form</a></li>
                        <li><a href="./Info.php">Info</a></li>
                        <li><a href="./Photos.php">Photos</a></li>
                        <li>
                            <p>|</p>
                        </li>
                        <li><a id="Login">Login</a></li>
                    </ul>

                </section>
            </div>
        </div>
    </header>
    <?php if (isset($_GET["redirigido"])) {
        echo "<p class=\"error\">Please introduce login to continue </p>";
    } ?>
    <?php if (isset($err) and $err == true) {
        echo "<p class=\"error\"> Please check user and password </p>";
    }

    if (isset($_SESSION['usuario'])) {
        echo "<h2>HOWI</h2>";
        echo "<h2>" . session_status() . "</h2>";
    } else {
    ?>
        <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="POST">
            <h2>User:
                <input id="usuario" name="usuario" type="text" value="<?php if (isset($usuario)) echo $usuario; ?>">
            </h2>
            <br><br>
            <h2>Password:
                <input id="clave" name="clave" type="password">
            </h2>
            <br><br>
            <input id="Buttom" type="submit" name="sendLogin" value="Send Request">
        </form>
        <p> </p>

        <p> </p>
    <?php
    }
    ?>
    <footer></footer>
</body>

</html>