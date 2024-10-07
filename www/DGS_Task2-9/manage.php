<?php           
    function test_input($data) {
        $data = trim($data);
        $data = stripslashes($data);
        $data = htmlspecialchars($data);
        return $data;
    }
    function recorrer_array($data, array $array){
        foreach($array as $key=>$value){
            if($data == $value){
                return $key;
            }
        }
    }
?>
<html>
    <head>
    <style>
        .error {color: #FF0000;}
    </style>
    </head>
    <body>
    <?php
        $name = $subject = $classes ="";
        $nameErr = $subjectErr = $classesErr ="";

        $Subjects = array (
            "Java Programming" => 0,
            "Web Design" => 1,
            "Dockers administration" => 2,
            "Django framework" => 3,
            "Mongo database" => 4
        );

        if($_SERVER["REQUEST_METHOD"] == "POST"){
            if(empty($_POST["name"])){
                $nameErr = "Name and surname is needed";
            }else{
                $name = test_input($_POST["name"]);
            }

            if(empty($_POST["subject"]) && ($_POST["subject"]!=0)){
                $subjectErr = "You must choose a subject";
            }else{
                $subject = test_input($_POST["subject"]);
            }

            if(empty($_POST["classes"])){
                $classesErr = "You must select a type of classes";
            }else{
                $classes = test_input($_POST["classes"]);
            }
            
            if($classes !== ""){
                if($classesErr!==""){
                    ?>
                    <a href="manage2.php"><span class="error"><?php echo $classErr ?></span></a>
                    <?php
                }else{
                    if($nameErr==""){
                        ?>
                            <h2><?php echo $name?> wants to enroll in <?php echo recorrer_array($subject,$Subjects)?> and <?php echo $classes?> classes</h2>
                        <?php
                    }else{
                            ?>
                            <a href="formulario.php"><span class="error"><?php echo $nameErr ?></span></a>
                        <?php
                    }
                }
            }else{
                if($nameErr==""){
                ?>
                    <h2><?php echo $name?> wants to enroll in <?php echo recorrer_array($subject,$Subjects)?></h2>
                    <a href="./manage2.php?name=<?php echo $name?>&subject=<?php echo $subject?>">Seguinte páxina</a>
                <?php
                }else{
                    ?>
                    <a href="formulario.php"><span class="error"><?php echo $nameErr ?></span></a>
                <?php
                }
            }
        }
    ?>

    </body>
</html>