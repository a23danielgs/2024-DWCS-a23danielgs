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
            ?>
            <h2><?php echo $name?> wants to enroll in <?php echo recorrer_array($subject,$Subjects)?></h2>
    <?php
        }
    ?>

    </body>
</html>