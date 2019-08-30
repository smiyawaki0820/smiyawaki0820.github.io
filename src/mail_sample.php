<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
  </head>
  <body>
    <?php
      mb_language("Japanese");
      mb_internal_encoding("UTF-8");
      $to = "skow.kitten@icloud.com";
      $title = $_POST['name'];
      $content = $_POST['mail-subject'];
      mb_send_mail($to, $title, $content)
    ?>
  </body>
</html>