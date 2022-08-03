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
