import pigpio
import time


def main():
    m1 = 19
    m2 = 26
    pin = [14, 15, 18, 23]

    pi = pigpio.pi()
    pi.set_mode(m1, pigpio.OUTPUT)
    pi.set_mode(m2, pigpio.OUTPUT)
    for i in range(4):
        pi.set_mode(pin[i], pigpio.OUTPUT)

    for i in range(5):  # 30~210degを使う
        for i in range(0, 90):
            pi.set_servo_pulsewidth(m1, pulse(30 + i))
            pi.set_servo_pulsewidth(m2, pulse(30 + i / 2))
            time.sleep(0.02)
        for i in range(90, 0, -1):
            pi.set_servo_pulsewidth(m1, pulse(30 + i))
            pi.set_servo_pulsewidth(m2, pulse(30 + i / 2))
            time.sleep(0.02)

        pi.write(pin[0], 1)
        time.sleep(2)
        pi.write(pin[0], 0)


def pulse(degree):
    return 500 + 2000 * degree / 270


if __name__ == "__main__":
    main()
