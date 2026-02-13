from os import system 
system("clear") # This allows the program to clear the screen automatically.

from module import Robot

name = input("Enter a name for your robot: ")
color = input("Enter a color for your robot: ")
robot = Robot(name, color)

while True:
    print("\nCommands: Charge | Work | Repair | Status | Recolor | Shutdown")
    command = input("What would you like to do next? ")
    system("clear")

    if command.lower() == "charge":
        print("How much to charge? ")
        print(robot.battery + int(input()))

    elif command.lower() == "work":
        hours = input("How many hours to work? ")
        print (name + " has worked " + hours + " hours")

    elif command.lower() == "repair":
        print(robot.repair())

    elif command.lower() == "status":
        print(robot.status())

    elif command.lower() == "recolor":
        new_color = input("What is the new color? ")
        robot.color = new_color

    elif command.lower() == "shutdown":
        print("Shutting down robot...")
        break

    else:
        print("Unknown command.")