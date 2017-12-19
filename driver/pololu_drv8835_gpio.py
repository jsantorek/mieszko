import RPi.GPIO as GPIO

# Motor speeds for this library are specified as numbers
# between -MAX_SPEED and MAX_SPEED, inclusive.
_max_speed = 480  # 19.2 MHz / 2 / 480 = 20 kHz
MAX_SPEED = _max_speed

io_initialized = False


def io_init():
    global io_initialized
    if io_initialized:
        return

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(10, GPIO.OUT)    # wiringpi.pinMode(12, wiringpi.GPIO.PWM_OUTPUT)
    GPIO.setup(9, GPIO.OUT)     # wiringpi.pinMode(13, wiringpi.GPIO.PWM_OUTPUT)

    # wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
    # wiringpi.pwmSetRange(MAX_SPEED)
    # wiringpi.pwmSetClock(2)

    GPIO.setup(24, GPIO.OUT)    # wiringpi.pinMode(5, wiringpi.GPIO.OUTPUT)
    GPIO.setup(25, GPIO.OUT)    # wiringpi.pinMode(6, wiringpi.GPIO.OUTPUT)

    io_initialized = True


class Motor(object):
    MAX_SPEED = _max_speed

    def __init__(self, pwm_pin, dir_pin):
        self.pwm_pin = pwm_pin
        self.dir_pin = dir_pin

    def setSpeed(self, speed):
        if speed < 0:
            speed = -speed
            dir_value = GPIO.HIGH
        else:
            dir_value = GPIO.LOW

        if speed > MAX_SPEED:
            speed = MAX_SPEED

        io_init()
        GPIO.output(self.dir_pin, dir_value)   # wiringpi.digitalWrite(self.dir_pin, dir_value)
        pwm = GPIO.PWM(self.pwm_pin, speed)  # wiringpi.pwmWrite(self.pwm_pin, speed)
        pwm.start()

class Motors(object):
    MAX_SPEED = _max_speed

    def __init__(self):
        self.motor1 = Motor(10, 24)
        self.motor2 = Motor(9, 25)

    def setSpeeds(self, m1_speed, m2_speed):
        self.motor1.setSpeed(m1_speed)
        self.motor2.setSpeed(m2_speed)


motors = Motors()
