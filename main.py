import time as t

class RGB:
    def __init__(self, name, r, g, b):
        self.Name = name
        self.R = r
        self.G = g
        self.B = b


colours = {
    "Off": RGB("Off", 0, 0, 0),
    "White": RGB("White", 255, 255, 255),
    "Light Gray": RGB("Light Gray", 224, 224, 224),
    "Gray": RGB("Gray", 128, 128, 128),
    "Dark Gray": RGB("Dark Gray", 64, 64, 64),
    "Red": RGB("Red", 255, 0, 0),
    "Pink": RGB("Pink", 255, 96, 208),
    "Purple": RGB("Purple", 160, 32, 255),
    "Light Blue": RGB("Light Blue", 80, 208, 255),
    "Blue": RGB("Blue", 0, 32, 255),
    "Yellow-Green": RGB("Yellow-Green", 96, 255, 128),
    "Green": RGB("Green", 0, 192, 0),
    "Yellow": RGB("Yellow", 255, 224, 32),
    "Orange": RGB("Orange", 255, 160, 16),
    "Brown": RGB("Brown", 160, 128, 96),
    "Pale Pink": RGB("Pale Pink", 255, 208, 160)
}


class BaseMode:
    def __init__(self):
        self.R = 0
        self.G = 0
        self.B = 0

    def set_pins(self, r, g, b):
        self.R = r
        self.G = g
        self.B = b


class BaseColourMode(BaseMode):
    def __init__(self):
        super().__init__()
        self.Colour_Primary = colours["Off"]

    def set_colour(self, colour):
        self.Colour_Primary = colours[colour]


class BasePairMode(BaseColourMode):
    def __init__(self):
        super().__init__()
        self.Colour_Secondary = colours["Off"]

    def set_alt_colour(self, alt_colour):
        self.Colour_Secondary = colours[alt_colour]


class BaseTimeMode(BaseMode):
    def __init__(self):
        super().__init__()
        self.Period_ms = 0

    def set_period_ms(self, period_ms):
        self.Period_ms = period_ms


# SolidMode inherits only from BaseMode as it does not vary by time
class SolidMode(BaseColourMode):
    def __init__(self):
        super().__init__()


# FadeMode inherits from BaseColourMode and BaseTimeMode
class FadeMode(BaseColourMode, BaseTimeMode):
    def __init__(self):
        super().__init__()


# PairFadeMode inherits from BasePairMode and BaseTimeMode
class PairFadeMode(BasePairMode, BaseTimeMode):
    def __init__(self):
        super().__init__()


# RainbowMode inherits from only BaseTimeMode as no colour is selected
class RainbowMode(BaseTimeMode):
    def __init__(self):
        super().__init__()


class PyController:
    def __init__(self, pin_r, pin_g, pin_b):
        self.RGB = RGB("Pins", 0, 0, 0)
        self.PWM_Period_ms = 50
        self.Pin_R = pin_r
        self.Pin_G = pin_g
        self.Pin_B = pin_b
        self.StartTime = t.time()

    def update_pins(self, pin_r, pin_g, pin_b):
        self.RGB = RGB("Pins", pin_r, pin_g, pin_b)
