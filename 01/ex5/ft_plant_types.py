class Plant:
    name: str
    height: int
    age: int

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        print(self.name.capitalize() + ":", self.height, end="")
        print("cm,", self.age, "days old")


class Flower(Plant):
    color: str

    def bloom(self):
        print(self.name + " is blooming beautifully !")

    def __init__(self, name, height, age, color):
        super().__init__(name=name, height=height, age=age)
        self.color = color


class Tree(Plant):
    trunk_diameter: str

    def produce_shade(self):
        shade_size = self.height * self.trunk_diameter / 1000
        print(self.name, "provides", shade_size, "square meter")

    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name=name, height=height, age=age)
        self.trunk_diameter = trunk_diameter


class Vegetable(Plant):
    harvest_season: str
    nutritional_value: str

    def __init__(self, name, height, age, hs, nv):
        super().__init__(name=name, height=height, age=age)
        self.harvest_season = hs
        self.nutritional_value = nv


if __name__ == "__main__":
    flower0 = Flower("Rose", 30, 5, "red")
    flower1 = Flower("Chrysanthem", 50, 1, "yellow")
    tree0 = Tree("Platane", 300, 6, 30)
    tree1 = Tree("Sapin", 700, 15, 50)
    vegetable0 = Vegetable("Salade", 30, 1, "Summer", "Vitamine c")
    vegetable1 = Vegetable("tomato", 200, 2, "Autumn", "Vitamine d")
    print(flower0.name, flower0.height, flower0.age, flower0.color)
    flower0.bloom()
    tree0.produce_shade()
    print(vegetable0.name, "is rich in", vegetable0.nutritional_value)
