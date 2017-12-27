import RPi.GPIO as GPIO

# Motor speeds for this library are specified as numbers
# between -MAX_SPEED and MAX_SPEED, inclusive.
# _max_speed = 480  # 19.2 MHz / 2 / 480 = 20 kHz
_max_speed = 480
MAX_SPEED = _max_speed

io_initialized = False


def io_init():
    global io_initialized
    if io_initialized:
        return

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)

    GPIO.setup(5, GPIO.OUT)
    GPIO.setup(6, GPIO.OUT)

    io_initialized = True


class Motor(object):
    MAX_SPEED = _max_speed

    def __init__(self, pwm_pin, dir_pin):
        io_init()
        self.dir_pin = dir_pin
        self.pwm = GPIO.PWM(pwm_pin, 1)

    def set_speed(self, speed):
        if speed < 0:
            speed = -speed
            dir_value = GPIO.HIGH
        else:
            dir_value = GPIO.LOW
        if speed > MAX_SPEED:
            speed = MAX_SPEED

        GPIO.output(self.dir_pin, dir_value)
        if speed > 0:
            self.pwm.ChangeFrequency(speed)
            self.pwm.start(100)
        else:
            self.pwm.stop()


class Motors(object):
    MAX_SPEED = _max_speed

    def __init__(self):
        self.motor1 = Motor(12, 5)
        self.motor2 = Motor(13, 6)

    def set_speeds(self, m1_speed, m2_speed):
        self.motor1.set_speed(m1_speed)
        self.motor2.set_speed(m2_speed)


motors = Motors()
