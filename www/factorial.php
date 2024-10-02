<html>
    <head>
        <title>CalculadoraF</title>
        <meta charset="utf-8">
        <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
        <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
        <style>
            h1 {
                color:green;
            }
            p {
                font-weight: bolder;
            }
        </style>
    </head>
    <body>
        <div class="container-fluid">
            <h1>Calculadora factorial</h1>
            <?php                
                $factorial=12;
                $resultado=1;
               
                for($x=$factorial;$x>0;$x--){
                    $resultado=$resultado*$x;
                }

                echo "<p>El resultado del factorial de $factorial es $resultado</p>";
            ?>
        </div>
    </body>
</html>
