PI_IP = '127.0.0.1'
PI_PORT_SOCKET = 12345
PI_PORT_STREAM = 8080

# Webカメラを使わずにテストするモード
NO_CAMERA = False
# Flaskのデバッグモード
# モーターの絶対角度指定など
DEBUG_FLASK = True

ANGLE_COEFF = 5 # もっとちいさくても良さそう
MIN_ANGLE_X = 30
MAX_ANGLE_X = 120 # ~210
MIN_ANGLE_Y = 30
MAX_ANGLE_Y = 120

NUM_ROCKETS = 8