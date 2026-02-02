from typing_extensions import override


class GardenError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__()
        self.message: str = message

    @override
    def __str__(self) -> str:
        return f"Caught a garden error: {self.message}"


class SunlightError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)

    @override
    def __str__(self) -> str:
        return f"Caught SunlightError: {self.message}"


class WaterError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)

    @override
    def __str__(self) -> str:
        return f"Caught WaterError: {self.message}"


class Plant:
    __name: str
    __water_level: int
    __sunlight_hours: int

    def __init__(self, name: str, water_level: int,
                 sunlight_hours: int) -> None:
        if name == "":
            raise Exception("Plant name cannot be empty")
        self.set_name(name)
        self.__water_level = water_level
        self.__sunlight_hours = sunlight_hours
        print(f"Added {name} successfully")

    def get_name(self) -> str:
        return self.__name

    def get_water_level(self) -> int:
        return self.__water_level

    def get_sunlight_hours(self) -> int:
        return self.__sunlight_hours

    def set_name(self, name: str) -> None:
        if name == "":
            raise Exception("Name cannot be empty")
        self.__name = name

    def set_water_level(self, water_level: int) -> None:
        if water_level < 1:
            raise WaterError(f"Water level {water_level} is too low (min 1)")
        if water_level > 10:
            raise WaterError(f"Water level {water_level} is too high (max 10)")
        self.__water_level = water_level

    def set_sunlight_hours(self, sunlight_hours: int) -> None:
        if sunlight_hours < 2:
            raise SunlightError(f"Sunlight hours {sunlight_hours}\
 is too low (min 2)")
        if sunlight_hours > 12:
            raise SunlightError(f"Sunlight hours {sunlight_hours}\
 is too high (max 12)")
        self.__sunlight_hours = sunlight_hours

    def water_plant(self) -> None:
        self.__water_level += 1
        print(f"Watering {self.__name} - success")


class GardenManager:
    garden: list[Plant]
    __water_tank_level: int

    class WaterTankError(Exception):
        def __init__(self, message: str) -> None:
            super().__init__()
            self.message: str = message

        @override
        def __str__(self) -> str:
            return f"Caught WaterTankError: {self.message}"

    def __init__(self) -> None:
        self.garden = []
        self.__water_tank_level = 0

    def get_water_tank_level(self) -> int:
        return self.__water_tank_level

    def set_water_tank_level(self, water_level: int) -> None:
        try:
            if water_level < 0:
                raise self.WaterTankError("Water level cannot be negative")
            self.__water_tank_level = water_level
        except self.WaterTankError as err:
            print(err)

    def add_plants_to_garden(self, plants: list[tuple[str, int, int]]) -> None:
        try:
            for a, b, c in plants:
                self.garden.append(Plant(a, b, c))
        except Exception as err:
            print("Error adding plant:", err)

    def check_plants_health(self) -> None:
        try:
            for plant in self.garden:
                if plant.get_water_level() < 1:
                    raise WaterError(f"{plant.get_name()}: Water level\
 {plant.get_water_level()} is too low (min 1)")
                elif plant.get_water_level() > 10:
                    raise WaterError(f"{plant.get_name()}: Water level\
 {plant.get_water_level()} is too high (max 10)")
                elif plant.get_sunlight_hours() < 2:
                    raise SunlightError(f"{plant.get_name()}: Sunlight hours\
 {plant.get_sunlight_hours()} is too low (min 2)")
                elif plant.get_sunlight_hours() > 12:
                    raise SunlightError(f"{plant.get_name()}: Sunlight hours\
 {plant.get_sunlight_hours()} is too high (max 12)")
                else:
                    print(f"{plant.get_name()}: healthy (water:\
 {plant.get_water_level()}, sun: {plant.get_sunlight_hours()})")
        except (WaterError, SunlightError) as err:
            print(err)

    def water_plants(self) -> None:
        """Watering all plants"""
        try:
            print("Opening watering system")
            for plant in self.garden:
                if self.__water_tank_level > 0:
                    plant.water_plant()
                    self.__water_tank_level -= 1
                else:
                    raise self.WaterTankError("Water tank is empty")
        except self.WaterTankError as err:
            print(err)
        finally:
            print("Closing watering system (cleanup)")


def test_garden_management() -> None:
    manager = GardenManager()
    print("=== Garden Management System ===\n")
    print("Adding plants to garden...")
    manager.add_plants_to_garden([
        ("Rose", 5, 5),
        ("Oak", 7, 2),
        ("Chrysantem", 2, 6),
        ("Tomato", 10, 3),
        ("", 8, 7)
        ])
    print("\nWatering plants...")
    manager.set_water_tank_level(10)
    manager.water_plants()
    print("\nChecking plant health...")
    manager.check_plants_health()
    print("\nTesting error recovery...")
    manager.set_water_tank_level(0)
    manager.water_plants()
    print("System recovered and continuing")
    print("\nGarden management system test complet!")


if __name__ == "__main__":
    test_garden_management()
