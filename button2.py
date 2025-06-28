import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)       # Use Broadcom GPIO numbering
LED_PIN = 16  # GPIO pin 16 (physical pin 36 on Pi Zero 2 W header)
BUTTON_PIN = 15
GPIO.setup(BUTTON_PIN, GPIO.IN)
GPIO
try:
    while True:
        state = GPIO.input(BUTTON_PIN)
        GPIO.output(LED_PIN, state)  # LED ON when button is pressed
        print(f"Button State: {state}")  # 0 = pressed if using pull-down, 1 = released
        time.sleep(0.1)

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
