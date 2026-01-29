class Plant:
    name: str
    height: int
    total_growth: int
    __kind: str

    def __init__(self, name: str, height: int) -> None:
        """Init plant with his value"""
        self.name = name
        self.height = height
        self.__kind = "regular"
        self.total_growth = 0

    def get_kind(self) -> str:
        """Return __kind value"""
        return self.__kind

    def set_kind(self, kind: str) -> None:
        """Set __kind value"""
        self.__kind = kind

    def grow(self) -> None:
        """Grow the plant"""
        self.height = self.height + 1
        self.total_growth += 1


class FloweringPlant(Plant):
    color: str
    blooming: bool = False

    def bloom(self) -> None:
        """Set blooming to true"""
        self.blooming = True
        print(self.name, "is blooming beautifully !")

    def __init__(self, name: str, height: int, color: str) -> None:
        """Init Flowering plant with his value"""
        super().__init__(name=name, height=height)
        self.color = color
        self.set_kind("flowering")


class PrizeFlower(FloweringPlant):
    prize: int

    def __init__(self, name: str, height: int, color: str, prize: int) -> None:
        """Init prize flower with his value"""
        super().__init__(name=name, height=height, color=color)
        self.prize = prize
        self.set_kind("prize")


class GardenManager:
    gardens: dict[str, list[Plant | FloweringPlant | PrizeFlower]]
    nb_gardens: int

    def __init__(self) -> None:
        """Init garden manager"""
        self.gardens = {}
        self.nb_gardens = 0

    class GardenStats:
        @classmethod
        def garden_report(cls,
                          garden: list[Plant |
                                       FloweringPlant |
                                       PrizeFlower] | None) -> None:
            """Start all garden report"""
            if garden is not None:
                cls.flower_in_garden(garden)
                print("")
                cls.added_plant_report(garden)
                cls.plants_in_garden(garden)
            else:
                print("Garden not provide")

        @staticmethod
        def flower_in_garden(garden: list[Plant |
                                          FloweringPlant |
                                          PrizeFlower]) -> None:
            """List flower in garden and display their status"""
            for n in garden:
                print("-", n.name + ":", end=" ")
                print(n.height, "cm", end="")
                if n.get_kind() == "flowering" or n.get_kind() == "prize":
                    print(",", n.color, "flowers", end="")
                    if n.blooming:
                        print(" (blooming)", end="")
                if n.get_kind() == "prize":
                    print(", Prize points:", n.prize, end="")
                print("")

        @staticmethod
        def added_plant_report(garden: list[Plant |
                                            FloweringPlant |
                                            PrizeFlower]) -> None:
            """Report number of plant added to garden"""
            total_growth = 0
            total_plants = 0
            for n in garden:
                total_plants += 1
                total_growth += n.total_growth
            print(f"Plants added: {total_plants},",
                  f"Total growth: {total_growth}cm")

        @staticmethod
        def plants_in_garden(garden: list[Plant |
                                          FloweringPlant |
                                          PrizeFlower]) -> None:
            """Report number of plant by types"""
            nb_regular = 0
            nb_flowering = 0
            nb_prize = 0
            for n in garden:
                if n.get_kind() == "regular":
                    nb_regular += 1
                elif n.get_kind() == "flowering":
                    nb_flowering += 1
                elif n.get_kind() == "prize":
                    nb_prize += 1
            print(f"Plant types: {nb_regular} regular,",
                  f"{nb_flowering} flowering, {nb_prize} prize flowers")

    def get_nb_gardens(self) -> int:
        """return the number of garden in the manager"""
        return self.nb_gardens

    def get_garden(self, garden: str) -> list[Plant |
                                              FloweringPlant |
                                              PrizeFlower] | None:
        """Return the plant list of the garden name provide if exist"""
        if garden in self.gardens:
            return self.gardens[garden]
        else:
            return None

    def add_plant(self, garden: str, new_plant: Plant |
                  FloweringPlant |
                  PrizeFlower) -> None:
        """Add one plant to the garden if exist"""
        if garden in self.gardens:
            i = 0
            for n in self.gardens[garden]:
                i = i + 1
            new: list[Plant |
                      FloweringPlant |
                      PrizeFlower] = [Plant("", 0)] * (i + 1)
            j = 0
            while j < i:
                new[j] = self.gardens[garden][j]
                j = j + 1
            new[i] = new_plant
            self.gardens[garden] = new
            print("Added ", new_plant.name, " to ",
                  garden, "'s garden", sep="")
        else:
            print("Garden not found")

    def create_garden_network(self, garden_name: str) -> None:
        """Create a garden by name provide if it not exist"""
        if garden_name in self.gardens:
            print("garden already exist")
        else:
            self.gardens[garden_name] = []
            self.nb_gardens += 1

    def grow_all(self, garden: str) -> None:
        """Make all plant of one garden to grow"""
        if garden in self.gardens:
            print(f"{garden} is helping all plants grow...")
            for n in self.gardens[garden]:
                print(f"{n.name} grew 1cm")
                n.grow()
        else:
            print("Garden not found")


if __name__ == "__main__":
    oak = Plant("oak tree", 101)
    rose = FloweringPlant("rose", 26, "red")
    sunflower = PrizeFlower("sunflower", 51, "yellow", 10)
    manager = GardenManager()

    rose.bloom()
    manager.create_garden_network("Alice")
    manager.add_plant("Alice", oak)
    manager.add_plant("Alice", rose)
    manager.add_plant("Alice", sunflower)
    manager.add_plant("Bob", oak)
    manager.grow_all("Alice")
    manager.grow_all("Alice")
    print("\n\nGardenReport")
    manager.GardenStats.garden_report(manager.get_garden("Alice"))
