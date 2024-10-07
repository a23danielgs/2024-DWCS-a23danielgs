<?php        
    function test_input($data) {
        $data = trim($data);
        $data = stripslashes($data);
        $data = htmlspecialchars($data);
        return $data;
    }  
    function options (array $array,$data){
        foreach($array as $key=>$value){
            if($data==$value){
                echo "<option value=\"$value\" selected=\"selected\">";          
                echo $key;       
                echo "</option>";
            }else{
                echo "<option value=\"$value\">";          
                echo $key;       
                echo "</option>";
            }
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
        select{
            margin-bottom: 30px;
        }
    </style>
</head>
<body>
    <?php
        $name = $subject ="";
        $nameErr = $subjectErr = "";

        $Subjects = array (
            "Java Programming" => 0,
            "Web Design" => 1,
            "Dockers administration" => 2,
            "Django framework" => 3,
            "Mongo database" => 4
        );

        if($_SERVER["REQUEST_METHOD"] == "GET"){
            if(empty($_GET["name"])){
                $nameErr = "Name and surname is needed";
            }else{
                $name = test_input($_GET["name"]);
            }

            if(empty($_GET["subject"]) && ($_GET["subject"]!=0)){
                $subjectErr = "You must choose a subject";
            }else{
                $subject = test_input($_GET["subject"]);
            }
        }
    ?>
    
    <form method="POST" action ="manage.php">
        <div id="column1">
            <p>Name and surnames:</p>
            <p>Subject to enroll:</p>
            <p>Type of your classes:</p>
            <input type="submit" value="Send data">
        </div>
        <div id="column2">
            <input required id="Barr" type="text" name="name" value=<?php echo $name?>>

            <select name="subject">
            <?php options($Subjects,$subject)?>
            </select>
            <div id="ButtonsText">
                <input type="radio" name="classes" value="In-person">In-person classes
                <input type="radio" name="classes" value="Distance">Distance classes
            </div>
        </div>

    </form>
</body>
</html>