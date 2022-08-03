import math
import time
import colours


class BaseMode:
    def __init__(self):
        self.R = 0
        self.G = 0
        self.B = 0

    def set_pins(self, rgb):
        self.R = rgb.R
        self.G = rgb.G
        self.B = rgb.B


class BaseColourMode(BaseMode):
    def __init__(self):
        super().__init__()
        self.Colour_Primary = colours.index["Off"]

    def set_colour(self, colour):
        self.Colour_Primary = colours.index[colour]


class BasePairMode(BaseColourMode):
    def __init__(self):
        super().__init__()
        self.Colour_Secondary = colours.index["Off"]

    def set_alt_colour(self, alt_colour):
        self.Colour_Secondary = colours.index[alt_colour]


class BaseTimeMode(BaseMode):
    def __init__(self, period_ms):
        print("Running Base Time Constructor")
        super().__init__()
        self.Period_ms = period_ms
        self.Old_Time_ms = None
        self.Start_Time_ms = time.ticks_ms()
        self.New_Time_ms = self.Start_Time_ms
        self.Period_Phase_ms = None
        self.Phase = None
        self.Phase_Degrees = None
        self.Phase_Rads = None

    def set_period_ms(self, period_ms):
        self.Period_ms = period_ms

    def update_time(self):
        print("Updating Time")
        self.Old_Time_ms = self.New_Time_ms
        self.New_Time_ms = time.ticks_ms()
        self.Period_Phase_ms = time.ticks_diff(self.Start_Time_ms, self.New_Time_ms) % self.Period_ms
        print("Calculated Period Phase Differential")
        self.Phase = self.Period_Phase_ms / self.Period_ms
        self.Phase_Degrees = self.Phase * 360
        self.Phase_Rads = self.Phase * 2 * math.pi


# SolidMode inherits only from BaseMode as it does not vary by time
class SolidMode(BaseColourMode):
    def __init__(self):
        super().__init__()

    def update(self):
        self.set_pins(self.Colour_Primary)


# FadeMode inherits from BaseColourMode and BaseTimeMode
class FadeMode(BaseColourMode, BaseTimeMode):
    def __init__(self, period_ms):
        super().__init__(period_ms=period_ms)

    def fade(self, col):
        return abs(math.sin(self.Phase_Rads)) * col

    def update(self):
        self.update_time()
        print("Updated Time")
        self.R = self.fade(self.Colour_Primary.R)
        self.G = self.fade(self.Colour_Primary.G)
        self.B = self.fade(self.Colour_Primary.B)
        pass


# PairFadeMode inherits from BasePairMode and BaseTimeMode
class PairFadeMode(BasePairMode, BaseTimeMode):
    def __init__(self):
        super().__init__()

    def update(self):
        pass


# RainbowMode inherits from only BaseTimeMode as no colour is selected
class RainbowMode(BaseTimeMode):
    def __init__(self):
        super().__init__(10000)

    def update(self):
        pass


modes = {
    "Solid": SolidMode(),
    "Fade": FadeMode(5000),
    "Pair Fade": PairFadeMode(),
    "Rainbow": RainbowMode()
}
