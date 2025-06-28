import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)       # Use Broadcom GPIO numbering

BUTTON_PIN = 15
GPIO.setup(BUTTON_PIN, GPIO.IN)

try:
    while True:
        state = GPIO.input(BUTTON_PIN)
        print(f"Button State: {state}")  # 0 = pressed if using pull-down, 1 = released
        time.sleep(0.1)

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
