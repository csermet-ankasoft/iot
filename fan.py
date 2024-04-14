import RPi.GPIO as GPIO
import time

# Constants
ENA_PIN = 16  # GPIO pin connected to the EN1 pin L298N
IN1_PIN = 20  # GPIO pin connected to the IN1 pin L298N
IN2_PIN = 21  # GPIO pin connected to the IN2 pin L298N

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(ENA_PIN, GPIO.OUT)
GPIO.setup(IN1_PIN, GPIO.OUT)
GPIO.setup(IN2_PIN, GPIO.OUT)

# Create PWM object
pwm = GPIO.PWM(ENA_PIN, 50)  # 100 Hz frequency

# Main loop
try:
    while True:
        # Motor A spins clockwise
        GPIO.output(IN1_PIN, GPIO.HIGH)
        GPIO.output(IN2_PIN, GPIO.LOW)
        print("start")

        # Increase speed gradually
        for speed in range(0, 151):
            pwm.ChangeDutyCycle(speed)
            time.sleep(0.01)
            print(speed)

        time.sleep(1)  # Rotate at maximum speed for 1 second in clockwise direction

        # Change direction to anti-clockwise
        GPIO.output(IN1_PIN, GPIO.LOW)
        GPIO.output(IN2_PIN, GPIO.HIGH)

        time.sleep(1)  # Rotate at maximum speed for 1 second in anti-clockwise direction

        # Decrease speed gradually
        for speed in range(100, -1, -1):
            pwm.ChangeDutyCycle(speed)
            time.sleep(0.01)

        time.sleep(1)  # Stop motor for 1 second

except KeyboardInterrupt:
    pass

finally:
    # Stop PWM and cleanup GPIO on program exit
    pwm.stop()
    GPIO.cleanup()