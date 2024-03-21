import RPi.GPIO as GPIO
import time
import pygame

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Define GPIO pin connected to the fabric sensor
sensor_pin = 17

# Set up GPIO pin as input with pull-up resistor enabled
GPIO.setup(sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initialize Pygame for audio playback
pygame.init()

# Load the sound file
pop = pygame.mixer.Sound("/home/zishanpi/gpio-music-box/samples/pop.wav")

try:
    while True:
        # Read sensor state (pressed or not)
        sensor_state = GPIO.input(sensor_pin)
        
        # Check if the sensor is pressed
        if sensor_state == GPIO.LOW:
            print("Sensor pressed")
            # Play the sound
            pop.play()
        else:
            print("Sensor not pressed")

        # Optional: Add a delay between readings to prevent CPU usage
        time.sleep(0.1)

except KeyboardInterrupt:
    # Clean up GPIO resources on Ctrl+C
    GPIO.cleanup()
