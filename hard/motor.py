import pigpio
import time


def main():
    m1 = 14
    m2 = 23

    pi = pigpio.pi()
    pi.set_mode(m1, pigpio.OUTPUT)
    pi.set_mode(m2, pigpio.OUTPUT)

    while True:  # 30~210degを使う
        for i in range(0, 180):
            pi.set_servo_pulsewidth(m1, pulse(30 + i))
            pi.set_servo_pulsewidth(m2, pulse(30 + i / 2))
            time.sleep(0.02)
        for i in range(180, 0, -1):
            pi.set_servo_pulsewidth(m1, pulse(30 + i))
            pi.set_servo_pulsewidth(m2, pulse(30 + i / 2))
            time.sleep(0.02)


def pulse(degree):
    return 500 + 2000 * degree / 270


if __name__ == "__main__":
    main()
