print("Welcome to the Volume Calculator.")
print("This calculator calculates volumes of rectangular prisms, cylinders, cones, square pyramids, and spheres.")
choice_list = ["rectangle", "cylinder", "cone", "pyramid", "sphere"]
val_error = "Please enter your values again."


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


while True:
    print("Please choose: rectangular prism by typing rectangle, and pyramid for square pyramids.\n "
          "The rest are the same (cone is cone).")

    while True:
        option = input("Please type which 3D shape you'd like to calculate the volume of: ")
        if option.strip().lower() in choice_list:
            break
        while option.strip().lower() not in choice_list:
            print("Invalid input. Please read the instructions and try again")
            break

    if option.strip().lower() == "rectangle":
        try:
            rlength = float(input("Please type the length: "))
            rwidth = float(input("Please type the width: "))
            rheight = float(input("Please type the height: "))
            r1 = RectangularPrism(rlength, rwidth, rheight)
            r1.volume()
        except ValueError:
            print(val_error)

    elif option.strip().lower() == "cylinder":
        try:
            cyradius = float(input("Please type the radius: "))
            cyheight = float(input("Please type the height: "))
            cy1 = Cone(cyradius, cyheight)
            cy1.volume()
        except ValueError:
            print(val_error)

    elif option.strip().lower() == "sphere":
        try:
            sphradius = float(input("Please type the radius: "))
            sp1 = Sphere(sphradius)
            sp1.volume()
        except ValueError:
            print(val_error)

    elif option.strip().lower() == "cone":
        try:
            coradius = float(input("Please type the radius: "))
            coheight = float(input("Please type the height: "))
            co1 = Cone(coradius, coheight)
            co1.volume()
        except ValueError:
            print(val_error)

    elif option.strip().lower() == "pyramid":
        try:
            pylength = float(input("Please type the length: "))
            pywidth = float(input("Please type the length: "))
            pyheight = float(input("Please type the height: "))
            py1 = SquarePyramid(pylength, pywidth, pyheight)
            py1.volume()
        except ValueError:
            print(val_error)

    while True:
        restart = input("Would you like to restart the program? (Type yes or no): ")
        if restart.lower().strip() in ("yes", "no"):
            break
        elif restart.lower().strip() not in ("yes", "no"):
            print("Please type 'yes' or 'no'. ")
            continue

    if restart.lower().strip() == "yes":
        continue
    else:
        break
