class Plants:
    name: str
    height: int
    days: int

    def __init__(self, name, height, days):
        self.name = name
        self.height = height
        self.days = days

    def get_info(self):
        print(self.name.capitalize() + ":", self.height, end="")
        print("cm,", self.days, "days old")

    def grow(self):
        self.height = self.height + 1

    def age(self):
        self.days = self.days + 1
        self.grow()


if __name__ == "__main__":
    x = Plants("rose", 25, 1)
    start = x.days;
    x.get_info()
    for n in range(1, 8):
        x.age()
    x.get_info()
    print("Growth this week: +", x.days - start, "cm");
