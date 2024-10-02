<?php declare(strict_types=1); 
    function nombrar (?string $name,int $age,string $surname="Apelido"){
        echo "<p><b>".$name." ".$surname." is ".$age." years old.</b></p>";
    }
?>
<html>
    <head>
        <title>Functions</title>
        <meta charset="utf-8">
        <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
        <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
    </head>
    <body>
        <div class="container-fluid">
            <h1>Functions</h1>
            <?php
                define("nombre","Jose Manuel");
                define("apellido","Sánchez");
                define("edad",30);
                nombrar(nombre,edad,apellido);
                nombrar(null,0);
            ?>
        </div>
    </body>
</html>