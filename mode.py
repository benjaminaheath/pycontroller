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

    def update(self):
        pass


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
        super().__init__()
        self.Period_ms = period_ms
        self.Prev_Time_ms = None
        self.Present_Time_ms = time.ticks_ms()
        self.Diff_ms = None

    def set_period_ms(self, period_ms):
        self.Period_ms = period_ms

    def update_time(self):
        self.Prev_Time_ms = self.Present_Time_ms
        self.Prev_Time_ms = time.ticks_ms()


# SolidMode inherits only from BaseMode as it does not vary by time
class SolidMode(BaseColourMode):
    def __init__(self):
        super().__init__()

    def update(self):
        super().set_pins(super().Colour_Primary)
        pass


# FadeMode inherits from BaseColourMode and BaseTimeMode
class FadeMode(BaseColourMode, BaseTimeMode):
    def __init__(self):
        super().__init__()

    def update(self):
        super(BaseTimeMode).update_time()
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
    "Fade": FadeMode(),
    "Pair Fade": PairFadeMode(),
    "Rainbow": RainbowMode()
}
