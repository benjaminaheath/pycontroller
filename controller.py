from machine import PWM, Pin
import mode
import time

class PyController:

    def __init__(self, pin_r, pin_g, pin_b):
        # Configure Pins as Pin Objects
        self.Pin_R = Pin(pin_r)
        self.Pin_G = Pin(pin_g)
        self.Pin_B = Pin(pin_b)
        # Configure Pin Objects as PWM

        self.PWM_R = PWM(self.Pin_R)
        self.PWM_G = PWM(self.Pin_G)
        self.PWM_B = PWM(self.Pin_B)
        # Configure PWM Parameters
        self.PWM_R.freq(100000)
        self.PWM_G.freq(100000)
        self.PWM_B.freq(100000)

        # Default Mode as Solid, Off
        self.mode = mode.modes["Rainbow"]
        self.mode.set_period_ms(10000)

    def update(self):
        self.mode.update()
        self.PWM_R.duty_u16(256*(self.mode.R+1))
        self.PWM_G.duty_u16(256*(self.mode.G+1))
        self.PWM_B.duty_u16(256*(self.mode.B+1))

    def update_rgb(self, rgb_pins):
        self.PWM_R.duty_u16(256*(rgb_pins.R+1))
        self.PWM_G.duty_u16(256*(rgb_pins.G+1))
        self.PWM_B.duty_u16(256*(rgb_pins.B+1))

    def thread(self):
        while True:
            self.update()
            time.sleep_ms(10)