<!DOCTYPE HTML>
<html lang="ja">
    <head>
        <meta charset="utf-8">
        <title>Miyawaki Shumpei| 宮脇峻平</title>
    </head>
    <body>
        <?php
			mb_language("Japanese");
			mb_internal_encoding("UTF-8");

			$to = "skow.kitten@icloud.com";
			$title = $_POST['name'];
            $content = $_POST['message'];
            $headers = $_POST['email'];

			if(mail($to, $title, $content, $headers)){
				echo "メールを送信しました";
			} else {
				echo "メールの送信に失敗しました";
			}
		?>
    </body>
</html>