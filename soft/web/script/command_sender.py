import json
import socket
from config import PI_IP, PI_PORT_SOCKET

def send_command(*args):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((PI_IP, PI_PORT_SOCKET))
        
        data = None
        if args[0] == 'MOTOR':
            data = {
                'device': args[0],
                'direction': args[1],
                'angle': args[2],
            }
        elif args[0] == 'ROCKET':
            data = {
                'device': args[0],
                'index': args[1],
            }
        else:
            print('send_signal: Invalid arguments')
            return

        msg = json.dumps(data)
        client.sendall(msg.encode())
