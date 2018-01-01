import RPi.GPIO as GPIO

io_initialized = False

W1 = 10
W2 = 9
W3 = 11
W4 = 8
W5 = 7


def io_init():
    global io_initialized
    if io_initialized:
        return

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(W1, GPIO.IN)
    GPIO.setup(W2, GPIO.IN)
    GPIO.setup(W3, GPIO.IN)
    GPIO.setup(W4, GPIO.IN)
    GPIO.setup(W5, GPIO.IN)

    io_initialized = True


class Whisker(object):
    def __init__(self, pin):
        self.pin = pin

    def read(self):
        return GPIO.input(self.pin)


class Whiskers(object):
    def __init__(self):
        io_init()
        self.whisker1 = Whisker(W1)
        self.whisker2 = Whisker(W2)
        self.whisker3 = Whisker(W3)
        self.whisker4 = Whisker(W4)
        self.whisker5 = Whisker(W5)

    def read(self):
        return [self.whisker1.read(),
                self.whisker2.read(),
                self.whisker3.read(),
                self.whisker4.read(),
                self.whisker5.read()]


whiskers = Whiskers()
