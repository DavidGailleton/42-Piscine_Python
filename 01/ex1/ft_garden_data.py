class Plants:
    name: str
    height: int
    age: int

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def print_plant(self):
        print(self.name.capitalize() + ":", self.height, end="")
        print("cm,", self.age, "days old")


if __name__ == "__main__":
    x = Plants("rose", 25, 30)
    y = Plants("sunflower", 80, 45)
    z = Plants("cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    x.print_plant()
    y.print_plant()
    z.print_plant()
