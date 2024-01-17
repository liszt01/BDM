import pigpio
import time


def main():
    pin = [14, 15, 18, 23]

    pi = pigpio.pi()
    for i in range(4):
        pi.set_mode(pin[i], pigpio.OUTPUT)

    # while True:
    #     for i in range(2):
    #         pi.write(pin[i], 1)
    #         time.sleep(3)
    #         pi.write(pin[i], 0)

    i = 0
    pi.write(pin[i], 1)
    time.sleep(2)
    pi.write(pin[i], 0)


if __name__ == "__main__":
    main()
