import math
import sys


def print_distance(a: tuple[int, int, int], b: tuple[int, int, int]) -> None:
    distance = math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2+(a[2]-b[2])**2)
    print("Distance between (", end="")
    print(a[0], end="")
    print(", ", end="")
    print(a[1], end="")
    print(", ", end="")
    print(a[2], end="")
    print(") and (", end="")
    print(b[0], end="")
    print(", ", end="")
    print(b[1], end="")
    print(", ", end="")
    print(b[2], end="")
    print("):", distance)


if __name__ == "__main__":
    argv = sys.argv
    try:
        if len(argv) != 2:
            raise Exception("Invalid number of args")
        args = argv[1].split(',')
        if len(args) != 3:
            raise Exception("Invalid argument format." +
                            "Try like this : \"15,64,78\"")
        int_args = (int(args[0]), int(args[1]), int(args[2]))
        print("Parsing coordinates:", args[1])
        print_distance((0, 0, 0), int_args)
    except ValueError as err:
        print("Parsing invalid coordinates: \"", end="")
        print(argv[1], end="\"\n")
        print(err)
    except Exception as err:
        print(err)
