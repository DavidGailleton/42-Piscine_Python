def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    if not plant_name or not plant_name[0]:
        raise ValueError("Error: Plant name cannot be empty")
    elif water_level < 1:
        raise ValueError(f"Error: Water level {water_level}\
 is too low (min 1)")
    elif water_level > 10:
        raise ValueError(f"Error: Water level {water_level}\
 is too high (max 10)")
    elif sunlight_hours < 2:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours}\
 is too low (min 2)")
    elif sunlight_hours > 12:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours}\
 is too high (max 12)")
    else:
        print("Plant '" + plant_name + "' is healthy!")


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===")
    print("\nTesting good values...")
    try:
        check_plant_health("tomato", 5, 5)
    except ValueError as err:
        print(err)
    print("\nTesting bad water level...")
    try:
        check_plant_health("salade", 0, 5)
    except ValueError as err:
        print(err)
    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("carrots", 5, 20)
    except ValueError as err:
        print(err)
    print("\nTesting empty plant name...")
    try:
        check_plant_health("", 5, 5)
    except ValueError as err:
        print(err)
    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
