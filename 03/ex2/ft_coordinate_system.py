import math
import sys


def print_distance(a: tuple[int, int, int], b: tuple[int, int, int]) -> None:
    distance = math.sqrt(
        (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2
    )
    print(f"Distance between: {a} and {b}: {distance}")


if __name__ == "__main__":
    argv = sys.argv
    try:
        if len(argv) != 2:
            raise Exception("Invalid number of args")
        print(f'Parsing coordinates: "{argv[1]}"')
        args = argv[1].split(",")
        if len(args) != 3:
            raise Exception(
                "Invalid argument format." + 'Try like this : "15,64,78"'
            )
        int_args = (int(args[0]), int(args[1]), int(args[2]))
        print(f"Parsed position: {int_args}")
        print_distance((0, 0, 0), int_args)
    except ValueError as err:
        print(f'Invalid coordinates: "{argv[1]}"')
        print(err)
    except Exception as err:
        print(err)
