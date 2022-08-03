from machine import PWM, Pin
import time
import rgb


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
        self.PWM_R.freq(1000)
        self.PWM_G.freq(1000)
        self.PWM_B.freq(1000)
        # Set Initial PWM Duty Cycles
        self.PWM_R.duty_u16(20000)
        self.PWM_G.duty_u16(40000)
        self.PWM_B.duty_u16(60000)

    def update_pins(self, rgb_pins):
        self.PWM_R.duty_u16(256*(rgb_pins.R+1))
        self.PWM_G.duty_u16(256*(rgb_pins.G+1))
        self.PWM_B.duty_u16(256*(rgb_pins.B+1))


LED = PyController(0, 1, 2)


while True:
    LED.update_pins(rgb.colours["Red"])
    time.sleep_ms(1000)
    LED.update_pins(rgb.colours["Green"])
    time.sleep_ms(1000)
    LED.update_pins(rgb.colours["Blue"])
    time.sleep_ms(1000)
