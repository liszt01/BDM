import socket
import signal
import sys
import threading
from config import PI_IP, PI_PORT_SOCKET

BUFSIZE = 1024
MAX_CONN = 10

# シグナルハンドラ関数
def signal_handler(sig, frame):
    print('プログラムを終了します')
    # できれば client socket も閉じるようにしたい
    server.close()
    sys.exit(0)

# SIGINT（Ctrl+C）に対するハンドラを設定
signal.signal(signal.SIGINT, signal_handler)

# import pigpio
# import time
# import json
# m1 = 26 # X
# m2 = 19 # Y
# pi = pigpio.pi()
# pi.set_mode(m1, pigpio.OUTPUT)
# pi.set_mode(m2, pigpio.OUTPUT)

# def test():
#     while True:  # 30~210degを使う
#         for i in range(0, 20):
#             pi.set_servo_pulsewidth(m1, pulse(80 + i))
#             time.sleep(0.02)
#         for i in range(20, 0, -1):
#             pi.set_servo_pulsewidth(m1, pulse(80 + i))
#             time.sleep(0.02)

# def set_motor(direction, degree):
#     if (direction == 'X'):
#         pi.set_servo_pulsewidth(m1, pulse(degree))
#     elif (direction == 'Y'):
#         pi.set_servo_pulsewidth(m2, pulse(degree))


# def pulse(degree):
#     return 500 + 2000 * degree / 270


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((PI_IP, PI_PORT_SOCKET))
server.listen(MAX_CONN)
print('[*] listen {}:{}'.format(PI_IP, PI_PORT_SOCKET))

def handle_client(client_socket):
    request = client_socket.recv(BUFSIZE)
    print('[*] recv: {}'.format(request.decode()))
    # data = json.loads(request.decode())
    # if data['device'] == 'MOTOR':
    #     print(data['direction'], data['angle'])
    #     set_motor(data['direction'], int(data['angle']))
    client_socket.close()

while True:
    client,addr = server.accept()
    print('[*] connected from: {}:{}'.format(addr[0], addr[1]))
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()