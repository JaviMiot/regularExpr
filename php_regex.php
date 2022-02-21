<?<php>
$file = fopen("./results.csv", "r")

$match =0;
$nomatch =0;

while (!feof($file)) {
    $line = fgets($file);
    if(preg_match(
        /^2018\-01\-(\d{2}).*$/,
        $line,
        $m
    )){
        print_r($m)
        $match++;
    }else{
        $nomatch++;
    }
    echo $line;
}

fclose($file);

printtf("\n\nmatch %d\n no match %d\nnomatch %d\n",
$match, $nomatch);


</php>