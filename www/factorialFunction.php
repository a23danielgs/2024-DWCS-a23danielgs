<?php declare(strict_types=1); 
    function factorial(int $factorial):int{
        $resultado=1; 
        if(numero>=0){
            for($x=$factorial;$x>0;$x--){
                $resultado=$resultado*$x;
            }
            return $resultado;
        }else{
            throw new Exception("El factorial de un número menor que 0 no es calculable");
        }              
    }
?>
<html>
    <head>
        <title>CalculadoraFF</title>
        <meta charset="utf-8">
        <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
        <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
    </head>
    <body>
        <div class="container-fluid">
            <h1>Calculadora factorial</h1>
            <?php
            define("numero",0);                
            try{            
                echo "<p>El resultado del factorial de ".numero." es ".factorial(numero)."</p>";              
            }catch(Exception $e){
                echo 'Message: '.$e->getMessage();
            }                  
            ?>
        </div>
    </body>
</html>
