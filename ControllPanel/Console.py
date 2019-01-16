from ControllPanel import Requests

print()
print("Bienvenido!")

while True:

    print()

    print("Here are your options, bitch:")
    print()

    print("0: Exit.")
    print("1: Create a new rule.")
    print("2: List all actuators.")
    print("3: Add an actuator.")
    print("4: Update an actuator.")
    print("5: List all sensors.")
    print("6: Add a new sensor.")
    print()

    option = int(input("What would you like to do? "))

    if option not in range(0, 7):
        print(f"{option} is not a valid option.")
        continue

    if option == 0:
        exit(0)

    elif option == 1:
        rule = dict(input("Please input the new rule as a dictionary."))
        atype = input("What is the actuator type?")
        aid = input("What is the id of the actuator?")
        Requests.post_new_rule(rule, atype, aid)

    elif option == 2:
        Requests.list_actuators()

    elif option == 3:
        actuator = dict(input("Please input the new actuator as a dictionary."))
        Requests.add_actuator(actuator)

    elif option == 4:
        boolean_value = input("Please input a boolean value (not sure what for)")
        atype = input("What is the actuator type?")
        aid = input("What is the id of the actuator?")
        Requests.update_actuator(boolean_value, atype, aid)

    elif option == 5:
        Requests.list_sensors()

    elif option == 6:
        sensor = dict(input("Please input the new sensor as a dictionary."))
        Requests.add_sensor(sensor)

    print()

    exit_or_nah = None

    while exit_or_nah != "n" and exit_or_nah != "y":

        exit_or_nah = input("Would you like to do more? (y/n)")

        if exit_or_nah != "y" and exit_or_nah != "n":
            print(f"{exit_or_nah} is not a valid option.")

    if exit_or_nah == "n":
        exit(0)

