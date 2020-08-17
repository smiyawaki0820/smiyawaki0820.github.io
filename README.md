# Directory Tree
```
app/
|- templates/
|  |- index.html
|- static/
|- app.py
models/
|- __init__.py
|- models.py
|- database.py
run.py
```


# app/

## templates
- HTMLファイルを格納する場所

## static
- HTMLファイル以外の、CSSファイル・JSファイル・画像ファイル等を格納する場所

## app.py
- アプリロジックを書くファイル
- リクエストされたURLに応じてどのHTMLファイルを返すかを指定します



# models/

- SQLiteをセットアップする
- http://www.kzfmix.com/flaski/second.html

## models.py
- テーブルのカラム情報を定義するためのクラスを格納します。
- テーブル操作を行う際のレコード生成もこのクラスを通して行います。
- 今回は神社に対しての「お願い」を格納するためのテーブルを作成したいと思います。
- カラム構成は
```
* ID（int：キー情報）
* title（String(128)：お願いのタイトル）
* body（text：お願いの内容）
* date（datetime：お願いの投稿日時）
```


