class RectangularPrism:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        volume = self.length * self.width * self.height
        print(volume)


class Cylinder:
    def __init__(self, r, h):
        self.r = r
        self.h = h

    def volume(self):
        volume = 3.14 * (self.r**2) * self.h
        print(volume)


class Sphere:
    def __init__(self, r):
        self.r = r

    def volume(self):
        volume = 1.33 * 3.14 * (self.r**3)
        print(volume)


class Cone:
    def __init__(self, r, h):
        self.r = r
        self.h = h

    def volume(self):
        volume = .33 * 3.14 * (self.r**2) * self.h
        print(volume)


class SquarePyramid:
    def __init__(self, length, w, h):
        self.length = length
        self.w = w
        self.h = h

    def volume(self):
        volume = .33 * self.length * self.w * self.h
        print(volume)