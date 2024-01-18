# PI_IP = '172.20.10.5' # iPhoneテザリング 0
# PI_IP = '127.0.0.1' # localhost
# PI_IP = '157.82.200.199' # IST members
# PI_IP = '10.42.0.59' # LAN直通
PI_IP = '192.168.11.248' # iPhoneテザリング 1
PI_PORT_SOCKET = 12345

# パソコンの内蔵カメラをつかってテストするモード
INCAM = False
# Flaskのデバッグモード
# モーターの絶対角度指定など
DEBUG_FLASK = False

ANGLE_COEFF = 2 # カメラの移動速度に影響
MIN_ANGLE_X = 30
MAX_ANGLE_X = 210 # ~210
MIN_ANGLE_Y = 45
MAX_ANGLE_Y = 150 # ~120

NUM_ROCKETS = 8