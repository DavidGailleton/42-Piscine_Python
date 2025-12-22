class Plants:
    name: str
    height: int
    p_age: int

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.p_age = age

    def get_info(self):
        print(self.name.capitalize() + ":", self.height, end="")
        print("cm,", self.p_age, "days old")

    def grow(self):
        self.height = self.height + 1

    def age(self):
        self.p_age = self.p_age + 1
        self.grow()


if  __name__ == "__main__":
    plant_1 = Plants("Rose", 50, 2)
    plant_2 = Plants("Chrysanthem", 30, 1)
    plant_3 = Plants("Rosemary", 60, 5)
    plant_4 = Plants("Cucumber", 40, 3)
    plant_5 = Plants("Salade", 15, 4)
    plants = [plant_1, plant_2, plant_3, plant_4, plant_5]
    i = 0
    for n in plants:
        print("Created:", end=" ")
        n.get_info()
        i = i + 1
    print("\nTotal plants created:", i)

