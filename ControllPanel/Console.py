from ControllPanel import Requests

print()
print("Bienvenido!")

while True:

    print()

    print("All teh st00f dat u can do:")
    print()

    print("0: Exit.")
    print("1: Create a new rule.")
    print("2: List all actuators.")
    print("3: Add an actuator.")
    print("4: Update an actuator.")
    print("5: List all sensors.")
    print("6: Add a new sensor.")
    print()

    option = input("What would you like to do? ")

    print()

    try:
        option = int(option)
    except ValueError:
        print("Input has to be an integer.")

    print()

    if option not in range(0, 7):
        print(f"{option} is not a valid option.")
        continue

    if option == 0:
        exit(0)

    elif option == 1:

        atype = input("Actuator type: ")
        aid = input("Actuator id: ")

        try:
            aid = int(aid)
        except ValueError:
            print("Actuator id has to be an integer.")

        sensor_type = input("Sensor type: ")
        sensor_id = input("Sensor id: ")

        try:
            sensor_id = int(sensor_id)
        except ValueError:
            print("Sensor id has to be an integer.")

        threshold = input("Threshold: ")

        try:
            threshold = float(threshold)
        except ValueError:
            print("Threshold has to be a float.")

        gt = input("Greater than or less than threshold? ")

        try:
            gt = bool(gt)
        except ValueError:
            print("Please give a boolean value.")

        rule = {"atype": atype, "aid": aid, "type": sensor_type,
                "id": sensor_id, "threshold": threshold, "gt": gt}

        Requests.post_new_rule(rule, atype, aid)

    elif option == 2:
        Requests.list_actuators()

    elif option == 3:
        actuator_id = input("Actuator id: ")

        try:
            actuator_id = int(actuator_id)
        except ValueError:
            print("Actuator id has to be an integer.")

        actuator_type = input("Actuator type: ")
        active = input("Active: ")

        try:
            active = bool(active)
        except ValueError:
            print("Please give a boolean value.")

        actuator = {"id": actuator_id, "type": actuator_type, "active": active}

        Requests.add_actuator(actuator)

    elif option == 4:
        boolean_value = input("Please input a boolean value (not sure what for)")

        try:
            boolean_value = bool(boolean_value)
        except ValueError:
            print("Please give a boolean value.")

        atype = input("What is the actuator type?")
        aid = input("What is the id of the actuator?")

        try:
            aid = int(aid)
        except ValueError:
            print("Actuator id has to be an integer.")

        Requests.update_actuator(boolean_value, atype, aid)

    elif option == 5:
        Requests.list_sensors()

    elif option == 6:
        sensor_id = input("Sensor id: ")
        try:
            sensor_id = int(sensor_id)
        except ValueError:
            print("Sensor id has to be an integer.")

        sensor_type = input("Sensor_type: ")

        sensor = {"id": sensor_id, "type": sensor_type}

        Requests.add_sensor(sensor)

    print()

    exit_or_nah = None

    while exit_or_nah not in ['y', 'n']:

        exit_or_nah = input("Would you like to do more? (y/n)")

        if exit_or_nah not in ['y', 'n']:
            print(f"{exit_or_nah} is not a valid option.")

    if exit_or_nah == "n":
        exit(0)
