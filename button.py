import RPi.GPIO as GPIO
import time

# GPIO pin 16 (physical pin 36 on Pi Zero 2 W header)
LED_PIN = 16

GPIO.setmode(GPIO.BCM)       # Use Broadcom GPIO numbering
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)  # LED ON
        time.sleep(2)

        GPIO.output(LED_PIN, GPIO.LOW)   # LED OFF
        time.sleep(2)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
