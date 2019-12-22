<?php

    $name = $_POST['name'];
    $mail = $_POST['mail'];
    $toiawase = $_POST['toiawase'];

    $mailTO = "test@test.com"; // メールの送信先
    $mailHeader = "From: from@from.com"; // メールの送信者
    $mailSubject = "お問い合わせありがとうございます"; // メールの件名
    $mailBody = '
    $name 様\r\n
    お問い合わせありがとうございます\r\n
    \r\n
    ご返信まで～～～～';

    mail($mailTO, $mailSubject, $mailBody, $mailHeader);


echo "
<!DOCTYPE html>
<html>
<head>
<meta charset='UTF-8'>
<title>Insert title here</title>
</head>
<body>
お問い合わせありがとうございます。
</body>
</html>
";