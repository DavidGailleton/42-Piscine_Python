from typing_extensions import override


class GardenError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__()
        self.message: str = message

    @override
    def __str__(self) -> str:
        return f"Caught a garden error: {self.message}"


class PlantError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)

    @override
    def __str__(self) -> str:
        return f"Caught PlantError: {self.message}"


class WaterError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)

    @override
    def __str__(self) -> str:
        return f"Caught WaterError: {self.message}"


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print("\n Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as err:
        print(err)
    print("\nTesting WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as err:
        print(err)
    print("\nTesting catching all garden errors...")
    try:
        raise GardenError("The tomato plant is wilting")
    except GardenError as err:
        print(err)
    try:
        raise GardenError("Not enough water in the tank")
    except GardenError as err:
        print(err)
    print("\nAll custom error types work correctly !")
