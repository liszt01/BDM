from flask import Flask, render_template, Response, redirect, url_for
from image_processing import VideoCamera
import socket

app = Flask(__name__)

# ソケットの作成
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# サーバーと接続
host = '192.168.123.249'
port = 12345
client_socket.connect((host, port))

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

def send_data(msg):
    client_socket.sendall(msg.encode())

@app.route('/launch')
def send_launch():
    send_data("LAUNCH!!")
    return redirect(url_for('index'))

@app.route('/up')
def send_up():
    send_data("UP!!")
    return redirect(url_for('index'))

@app.route('/left')
def send_left():
    send_data("LEFT!!")
    return redirect(url_for('index'))

@app.route('/right')
def send_right():
    send_data("RIGHT!!")
    return redirect(url_for('index'))

@app.route('/down')
def send_down():
    send_data("DOWN!!")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
