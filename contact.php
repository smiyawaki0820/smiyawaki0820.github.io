<!DOCTYPE html>
<html lang="ja">
    <head>
        <meta charset="utf-8">
        <title>mail Miyawaki</title>
    </head>
    <body>
        <?php
			mb_language("Japanese");
			mb_internal_encoding("UTF-8");

			$to = "lab.skow.mywk@gmail.com";
			$title = $_POST['name'];
            $content = $_POST['message'];
            $headers = $_POST['email'];

			if(mb_send_mail($to, $title, $content, $headers)){
				echo "メールを送信しました";
			} else {
				echo "メールの送信に失敗しました";
			}
		?>
    </body>
</html>