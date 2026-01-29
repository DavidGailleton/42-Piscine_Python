class Plant:
    name: str
    height: int
    days: int

    def __init__(self, name: str, height: int, days: int) -> None:
        """Init plant with his value"""
        self.name = name
        self.height = height
        self.days = days

    def print_plant(self) -> None:
        """Display plant informations"""
        print(self.name, ": ", self.height,
              "cm, ", self.days, " days old", sep="")


if __name__ == "__main__":
    x = Plant("rose", 25, 30)
    y = Plant("sunflower", 80, 45)
    z = Plant("cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    x.print_plant()
    y.print_plant()
    z.print_plant()
