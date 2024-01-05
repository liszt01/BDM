from signal_dispatcher import send_signal
from config import ANGLE_COEFF, MIN_ANGLE_X, MAX_ANGLE_X, MIN_ANGLE_Y, MAX_ANGLE_Y

angle_x = 120
angle_y = 30

def enforce_angle_constraints():
    global angle_x, angle_y
    angle_x = min(MAX_ANGLE_X, max(MIN_ANGLE_X, angle_x))
    angle_y = min(MAX_ANGLE_Y, max(MIN_ANGLE_Y, angle_y))

def move_motor_relative(dx, dy):
    global angle_x, angle_y
    angle_x += ANGLE_COEFF * dx
    angle_y += ANGLE_COEFF * (-dy)
    enforce_angle_constraints()

    send_signal('MOTOR', 'X', angle_x)
    send_signal('MOTOR', 'Y', angle_y)

def set_absolute_angle(x, y):
    global angle_x, angle_y
    angle_x = x
    angle_y = y
    enforce_angle_constraints()

    send_signal('MOTOR', 'X', angle_x)
    send_signal('MOTOR', 'Y', angle_y)