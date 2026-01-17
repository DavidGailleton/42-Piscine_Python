from logging import raiseExceptions


class Plant:
    __name: str
    __water: int
    __sun: int

    @classmethod
    def set_name(cls, name: str) -> None:
        if not name or not name[0]:
            raise ValueError("Name cannot be empty")
        cls.__name = name

    @classmethod
    def set_water(cls, water: int) -> None:
        if water < 0:
            raise ValueError("Water level cannot be negative")
        cls.__water = water

    @classmethod
    def set_sun(cls, sun: int) -> None:
        if sun < 0:
            raise ValueError("Sun level cannot be negative")
        cls.__sun = sun

    @classmethod
    def get_name(cls) -> str:
        return cls.__name

    @classmethod
    def get_water(cls) -> int:
        return cls.__water

    @classmethod
    def get_sun(cls) -> int:
        return cls.__sun

    def __init__(self, name: str, water: int, sun: int) -> None:
        self.set_name(name)
        self.set_water(water)
        self.set_sun(sun)


class GardenManager:
    __plants: list[Plant]
    __water_tank_level: int

    @classmethod
    def get_water_tank_level(cls) -> int:
        return cls.__water_tank_level

    @classmethod
    def set_water_tank_level(cls, level: int) -> None:
        cls.__water_tank_level = level

    def add_plant(self, name: str, water: int, sun: int) -> None:
        try:
            new_plant = Plant(name, water, sun)
            i = 0
            for n in self.__plants:
                i = i + 1
            new_lst: list[Plant | None] = [None] * (i + 1)
            i = 0
            for n in self.__plants:
                new_lst[i] = n
                i = i + 1
            new_lst[i] = new_plant
            print("Added", name, "successfully")
        except ValueError as err:
            print(err)

    def water_plants(self) -> None:
        print("Watering plants...")
        try:
            print("Opening watering system")
            for n in self.__plants:
                if self.__water_tank_level <= 0:
                    raise Exception("Caught GardenError: Not enough water in tank")
                n.set_water(n.get_water() + 1)
                self.__water_tank_level = self.__water_tank_level - 1;
                print("Watering", n.get_name(), "- success")
        except Exception as err:
            print(err);
        finally:
            print("Closing watering system (cleanup)")

    def __init__(self) -> None:
        self.__plants = []
        self.__water_tank_level = 0


if __name__ == "__main__":
    manager = GardenManager()
    manager.set_water_tank_level(10)
    manager.add_plant("Tomato", 2, 10)
    manager.add_plant("Lettuce", 5, 7)
    manager.water_plants()
