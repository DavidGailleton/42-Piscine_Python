def water_plants(plant_list: []) -> None:
    for plant in plant_list:
        if plant == None:
            raise ValueError
        print("Watering", plant)


def test_watering_system() -> None:
    plants = ["tomato", "lettuce", "carrots", None]
    try:
        print("Opening watering system")
        water_plants(plants)
    except:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


if __name__ == "__main__":
    test_watering_system()
