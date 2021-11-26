<?php
//avataan yhteys mysql tietokantaan "tunnukset"
mysql_connect("localhost", "root", "salasana") or die("ei yhteyttä");
mysql_select_db("tunnukset");

//Otetaan vastaan kirjautumislomakkeesta tulleet tiedot
$kayttajatunnus = $_POST['kayttajatunnus'];
$salasana = $_POST['salasana'];

//Tässä kohtaa koodia tulisi käsitellä syötteen turvallisuus
// Nyt sitä ei tehdä, joten kirjautumissivu on haavoittuvainen SQL injektiolle!

// muodostetaan kysely, suoritetaan se ja lasketaan kyselyn rivit
$kysely = "SELECT * FROM tunnukset WHERE kayttajanimi='$kayttajatunnus' AND salasana='$salasana'";
$tulos = mysql_query($kysely);
$rivit = mysql_num_rows($tulos);
// jos kysely palauttaa vain yhden rivin = kirjautuminen on onnistunut
// muussa tapauksessa kerrotaan epäonnistuneesta kirjautumisesta
if ($rivit == 1) {
header("location:kirjautuminen_onnistui.php");
}
else {
echo "Virhe kirjautumisessa" . "<br>";
}
?>
