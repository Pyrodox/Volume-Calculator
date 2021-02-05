from Shift15.Restart_Function import confirm_restart
from Volume_Calc.Volume_Calculations import volume_calculations

print("Welcome to the Volume Calculator.")
print("This calculator calculates volumes of rectangular prisms, cylinders, cones, square pyramids, and spheres.")
print("Please choose: rectangular prism by typing rectangle, and pyramid for square pyramids.\n "
      "The rest are the same (cone is cone).")

while True:
    choice_list = ["rectangle", "cylinder", "cone", "pyramid", "sphere"]

    while True:
        option = input("Please type which 3D shape you'd like to calculate the volume of: ")
        option1 = option.strip().lower()
        if option1 in choice_list:
            break
        while option1 not in choice_list:
            print("Invalid input. Please read the instructions and try again")
            break

    volume_calculations(option1)

    if confirm_restart() == "yes":
        print("The program has reset.")
        continue
    else:
        break
