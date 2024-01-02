import socket
import pigpio
import time


m1 = 26
pi = pigpio.pi()
pi.set_mode(m1, pigpio.OUTPUT)

def test():
    while True:  # 30~210degを使う
        for i in range(0, 20):
            pi.set_servo_pulsewidth(m1, pulse(80 + i))
            time.sleep(0.02)
        for i in range(20, 0, -1):
            pi.set_servo_pulsewidth(m1, pulse(80 + i))
            time.sleep(0.02)

def set_motor(degree):
    pi.set_servo_pulsewidth(m1, pulse(degree))


def pulse(degree):
    return 500 + 2000 * degree / 270

host = '192.168.123.249'  # 受信側のIPアドレス
port = 12345

print('Program start')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()

    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                print('Connection closed by', addr)
                break
            print('Received data:', data.decode())

            if data.decode() == "LAUNCH!!":
                # test()
                set_motor(60)