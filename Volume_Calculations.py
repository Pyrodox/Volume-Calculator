from Volume_Calc.Volumes import RectangularPrism, Cone, Cylinder, Sphere, SquarePyramid


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
