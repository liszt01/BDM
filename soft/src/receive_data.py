import socket
import signal
import sys
from config import PI_IP, PI_PORT_SOCKET

BUFSIZE = 1024

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
# m1 = 26
# pi = pigpio.pi()
# pi.set_mode(m1, pigpio.OUTPUT)

# def test():
#     while True:  # 30~210degを使う
#         for i in range(0, 20):
#             pi.set_servo_pulsewidth(m1, pulse(80 + i))
#             time.sleep(0.02)
#         for i in range(20, 0, -1):
#             pi.set_servo_pulsewidth(m1, pulse(80 + i))
#             time.sleep(0.02)

# def set_motor(degree):
#     pi.set_servo_pulsewidth(m1, pulse(degree))


# def pulse(degree):
#     return 500 + 2000 * degree / 270


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((PI_IP, PI_PORT_SOCKET))
server.listen()
print('[*] listen {}:{}'.format(PI_IP, PI_PORT_SOCKET))

while True:
    client, addr = server.accept()
    with client:
        print('[*] connected from: {}:{}'.format(addr[0], addr[1]))
        request = client.recv(BUFSIZE)
        print('[*] recv: {}'.format(request.decode()))

        # if request.decode() == "LAUNCH!!":
            # test()
            # set_motor(60)