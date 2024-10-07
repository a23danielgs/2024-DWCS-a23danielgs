<?php          
    function options (array $array){
        foreach($array as $key=>$value){
            echo "<option value=\"$value\">";          
            echo $key;       
            echo "</option>";
        }
    }
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .error {color: #FF0000;}
        form{
            display: flex;
            flex-direction: row;
        }
        #column1{
            display: flex;
            flex-direction: column;
        }
        #column2{
            display: flex;
            flex-direction: column;
            margin-left:5px;
        }
        #Barr{
            margin-top: 15px;
            margin-bottom: 30px;
        }
    </style>
</head>
<body>
    <?php
        $Subjects = array (
            "Java Programming" => 0,
            "Web Design" => 1,
            "Dockers administration" => 2,
            "Django framework" => 3,
            "Mongo database" => 4
        );
    ?>
    
    <form method="POST" action ="manage.php">
        <div id="column1">
            <p>Name and surnames:</p>
            <p>Subject to enroll:</p>
            <input type="submit" value="Send data">
        </div>
        <div id="column2">
            <input id="Barr" type="text" name="name">

            <select name="subject">
            <?php options($Subjects)?>
            </select>
        </div>

    </form>
</body>
</html>