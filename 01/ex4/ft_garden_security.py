class SecurePlant:
    name: str
    __height: int
    __age: int

    def set_height(self, height: int) -> None:
        if height < 0:
            print("Invalide operation attempted: height", height, "cm [REJECTED]")

        else:
            self.__height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print("Invalide operation attempted: age", age, "days [REJECTED]")
        else:
            self.__age = age

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.__height = height
        self.__age = age


if __name__ == "__main__":
    plant = SecurePlant("Rose", 10, 3)
    print(plant.name, plant.get_height(), plant.get_age())
    plant.set_height(-10)
    plant.set_age(30)
    print(plant.name, plant.get_height(), plant.get_age())
