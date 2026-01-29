class Plants:
    name: str
    height: int
    days: int

    def __init__(self, name: str, height: int, days: int) -> None:
        """Init plant with his value"""
        self.name = name
        self.height = height
        self.days = days

    def get_info(self) -> None:
        """Display plant informations"""
        print(self.name, ": ", self.height,
              "cm, ", self.days, " days old", sep="")

    def grow(self) -> None:
        """Increase height"""
        self.height = self.height + 1

    def age(self) -> None:
        """Increase days by one and grow plant"""
        self.days = self.days + 1
        self.grow()


if __name__ == "__main__":
    x = Plants("rose", 25, 30)
    start = x.days
    print("=== Day 1 ===")
    x.get_info()
    for n in range(1, 7):
        x.age()
    print(f"=== Day {x.days - start + 1} ===")
    x.get_info()
    print("Growth this week: +",
          x.days - start, "cm", sep="")
