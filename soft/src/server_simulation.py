import socket

host = '127.0.0.1'  # 受信側のIPアドレス
port = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()

    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        data = conn.recv(1024)
        print('Received data:', data.decode())