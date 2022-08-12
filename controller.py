from machine import PWM, Pin

import colours
import mode
import time


class PyController:
    def __init__(self, pin_r, pin_g, pin_b):
        # Initialise controller model attributes
        self.mode = mode.modes["Rainbow"]
        self.primary_colour = colours.index["Red"]
        self.secondary_colour = colours.index["Red"]
        self.period_ms = 10000
        # Updated flags for when server receives a GET request:
        # true at startup to update mode initialisation
        self.primary_colour_updated = True
        self.secondary_colour_updated = True
        self.period_ms_updated = True
        # TODO: Implement detection of model update in mode classes

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
