import RPi.GPIO as GPIO

io_initialized = False

M1_SF = 5
M1_PWM = 12
M2_SF = 6
M2_PWM = 13


def io_init():
    global io_initialized
    if io_initialized:
        return

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(M1_SF, GPIO.OUT)
    GPIO.setup(M2_SF, GPIO.OUT)

    GPIO.setup(M1_PWM, GPIO.OUT)
    GPIO.setup(M2_PWM, GPIO.OUT)

    io_initialized = True


class Motor(object):
    def __init__(self, pwm_pin, dir_pin):
        self.dir_pin = dir_pin
        self.pwm = GPIO.PWM(pwm_pin, 10)
        self.pwm.start(0)

    def set_speed(self, speed):
        if speed < 0:
            dir_value = GPIO.HIGH
        else:
            dir_value = GPIO.LOW
        GPIO.output(self.dir_pin, dir_value)
        self.pwm.ChangeDutyCycle(abs(speed))


class Motors(object):
    def __init__(self):
        io_init()
        self.motor1 = Motor(M1_PWM, M1_SF)
        self.motor2 = Motor(M2_PWM, M2_SF)

    def set_speeds(self, m1_speed, m2_speed):
        self.motor1.set_speed(m1_speed)
        self.motor2.set_speed(m2_speed)


motors = Motors()
