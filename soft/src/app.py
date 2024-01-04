from flask import Flask, render_template, Response, redirect, url_for
import socket
from image_processing import VideoCamera, frame_generator
from config import PI_IP, PI_PORT_SOCKET


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(frame_generator(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def send_data(msg):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((PI_IP, PI_PORT_SOCKET))
    client.sendall(msg.encode())

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
