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
        if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
            GPIO.output(LED_PIN, GPIO.HIGH)  # LED ON
        else:    
            GPIO.output(LED_PIN, GPIO.LOW)   # LED OFF

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
