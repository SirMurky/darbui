<?PHP ini_set("memory_limit","32M");?>
<?PHP
    include_once("prisijungti.php");

    $query = "select A.TAIL_NUMBER, B.MODEL_NUMBER, B.DESCRIPTION , C.COMPANY_NAME, D.CODE,
 D.COUNTRY_NAME from `aircraft` as A inner join model as B inner
 join companies as C inner join country_codes as D on SDF_COC_003 = 'T' limit 20"; 
    
    $result = mysqli_query($conn, $query);
    
    while($row = mysqli_fetch_assoc($result)){
            $data[] = $row;
    }
    echo json_encode($data);
?>