# Webサーバを立ち上げる際に実行するファイル
from src.app import app

if __name__ == "__main__":
    #app.run()
    app.run(debug=False, host='localhost', port=8828, threaded=True)
