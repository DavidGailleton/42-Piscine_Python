def garden_operations(case: str) -> None:
    if case == "ValueError":
        int("abc")
    elif case == "ZeroDivisionError":
        10 / 0
    elif case == "FileNotFoundError":
        open("notexist")
    elif case == "KeyError":
        dic = {"test0": "t", "test1": "t"}
        dic["a"]


def test_error_types() -> None:
    try:
        garden_operations("ValueError")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    try:
        garden_operations("ZeroDivisionError")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")

    try:
        garden_operations("FileNotFoundError")
    except FileNotFoundError as err:
        print("Caught FileNotFoundError:", err)

    try:
        garden_operations("KeyError")
    except KeyError as err:
        print("Caught KeyError:", err)

    try:
        garden_operations("ValueError")
    except (ValueError, KeyError, ZeroDivisionError, FileNotFoundError):
        print("Caught an error, but program continues!")


if __name__ == "__main__":
    test_error_types()
    print("All error types tested successfully!")
