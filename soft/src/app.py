from flask import Flask, render_template, Response
from image_processing import VideoCamera
import socket

app = Flask(__name__)

# ソケットの作成
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ソケットを接続
host = '127.0.0.1'
port = 12345
# client_socket.connect((host, port))

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# returnではなくジェネレーターのyieldで逐次出力。
# Generatorとして働くためにgenとの関数名にしている
# Content-Type（送り返すファイルの種類として）multipart/x-mixed-replace を利用。
# HTTP応答によりサーバーが任意のタイミングで複数の文書を返し、紙芝居的にレンダリングを切り替えさせるもの。

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# launchボタンを押したときに
# localhost:8000 says send_data
# って表示されるのどうなんだろう。launchならまだしも、上下左右の移動でいちいち出てきたらうざったいな
#@app.route('/send_data')
#def send_data():
#    if client_socket:
#        data_to_send = "3 2 1 ... FIRE!!"
#        client_socket.sendall(data_to_send.encode())
#        return 'Data sent successfully'
#    else:
#        return 'Error: Socket not connected'

if __name__ == '__main__':
    app.run()
