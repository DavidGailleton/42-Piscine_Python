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


if __name__ == "__main__":
    x = Plants("rose", 25, 1)
    x.get_info()
    i = 1
    while i < 8:
        x.age()
        i = i + 1
    x.get_info()
