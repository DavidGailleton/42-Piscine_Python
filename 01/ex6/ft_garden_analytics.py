class Plant:
    name: str
    height: int
    kind: str

    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height
        self.kind = "regular"

    @classmethod
    def grow(self):
        self.height = self.height + 1

class FloweringPlant(Plant):
    color: str
    blooming = False

    def bloom (self):
        self.blooming = True
        print(self.name, "is blooming beautifully !")

    def __init__(self, name, height, color):
        super().__init__(name=name, height=height)
        self.color = color
        self.kind = "flowering"


class PrizeFlower(FloweringPlant):
    prize: int

    def __init__(self, name, height, color, prize):
        super().__init__(name=name, height=height, color=color)
        self.prize = prize
        self.kind = "prize"

class GardenManager:
    __gardens = {}

    class GardenStats:
        @staticmethod
        def garden_report(garden: []):
            i = 0
            for n in garden:
                i = i + 1
            n = 0
            while n < i:
                print(garden[n].name + ":", end=" ")
                print(garden[n].height, "cm", end="")
                if (garden[n].kind == "flowering" or garden[n].kind == "prize"):
                    print(",", garden[n].color, "flowers", end=" ")
                    if (garden[n].blooming):
                        print("(blooming)", end="")
                if (garden[n].kind == "prize"):
                    print(", Prize points:", garden[n].prize, end="")
                print("")
                n = n + 1


    @classmethod
    def get_garden(self, garden: str) -> []:
        return self.__gardens[garden]


    @classmethod
    def add_plant(self, garden: str, new_plant: Plant):
        if garden in self.__gardens:
            i = 0
            for n in self.__gardens[garden]:
                i = i + 1
            new = [None] * (i + 1)
            j = 0;
            while j < i:
                new[j] = self.__gardens[garden][j]
                j = j + 1
            new[i] = new_plant
            self.__gardens[garden] = new
            print("Added", new_plant.name, "to", garden, "'s garden")
        else:
            print("Garden not found")

    @classmethod
    def create_garden_network(self, garden_name: str) -> None:
        if garden_name in self.__gardens:
            print("garden already exist")
        else:
            self.__gardens[garden_name] = []


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


    manager.GardenStats.garden_report(manager.get_garden("Alice"))
