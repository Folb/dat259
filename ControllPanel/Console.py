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
        sensor_type = input("Sensor type: ")
        sensor_id = input("Sensor id: ")
        threshold = input("Threshold: ")
        gt = input("Greater than or less than threshold? ")

        rule = {"atype": atype, "aid": aid, "sensor_type": sensor_type,
                "sensor_id": sensor_id, "threshold": threshold, "gt": gt}

        Requests.post_new_rule(rule, atype, aid)

    elif option == 2:
        Requests.list_actuators()

    elif option == 3:
        actuator_id = input("Actuator id: ")
        actuator_type = input("Actuator type: ")
        active = input("Active: ")

        actuator = {"actuator_id": actuator_id, "actuator_type": actuator_type, "active": active}

        Requests.add_actuator(actuator)

    elif option == 4:
        boolean_value = input("Please input a boolean value (not sure what for)")
        atype = input("What is the actuator type?")
        aid = input("What is the id of the actuator?")
        Requests.update_actuator(boolean_value, atype, aid)

    elif option == 5:
        Requests.list_sensors()

    elif option == 6:
        # sensorId = Column(Integer, nullable=False)
        # sensorType = Column(String(30), nullable=False)
        sensor_id = input("Sensor id: ")
        sensor_type = input("Sensor_type: ")

        sensor = {"sensor_id": sensor_id, "sensor_type": sensor_type}

        Requests.add_sensor(sensor)

    print()

    exit_or_nah = None

    while exit_or_nah != "n" and exit_or_nah != "y":

        exit_or_nah = input("Would you like to do more? (y/n)")

        if exit_or_nah != "y" and exit_or_nah != "n":
            print(f"{exit_or_nah} is not a valid option.")

    if exit_or_nah == "n":
        exit(0)

