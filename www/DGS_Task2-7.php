<?php 
    function select (array $refrescos){
        foreach($refrescos as $x=>$marca){
            echo "<option value=$x>";          
            echo $marca["text"]."  (".$marca["precio"]." €)";        
            echo "</option>";
        }
    }
    function test_input($data) {
        $data = trim($data);
        $data = stripslashes($data);
        $data = htmlspecialchars($data);
        return $data;
    }
?>
<html>
    <head>
        <title>Form</title>
        <meta charset="utf-8">
        <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
        <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
        <style>
        .error {color: #FF0000;}
        </style>
    </head>
    <body>
        <div class="container-fluid">
            <h1>Form</h1>
            <?php
                $cantidad = $precioTotal =0;
                $opcion = $cantidadErr = "";
                $refrescos = array (
                    "cocacola" => array ("text"=>"Coca Cola","precio"=>2.1),
                    "pesicola" => array ("text"=>"Pepsi Cola","precio"=>2),
                    "fanta" => array("text"=>"Fanta Naranja","precio"=>2.5),
                    "trina" => array ("text"=>"Trina Manzana","precio"=>2.3)
                );
                if($_SERVER["REQUEST_METHOD"] == "POST"){
                    if($_POST["cantidad"] == 0){
                        $cantidad = test_input($_POST["cantidad"]);
                    }
                    elseif(empty($_POST["cantidad"])){
                        $cantidadErr = "No se puede dejar el campo vacio";
                    }elseif($_POST["cantidad"]<0){
                        $cantidadErr = "No se puden seleccionar números negativos";
                    }else{
                        $cantidad = test_input($_POST["cantidad"]);
                    }

                    $opcion = test_input($_POST["opcion"]);

                    $NUM = $refrescos[$opcion]["precio"];               
                    $precioTotal = $cantidad*$NUM;
                }
            ?>
                <form method="POST" action ="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
                    <select name="opcion">
                        <?php select($refrescos);?>
                    </select>
                    <br><input value=0 type="number" name="cantidad"/><span class="error">*<?php echo $cantidadErr;?></span>
                    <br><input type="submit"/>
                </form>

        </div>
    </body>
</html>