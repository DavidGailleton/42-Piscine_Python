class SecurePlant:
    name: str
    __height: int
    __age: int

    def set_height(self, height: int) -> None:
        """Set height to plant"""
        if height < 0:
            print("Invalide operation attempted: height ",
                  height, "cm [REJECTED]", sep="")
            print("Secrity: Negative height rejected")
        else:
            self.__height = height
            print("Height updated: ", height, "cm [OK]", sep="")

    def set_age(self, age: int) -> None:
        """Set age to plant"""
        if age < 0:
            print("Invalide operation attempted: age", age, "days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = age
            print("Age updated:", age, "days [OK]")

    def get_height(self) -> int:
        """Get plant height"""
        return self.__height

    def get_age(self) -> int:
        """Get plant age"""
        return self.__age

    def __init__(self, name: str, height: int, age: int) -> None:
        """Init plant with his value"""
        self.name = name
        self.set_height(height)
        self.set_age(age)
        print("Plant created:", name)


if __name__ == "__main__":
    plant = SecurePlant("Rose", 10, 3)
    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-10)
    print("Current plant: ", plant.name, " (", plant.get_height(),
          "cm, ", plant.get_age(), " days)", sep="")
