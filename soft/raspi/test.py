import json
# import pigpio
import signal
import socket
import subprocess
import sys
import threading
import time

PI_IP = '127.0.0.1'
PI_PORT_SOCKET = 12345
# STREAM_SCRIPT = 'start_stream.sh'

BUFSIZE = 1024
MAX_CONN = 5

# motor
mX = 26
mY = 19

# nichrome
nc = [13, 6, 5, 0, 21, 20, 16, 12]

def pulse(degree):
    return 500 + 2000 * degree / 270

# def set_motor(direction, degree):
#     if (direction == 'X'):
#         pi.set_servo_pulsewidth(mX, pulse(degree))
#     elif (direction == 'Y'):
#         pi.set_servo_pulsewidth(mY, pulse(degree))

# def ignition(index):
#     with lock:
#         pi.write(nc[index], 1)
#         time.sleep(3)
#         pi.write(nc[index], 0)
#         time.sleep(1)

# シグナルハンドラ関数
def signal_handler(sig, frame):
    print('プログラムを終了します')
    server.close()
    # for pin in nc:
    #     pi.write(pin, 0)
    # GPIOピンを解放
    # pi.stop()
    # pigpiod を停止
    # subprocess.run(['sudo', 'pkill', 'pigpiod'])
    # ストリーム配信を停止
    # process_stream.terminate()
    sys.exit(0)

# SIGINT（Ctrl+C）に対するハンドラを設定
signal.signal(signal.SIGINT, signal_handler)

# ストリーム配信を開始
# process_stream = subprocess.Popen(['bash', STREAM_SCRIPT])
# pigpiod を起動する
# subprocess.run(['sudo', 'pigpiod'])

# pi = pigpio.pi()
# pi.set_mode(mX, pigpio.OUTPUT)
# pi.set_mode(mY, pigpio.OUTPUT)
# for pin in nc:
#     pi.set_mode(pin, pigpio.OUTPUT)

lock = threading.Lock()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((PI_IP, PI_PORT_SOCKET))
server.listen(MAX_CONN)
print('[*] listen {}:{}'.format(PI_IP, PI_PORT_SOCKET))

def handle_client(client_socket):
    request = client_socket.recv(BUFSIZE)
    print('[*] recv: {}'.format(request.decode()))
    data = json.loads(request.decode())
    # if data['device'] == 'MOTOR':
    #     set_motor(data['direction'], int(data['angle']))
    # elif data['device'] == 'ROCKET':
    #     ignition(data['index'])
    client_socket.close()

while True:
    client,addr = server.accept()
    print('[*] connected from: {}:{}'.format(addr[0], addr[1]))
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()
