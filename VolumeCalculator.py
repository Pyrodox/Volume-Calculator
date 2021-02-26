from Shift15.Restart_Function import confirm_restart


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


def volume_calculations(option1):
    val_error = "Please enter your values again."
    if option1 == "rectangle":
        try:
            rlength = float(input("Please type the length: "))
            rwidth = float(input("Please type the width: "))
            rheight = float(input("Please type the height: "))
            r1 = RectangularPrism(rlength, rwidth, rheight)
            r1.volume()
        except ValueError:
            print(val_error)
    elif option1 == "cylinder":
        try:
            cyradius = float(input("Please type the radius: "))
            cyheight = float(input("Please type the height: "))
            cy1 = Cylinder(cyradius, cyheight)
            cy1.volume()
        except ValueError:
            print(val_error)
    elif option1 == "sphere":
        try:
            sphradius = float(input("Please type the radius: "))
            sp1 = Sphere(sphradius)
            sp1.volume()
        except ValueError:
            print(val_error)
    elif option1 == "cone":
        try:
            coradius = float(input("Please type the radius: "))
            coheight = float(input("Please type the height: "))
            co1 = Cone(coradius, coheight)
            co1.volume()
        except ValueError:
            print(val_error)
    elif option1 == "pyramid":
        try:
            pylength = float(input("Please type the length: "))
            pywidth = float(input("Please type the length: "))
            pyheight = float(input("Please type the height: "))
            py1 = SquarePyramid(pylength, pywidth, pyheight)
            py1.volume()
        except ValueError:
            print(val_error)


print("This calculator calculates volumes of rectangular prisms, cylinders, cones, square pyramids, and spheres.")
print("Please choose: rectangular prism by typing rectangle, and pyramid for square pyramids. "
      "The rest are the same (cone is cone).")

while True:
    choice_list = ["rectangle", "cylinder", "cone", "pyramid", "sphere"]
    while True:
        option = input("Please type which 3D shape you'd like to calculate the volume of: ")
        option = option.strip().lower()
        if option in choice_list:
            break
        while option not in choice_list:
            print("Invalid input. Please read the instructions and try again")
            break
    volume_calculations(option)

    if confirm_restart() == "yes":
        print("The program has reset.")
        continue
    else:
        break
