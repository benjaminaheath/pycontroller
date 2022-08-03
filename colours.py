class RGB:
    def __init__(self, name, r, g, b):
        self.Name = name
        self.R = r
        self.G = g
        self.B = b


index = {
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
