<?php 
    function select (array $refrescos){
        echo "<form>";
        echo "<select name=\"opcion\">";
        foreach($refrescos as $x=>$marca){
            echo "<option value=$x>";          
            echo $marca["text"]."  (".$marca["precio"]." €)";        
            echo "</option>";
        }
        echo "</select>";
        echo "</form>";
    }
?>
<html>
    <head>
        <title>Generate a select dynamically.</title>
        <meta charset="utf-8">
        <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
        <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
    </head>
    <body>
        <div class="container-fluid">
            <h1>Generate a select dynamically.</h1>
            <?php
                $refrescos = array (
                    "cocacola" => array ("text"=>"Coca Cola","precio"=>2.1),
                    "pesicola" => array ("text"=>"Pepsi Cola","precio"=>2),
                    "fanta" => array("text"=>"Fanta Naranja","precio"=>2.5),
                    "trina" => array ("text"=>"Trina Manzana","precio"=>2.3)
                );

                select($refrescos);

            ?>
        </div>
    </body>
</html>