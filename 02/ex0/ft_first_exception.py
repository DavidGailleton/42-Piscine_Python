def check_temperature(temp_str: str) -> int:
    print("Testing temperature:", temp_str)
    try:
        x = int(temp_str)
        if x > 40:
            raise Exception("is too hot for plants (max 40°C)")
        elif x < 0:
            raise Exception("is too cold for plants (min 0°C)")
        else:
            print("Temperature " + temp_str + "°C is perfect for plants!")
    except ValueError:
        print("Error: '" + temp_str + "' is not a valid number")
        pass
    except Exception as ex:
        print("Error: " + temp_str + "°C", ex)
        pass

if __name__ == "__main__":
    check_temperature("25")
    print("")
    check_temperature("abc")
    print("")
    check_temperature("100")
    print("")
    check_temperature("-50")
    print("")
    print("All tests completed - program didn't crash!")
