import RPi.GPIO as GPIO
import time

# GPIO pin 16 (physical pin 36 on Pi Zero 2 W header)
LED_PIN = 16
BUTTON_PIN = 15

GPIO.setmode(GPIO.BCM)       # Use Broadcom GPIO numbering
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Button with pull-up resistor

try:
    while True:
        state = GPIO.input(BUTTON_PIN)

        print(f"Button State: {state}")
        if state == GPIO.LOW:
            GPIO.output(LED_PIN, GPIO.HIGH)  # LED ON when button is pressed
        else:
            GPIO.output(LED_PIN, GPIO.LOW)   # LED OFF
        time.sleep(0.1)



except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
