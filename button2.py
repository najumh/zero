from gpiozero import LED, Button
from signal import pause

# Define the LED and Button using BCM pin numbers
led = LED(16)              # GPIO 16 (physical pin 36)
button = Button(15, pull_up=True)  # GPIO 15 (physical pin 10), internal pull-up

# Turn LED ON when button is pressed
button.when_pressed = led.on

# Turn LED OFF when button is released
button.when_released = led.off

# Keep the script running to listen for events
pause()
