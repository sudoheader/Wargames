#!/usr/bin/php
<?php

$defaultdata = array( "showpassword" => "no", "bgcolor" => "#ffffff");

function xor_encrypt($in, $key) {

    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i = 0; $i < strlen($text); $i++) {
        $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}
// A ^ B = C
// A ^ C = B (reversing it)
// plaintext ^ key = ciphertext
// plaintext ^ ciphertext = key

$plaintext = json_encode($defaultdata);
$ciphertext = hex2bin('0a554b221e00482b02044f2503131a70531957685d555a2d121854250355026852115e2c17115e680c');
$key = 'qw8J';

// echo(xor_encrypt($plaintext, $ciphertext));

$good_data = array( "showpassword" => "yes", "bgcolor" => "#ffffff");

$good_plaintext = json_encode($good_data);
$good_ciphertext = xor_encrypt($good_plaintext, $key);

$cookie = base64_encode($good_ciphertext);

echo($cookie);

?>
