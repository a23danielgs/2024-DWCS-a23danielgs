<?php declare(strict_types=1); 
    function elevar(int $base,int $exponente = 2):int{
        $resultado = 1;
        for(;$exponente>0;$exponente--){
            $resultado=$resultado*$base;
        }
        return $resultado;
    }
?>
<html>
    <head>
        <title>CalculadoraP</title>
        <meta charset="utf-8">
        <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
        <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
    </head>
    <body>
        <div class="container-fluid">
            <h1>Calculadora de potencias</h1>
            <?php
               define("numero",3);
               define("exponente",-3);
               try{
                echo "<p>La potencia de ".numero." elevado a ".exponente." es ".elevar(numero,exponente)."</p>";   
               }
               catch(Exception $erro){
                echo "<p> Type erro ".$erro->getMessage()."</p>";
               }
              
            ?>
        </div>
    </body>
</html>