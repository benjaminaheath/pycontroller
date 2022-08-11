import math
import colours
import time


class BaseMode:
    def __init__(self):
        self.Name = None
        self.R = 0
        self.G = 0
        self.B = 0

    def set_pins(self, rgb):
        self.R = rgb.R
        self.G = rgb.G
        self.B = rgb.B


class BaseColourMode(BaseMode):
    def __init__(self, colour_primary):
        BaseMode.__init__(self)
        self.Colour_Primary = colour_primary

    def set_colour(self, colour):
        self.Colour_Primary = colours.index[colour]


class BasePairMode(BaseColourMode):
    def __init__(self, colour_primary, colour_secondary):
        super().__init__(colour_primary=colour_primary)
        self.Colour_Secondary = colour_secondary

    def set_alt_colour(self, alt_colour):
        self.Colour_Secondary = colours.index[alt_colour]


class BaseTimeMode(BaseMode):
    def __init__(self, period_ms):
        BaseMode.__init__(self)
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
        self.Old_Time_ms = self.New_Time_ms
        self.New_Time_ms = time.ticks_ms()
        self.Period_Phase_ms = time.ticks_diff(self.Start_Time_ms, self.New_Time_ms) % self.Period_ms
        self.Phase = self.Period_Phase_ms / self.Period_ms
        self.Phase_Degrees = self.Phase * 360
        self.Phase_Rads = self.Phase * 2 * math.pi


# SolidMode inherits only from BaseMode as it does not vary by time
class SolidMode(BaseColourMode):
    def __init__(self, colour_primary):
        super().__init__(colour_primary=colour_primary)
        self.Name="Solid"

    def update(self):
        self.set_pins(self.Colour_Primary)


# PulseMode inherits from BaseColourMode and BaseTimeMode
class PulseMode(BaseTimeMode, BaseColourMode):
    def __init__(self, period_ms, colour_primary):
        BaseTimeMode.__init__(self, period_ms=period_ms)
        BaseColourMode.__init__(self, colour_primary=colour_primary)
        self.Name = "Pulse"

    def pulse(self, col):
        return round(abs(0.5*math.sin(self.Phase_Rads)+0.5) * col)

    def update(self):
        self.update_time()
        self.R = self.pulse(self.Colour_Primary.R)
        self.G = self.pulse(self.Colour_Primary.G)
        self.B = self.pulse(self.Colour_Primary.B)


# PairFadeMode inherits from BasePairMode and BaseTimeMode
class PairFadeMode(BaseTimeMode, BasePairMode):
    def __init__(self, period_ms, colour_primary, colour_secondary):
        BaseTimeMode.__init__(self, period_ms=period_ms)
        BasePairMode.__init__(self, colour_primary=colour_primary, colour_secondary=colour_secondary)
        self.Name = "Pair Fade"

    def pair_fade(self, col1, col2):
        c1 = abs(0.5 * math.sin(self.Phase_Rads) + 0.5) * col1
        c2 = abs(0.5 * math.cos(self.Phase_Rads) + 0.5) * col2
        return round((c1+c2)/2)

    def update(self):
        self.update_time()
        self.R = self.pair_fade(self.Colour_Primary.R, self.Colour_Secondary.R)
        self.G = self.pair_fade(self.Colour_Primary.G, self.Colour_Secondary.G)
        self.B = self.pair_fade(self.Colour_Primary.B, self.Colour_Secondary.B)


# RainbowMode inherits from only BaseTimeMode as no colour is selected
class RainbowMode(BaseTimeMode):
    def __init__(self):
        super().__init__(10000)
        self.Name = "Rainbow"

    def rainbow(self, shift_rads):
        return round(abs(0.5*math.sin(self.Phase_Rads+shift_rads)+0.5) * 255)

    def update(self):
        self.update_time()
        self.R = self.rainbow(0)
        self.G = self.rainbow(2 * math.pi / 3)
        self.B = self.rainbow(4 * math.pi / 3)


modes = {
    "Solid": SolidMode(colours.index["Red"]),
    "Pulse": PulseMode(5000, colours.index["Red"]),
    "Pair_Fade": PairFadeMode(5000, colours.index["Red"], colours.index["Green"]),
    "Rainbow": RainbowMode()
}
