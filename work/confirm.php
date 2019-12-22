<?php

    $name = $_POST['name'];
    $mail = $_POST['mail'];
    $toiawase = $_POST['toiawase'];

echo "
<!DOCTYPE html>
<html>
<head>
<meta charset='UTF-8'>
<title>Insert title here</title>
</head>
<body>
お名前：$name
</br>
メールアドレス：$mail
</br>
お問い合わせ内容
</br>
$toiawase
</br>
</br>
<form action='complete.php' method='post'>
<input type='hidden' name='name' value='$name'>
<input type='hidden' name='mail' value='$mail'>
<input type='hidden' name='toiawase' value='$toiawase'>
<input type='button' onclick='history.back()' value='戻る''>
<input type='submit' value='確認'>
</form>
</body>
</html>";