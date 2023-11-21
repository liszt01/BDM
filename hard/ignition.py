import pigpio
import time


def main():
    i1 = 14
    i2 = 23

    pi = pigpio.pi()
    pi.set_mode(i1, pigpio.OUTPUT)
    pi.set_mode(i2, pigpio.OUTPUT)

    pi.write(i1, 1)
    time.sleep(3)
    pi.write(i1, 0)
    time.sleep(1)


if __name__ == "__main__":
    main()
