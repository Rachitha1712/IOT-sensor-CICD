from sensor import validate_temperature

def test_valid_temperature():
    assert validate_temperature(25) == "Valid Sensor Data"

def test_high_temperature():
    assert validate_temperature(90) == "Invalid Sensor Data"

def test_low_temperature():
    assert validate_temperature(-30) == "Invalid Sensor Data"