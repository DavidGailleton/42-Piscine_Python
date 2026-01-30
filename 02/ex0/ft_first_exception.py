def check_temperature(temp_str: str) -> int | None:
    """Test if temperature is correct"""
    try:
        x = int(temp_str)
        if x > 40:
            raise Exception("is too hot for plants (max 40°C)")
        elif x < 0:
            raise Exception("is too cold for plants (min 0°C)")
        else:
            print("Temperature " + temp_str + "°C is perfect for plants!")
            return x
    except ValueError:
        print("Error: '" + temp_str + "' is not a valid number")
    except Exception as ex:
        print("Error: " + temp_str + "°C", ex)
    return (None)

if __name__ == "__main__":
    print("=== Garden Temperature checker ===")
    print("\nTesting temperature: 25")
    check_temperature("25")
    print("\nTesting temperature: abc")
    check_temperature("abc")
    print("\nTesting temperature: 100")
    check_temperature("100")
    print("\nTesting temperature: -50")
    check_temperature("-50")
    print("\nAll tests completed - program didn't crash!")
