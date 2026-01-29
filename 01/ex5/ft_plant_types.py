from typing_extensions import override


class Plant:
    name: str
    height: int
    age: int

    def __init__(self, name: str, height: int, age: int) -> None:
        """Init plant with his value"""
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> None:
        """Display plant informations"""
        print(f"{self.name}: {self.height}cm, {self.age} days")


class Flower(Plant):
    color: str

    def bloom(self) -> None:
        """Make flower blooming"""
        print(self.name + " is blooming beautifully !")

    @override
    def get_info(self) -> None:
        """Display Flower info"""
        print(f"{self.name} (Flower): {self.height}cm,",
              f"{self.age} days, {self.color} color")

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Init flower with his value"""
        super().__init__(name=name, height=height, age=age)
        self.color = color


class Tree(Plant):
    trunk_diameter: int

    def produce_shade(self) -> None:
        """Produce shade and display his size"""
        shade_size = self.height * self.trunk_diameter / 1000
        print(self.name, "provides", shade_size, "square meter of shade")

    @override
    def get_info(self) -> None:
        """Display Tree info"""
        print(f"{self.name} (Tree): {self.height}cm,",
              f"{self.age} days, {self.trunk_diameter}cm diameter")

    def __init__(self, name: str, height: int,
                 age: int, trunk_diameter: int) -> None:
        """Init tree with his value"""
        super().__init__(name=name, height=height, age=age)
        self.trunk_diameter = trunk_diameter


class Vegetable(Plant):
    harvest_season: str
    nutritional_value: str

    def print_nutritional_value(self) -> None:
        """Display nutritional value"""
        print(f"{self.name} is rich in {self.nutritional_value}")

    @override
    def get_info(self) -> None:
        """Display Vegetable info info"""
        print(f"{self.name} (Vegetable): {self.height}cm,",
              f"{self.age} days, {self.harvest_season} harvest")

    def __init__(self, name: str, height: int,
                 age: int, hs: str, nv: str) -> None:
        """Init vegetable with his value"""
        super().__init__(name=name, height=height, age=age)
        self.harvest_season = hs
        self.nutritional_value = nv


if __name__ == "__main__":
    flower0 = Flower("Rose", 30, 5, "red")
    flower1 = Flower("Chrysanthem", 50, 1, "yellow")
    tree0 = Tree("Spruce", 300, 6, 30)
    tree1 = Tree("Oak", 700, 15, 50)
    vegetable0 = Vegetable("Salade", 30, 1, "Summer", "Vitamine c")
    vegetable1 = Vegetable("Tomato", 200, 2, "Autumn", "Vitamine d")

    flower0.get_info()
    flower0.bloom()
    print("")
    tree0.get_info()
    tree0.produce_shade()
    print("")
    vegetable0.get_info()
    vegetable0.print_nutritional_value()
