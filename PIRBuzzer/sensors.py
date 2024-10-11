import RPi.GPIO as GPIO
import time

PIR_pin = 23
Buzzer_pin = 24

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_pin, GPIO.IN)
GPIO.setup(Buzzer_pin, GPIO.OUT)

def main():
    motion_detection()


def beep(repeat):
    for i in range(0, repeat):
        for pulse in range(60):
            GPIO.output(Buzzer_pin, True)
            time.sleep(0.001)
            GPIO.output(Buzzer_pin, False)
            time.sleep(0.001)
        time.sleep(0.02)


def motion_detection():
    while True:
        if GPIO.input(PIR_pin):
            print("Motion detected")
            beep(4)
        time.sleep(1)



if __name__ == "__main__":
    main()


