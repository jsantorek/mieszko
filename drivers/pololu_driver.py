import RPi.GPIO as GPIO

io_initialized = False

M1_PWM = 12
M1_DIR = 24
M1_EN = 22
M2_PWM = 13
M2_DIR = 25
M2_EN = 23


def io_init():
    global io_initialized
    if io_initialized:
        return

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(M1_PWM, GPIO.OUT)
    GPIO.setup(M2_PWM, GPIO.OUT)
    GPIO.setup(M1_DIR, GPIO.OUT)
    GPIO.setup(M2_DIR, GPIO.OUT)
    GPIO.setup(M1_EN, GPIO.OUT)
    GPIO.setup(M2_EN, GPIO.OUT)

    io_initialized = True


class Motor(object):
    def __init__(self, pwm_pin, dir_pin, en_pin):
        self.dir_pin = dir_pin
        self.en_pin = en_pin
        self.pwm = GPIO.PWM(pwm_pin, 10)
        self.pwm.start(0)

    def enable(self):
        GPIO.output(self.en_pin, GPIO.HIGH)

    def disable(self):
        GPIO.output(self.en_pin, GPIO.LOW)

    def set_speed(self, speed):
        if speed < 0:
            dir_value = GPIO.HIGH
            speed = abs(speed)
        else:
            dir_value = GPIO.LOW
        GPIO.output(self.dir_pin, dir_value)
        self.pwm.ChangeDutyCycle(max(0, min(speed, 100)))


class Motors(object):
    def __init__(self):
        io_init()
        self.motor1 = Motor(M1_PWM, M1_DIR, M1_EN)
        self.motor2 = Motor(M2_PWM, M2_DIR, M2_EN)

    def enable(self):
        self.motor1.enable()
        self.motor2.enable()

    def disable(self):
        self.motor1.disable()
        self.motor2.disable()

    def set_speeds(self, m1_speed, m2_speed):
        self.motor1.set_speed(m1_speed)
        self.motor2.set_speed(m2_speed)


motors = Motors()
