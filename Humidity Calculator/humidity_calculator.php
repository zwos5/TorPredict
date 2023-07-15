<?php
echo "<link rel='stylesheet' type='text/css' href='calc_styles.css' />";

$wvapor_mass = "";
$aw_mix_volume = "";
$partial_pressure = "";
$sat_vapor_pressure = "";

$aHumidity = "";
$rHumidity = "";

function data_test($data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if(!empty($_POST["wvapor_mass"])) {
        $wvapor_mass = data_test($_POST["wvapor_mass"]);
    }

    if(!empty($_POST["aw_mix_volume"])) {
        $aw_mix_volume = data_test($_POST["aw_mix_volume"]);
    }
}

$aHumidity = $wvapor_mass / $aw_mix_volume;
$rHumidity = 100 * ($partial_pressure/$sat_vapor_pressure);

?>
<html>
<head>
<title> Humidity Calculator </title>
</head>

<body>
<a href="tornadowebreport.html">Tornado Report</a>
<a href="checkArea.html">Check Your Local Area</a>
<a href="chatbot.html">Tornadics.ai</a>
<a href="humidity_calculator.php">Humidity Calculator</a>
<h2>Humidity Calculator</h2>

<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>"> <p>
Water Vapor Mass: <input type="text" name="wvapor_mass" value="<?php echo $wvapor_mass; ?>"> <p>
Volume of Air and Water Vapor Mixture: <input type="text" name="aw_mix_volume" value="<?php echo $aw_mix_volume; ?>"> <p>
<input type="submit" value="Calculate Abolute Humidity"> <p>

Absolute Humidity: <input type="text" name="aHumidity" value="<?php echo $aHumidity; ?>"> <p>
<p>
Ratio of partial pressure of water vapor: <input type="text" name="partial_pressure" value="<?php echo $partial_pressure; ?>"> <p>
Saturation Vapor Pressure: <input type="text" name="sat_vapor_pressure" value="<?php echo $sat_vapor_pressure; ?>"> <p>

Relative Humidity: <input type="text" name="rHumidity" value="<?php echo $rHumidity; ?>"> <p>

</body>
</html>