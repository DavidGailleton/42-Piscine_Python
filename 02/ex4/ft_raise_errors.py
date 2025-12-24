def check_plant_health(plant_name, water_level, sunlight_hours):
    if not plant_name or not plant_name[0]:
        raise ValueError("Error: Plant name cannot be empty")
    elif water_level < 1:
        raise ValueError(f"Error: Water level {water_level} is too low (min 1)")
    elif water_level > 10:
        raise ValueError(f"Error: Water level {water_level} is too high (max 10)")
    elif sunlight_hours < 2:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} is too low (min 2)")
    elif sunlight_hours > 12:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} is too high (max 12)")
    else:
        print("Plant '" + plant_name + "' is healthy!")


def test_plant_checks():
    try:
        check_plant_health("tomato", 5, 5)
    except ValueError as err:
        print(err)
    try:
        check_plant_health("salade", 0, 5)
    except ValueError as err:
        print(err)
    try:
        check_plant_health("carrots", 5, 20)
    except ValueError as err:
        print(err)
    try:
        check_plant_health("", 5, 5)
    except ValueError as err:
        print(err)
    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
