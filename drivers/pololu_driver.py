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

    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)

    # wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
    # wiringpi.pwmSetRange(MAX_SPEED)
    # wiringpi.pwmSetClock(2)

    GPIO.setup(5, GPIO.OUT)
    GPIO.setup(6, GPIO.OUT)

    io_initialized = True


class Motor(object):
    MAX_SPEED = _max_speed

    def __init__(self, pwm_pin, dir_pin):
        self.pwm_pin = pwm_pin
        self.dir_pin = dir_pin
        self.pwm = GPIO.PWM(self.pwm_pin, 10)
        self.pwm.start(100)

    def set_speed(self, speed):
        if speed < 0:
            speed = -speed
            dir_value = GPIO.HIGH
        else:
            dir_value = GPIO.LOW

        if speed > MAX_SPEED:
            speed = MAX_SPEED

        io_init()
        GPIO.output(self.dir_pin, dir_value)


class Motors(object):
    MAX_SPEED = _max_speed

    def __init__(self):
        self.motor1 = Motor(12, 5)
        self.motor2 = Motor(13, 6)

    def set_speeds(self, m1_speed, m2_speed):
        self.motor1.set_speed(m1_speed)
        self.motor2.set_speed(m2_speed)


motors = Motors()
