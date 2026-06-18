def validate_temperature(temp):

    if temp < -20 or temp > 60:
        return "Invalid Sensor Data"

    return "Valid Sensor Data"


if __name__ == "__main__":

    temp = float(input("Enter Temperature: "))

    print(validate_temperature(temp))