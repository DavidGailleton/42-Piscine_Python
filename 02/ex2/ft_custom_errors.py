class GardenError(Exception):
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return f"Caught a garden error: {self.message}" 


class PlantError(GardenError):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"Caught PlantError: {self.message}" 


class WaterError(GardenError):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"Caught WaterError: {self.message}" 


if __name__ == "__main__":
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as err:
        print(err)
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as err:
        print(err)
