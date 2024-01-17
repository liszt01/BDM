import pigpio
import time


def main():
    pin = [14, 15, 18, 23, 19, 26]

    pi = pigpio.pi()
    for i in range(5):
        pi.set_mode(pin[i], pigpio.OUTPUT)

    for i in range(5):
        pi.write(pin[i], 0)


if __name__ == "__main__":
    main()
