import pigpio
import time

# motor
mX = 26
mY = 19

# nichrome
i0 = 13
i1 = 6
i2 = 5
i3 = 0
i4 = 21
i5 = 20
i6 = 16
i7 = 12

pi = pigpio.pi()
pi.set_mode(mX, pigpio.OUTPUT)
pi.set_mode(mY, pigpio.OUTPUT)
pi.set_mode(i0, pigpio.OUTPUT)
pi.set_mode(i1, pigpio.OUTPUT)
pi.set_mode(i2, pigpio.OUTPUT)
pi.set_mode(i3, pigpio.OUTPUT)
pi.set_mode(i4, pigpio.OUTPUT)
pi.set_mode(i5, pigpio.OUTPUT)
pi.set_mode(i6, pigpio.OUTPUT)
pi.set_mode(i7, pigpio.OUTPUT)

def test():
    while True:  # 30~210degを使う
        for i in range(0, 20):
            pi.set_servo_pulsewidth(m1, pulse(80 + i))
            time.sleep(0.02)
        for i in range(20, 0, -1):
            pi.set_servo_pulsewidth(m1, pulse(80 + i))
            time.sleep(0.02)

def set_motor(direction, degree):
    if (direction == 'X'):
        pi.set_servo_pulsewidth(m1, pulse(degree))
    elif (direction == 'Y'):
        pi.set_servo_pulsewidth(m2, pulse(degree))


def pulse(degree):
    return 500 + 2000 * degree / 270


def ignition(index):
    i1 = 14
    i2 = 23

    pi = pigpio.pi()
    pi.set_mode(i1, pigpio.OUTPUT)
    pi.set_mode(i2, pigpio.OUTPUT)

    pi.write(i1, 1)
    time.sleep(3)
    pi.write(i1, 0)
    time.sleep(1)