class Plant:
    name: str
    height: int
    days: int

    def get_info(self) -> None:
        """Display plant informations"""
        print(self.name, " (", self.height,
              "cm, ", self.days, " days)", sep="")

    def grow(self) -> None:
        """Increase height"""
        self.height = self.height + 1

    def age(self) -> None:
        """Increase days by one and grow plant"""
        self.days = self.days + 1
        self.grow()

    def __init__(self, name: str, height: int, age: int) -> None:
        """Init plant with his values and display his values"""
        self.name = name
        self.height = height
        self.days = age
        print("Created: ", end="")
        self.get_info()


class PlantFactory:
    @staticmethod
    def create_plants(plants: list[tuple[str,
                                         int, int]]) -> list[Plant | None]:
        """Create list of plants by list of arguments"""
        i = 0
        for n in plants:
            i = i + 1
        new_plants: list[Plant | None] = [None] * i
        i = 0
        for n in plants:
            new_plants[i] = Plant(n[0], n[1], n[2])
            i = i + 1
        return new_plants


if __name__ == "__main__":
    plants = PlantFactory.create_plants([
        ("Rose", 50, 2),
        ("Chrysanthem", 30, 1),
        ("Rosemary", 60, 5),
        ("Cucumber", 40, 3),
        ("Salade", 15, 4)
    ])
    i = 0
    for n in plants:
        i = i + 1
    print("\nTotal plants created:", i)
