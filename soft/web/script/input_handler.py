from config import ANGLE_COEFF, MIN_ANGLE_X, MAX_ANGLE_X, MIN_ANGLE_Y, MAX_ANGLE_Y, NUM_ROCKETS
from script.command_sender import send_command

angle_x = 120
angle_y = 30

launchable_rockets = [True] * NUM_ROCKETS
ammo = {
    'totalAmmo': NUM_ROCKETS,
    'remainingAmmo': NUM_ROCKETS,
}

def enforce_angle_constraints():
    global angle_x, angle_y
    angle_x = min(MAX_ANGLE_X, max(MIN_ANGLE_X, angle_x))
    angle_y = min(MAX_ANGLE_Y, max(MIN_ANGLE_Y, angle_y))

def move_motor_relative(dx, dy):
    global angle_x, angle_y
    angle_x += ANGLE_COEFF * (-dx)
    angle_y += ANGLE_COEFF * dy
    enforce_angle_constraints()

    send_command('MOTOR', 'X', angle_x)
    send_command('MOTOR', 'Y', angle_y)

def set_absolute_angle(x, y):
    global angle_x, angle_y
    angle_x = x
    angle_y = y
    enforce_angle_constraints()

    send_command('MOTOR', 'X', angle_x)
    send_command('MOTOR', 'Y', angle_y)

def launch_rocket():
    global launchable_rockets, ammo
    for i in range(NUM_ROCKETS):
        if launchable_rockets[i]:
            send_command('ROCKET', i)
            launchable_rockets[i] = False
            break
    ammo['remainingAmmo'] = launchable_rockets.count(True)
    return ammo

def reload():
    global launchable_rockets, ammo
    launchable_rockets = [True] * NUM_ROCKETS
    ammo['remainingAmmo'] = NUM_ROCKETS
    return ammo