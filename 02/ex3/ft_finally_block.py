def water_plants(plant_list: list[str | None]) -> None:
    """Display watering plant if plant is a string"""
    for plant in plant_list:
        if not plant:
            raise ValueError
        print("Watering", plant)


def test_watering_system() -> None:
    """Tester for water_plants() function"""
    plants = ["tomato", "lettuce", "carrots", None]
    print("=== Garden Watering System ===")
    print("\nTesting normal watering...")
    try:
        print("Opening watering system")
        water_plants(plants)
    except ValueError:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")
    print("\nCleanup always happens, even with errors")


if __name__ == "__main__":
    test_watering_system()
