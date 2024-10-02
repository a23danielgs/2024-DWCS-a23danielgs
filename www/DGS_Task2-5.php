<?php 
    function tripleCheck(array $array){
        $count=0;
        $anterior="";
        foreach($array as $value){          
            if($value==$anterior){              
                $count++;
            }else{
                $count=0;
            }           
            if($count==2){
                return true;
            }  
            $anterior=$value;
        }
        return false;
    }
    function countries(array $array){
        foreach($array as $country=>$capital){
            echo "The capital of ".$country." is ".$capital."<br>";
        }
    }
?>
<html>
    <head>
        <title>Working with arrays</title>
        <meta charset="utf-8">
        <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
        <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
    </head>
    <body>
        <div class="container-fluid">
            <h1>Working with arrays</h1>
            <?php
                echo"<h2>1.Triplecheck</h2>";
                $uno = array(1,1,2,2,1);
                $dos = array(1,1,2,1,2,3);
                $tres = array(1,1,1,2,2,2,1);
                echo var_dump(tripleCheck($uno));echo "<br>";
                echo var_dump(tripleCheck($dos));echo "<br>";
                echo var_dump(tripleCheck($tres));echo "<br>";

                echo"<h2>2.countries</h2>";
                $ceu = array( "Italy"=>"Rome", "Luxembourg"=>"Luxembourg", "Belgium"=> "Brussels", "Denmark"=>"Copenhagen", "Finland"=>"Helsinki", "France" => "Paris", "Slovakia"=>"Bratislava", "Slovenia"=>"Ljubljana", "Germany" => "Berlin", "Greece" => "Athens", "Ireland"=>"Dublin", "Netherlands"=>"Amsterdam", "Portugal"=>"Lisbon", "Spain"=>"Madrid", "Sweden"=>"Stockholm", "United Kingdom"=>"London", "Cyprus"=>"Nicosia", "Lithuania"=>"Vilnius", "Czech Republic"=>"Prague", "Estonia"=>"Tallin", "Hungary"=>"Budapest", "Latvia"=>"Riga", "Malta"=>"Valetta", "Austria" => "Vienna", "Poland"=>"Warsaw") ;

                countries($ceu);
            ?>
        </div>
    </body>
</html>