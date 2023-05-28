sensor_overflow_detected = False
sensor_with_overflow_nr = 0
max_temperature = 100.0

def celsius_from_kelvin(kelvins:list)->list:
    celsius_arr = []
    for i in range(len(kelvins)):
        celsius = kelvins[i] - 273
        if celsius > max_temperature:
            sensor_overflow_detected = True
            sensor_with_overflow_nr = i
        celsius_arr.append(kelvins[i] - 273)
    return celsius_arr

sensors_kelvin_degrees = [280.0, 500.0, 350.0, 400.0]
sensor_celsium_degrees = celsius_from_kelvin(sensors_kelvin_degrees)
if sensor_overflow_detected:
    print("overflow sensir: " + str(sensor_with_overflow_nr))
else:
    print("ok")