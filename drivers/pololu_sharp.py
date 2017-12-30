import RPi.GPIO as GPIO

io_initialized = False


def io_init():
    global io_initialized
    if io_initialized:
        return

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(27, GPIO.IN)
    GPIO.setup(22, GPIO.IN)
    GPIO.setup(23, GPIO.IN)
    GPIO.setup(24, GPIO.IN)
    GPIO.setup(25, GPIO.IN)

    io_initialized = True


class Whisker(object):
    def __init__(self, pin):
        self.pin = pin

    def read(self):
        return GPIO.input(self.pin)


class Whiskers(object):
    def __init__(self):
        io_init()
        self.whisker1 = Whisker(27)
        self.whisker2 = Whisker(22)
        self.whisker3 = Whisker(23)
        self.whisker4 = Whisker(24)
        self.whisker5 = Whisker(25)

    def read(self):
        return [self.whisker1.read(),
                self.whisker2.read(),
                self.whisker3.read(),
                self.whisker4.read(),
                self.whisker5.read()]


whiskers = Whiskers()
