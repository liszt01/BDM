from config import NUM_ROCKETS
from signal_dispatcher import send_signal

launchable_rockets = [True] * NUM_ROCKETS
ammo = {
    'totalAmmo': NUM_ROCKETS,
    'remainingAmmo': NUM_ROCKETS,
}

def launch_rockets():
    global launchable_rockets, ammo
    for i in range(NUM_ROCKETS):
        if launchable_rockets[i]:
            send_signal('ROCKET', i)
            launchable_rockets[i] = False
            break
    ammo['remainingAmmo'] = launchable_rockets.count(True)
    return ammo

def reload():
    global launchable_rockets, ammo
    launchable_rockets = [True] * NUM_ROCKETS
    ammo['remainingAmmo'] = NUM_ROCKETS
    return ammo
