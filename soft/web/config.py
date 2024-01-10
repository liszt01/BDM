PI_IP = '192.168.123.249'
PI_PORT_SOCKET = 12345

# パソコンの内蔵カメラをつかってテストするモード
INCAM = False
# Flaskのデバッグモード
# モーターの絶対角度指定など
DEBUG_FLASK = True

ANGLE_COEFF = 2 # カメラの移動速度に影響
MIN_ANGLE_X = 30
MAX_ANGLE_X = 210 # ~210
MIN_ANGLE_Y = 30
MAX_ANGLE_Y = 150 # ~120

NUM_ROCKETS = 8