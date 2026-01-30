def garden_operations(case: str) -> None:
    """Test some opereation case"""
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
    """Tester function to catch errors"""
    print("=== Garden Error Types Demo ===")
    print("\nTesting ValueError...")
    try:
        garden_operations("ValueError")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    print("\nTesting ZeroDivisionError...")
    try:
        garden_operations("ZeroDivisionError")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    print("\nTesting FileNotFoundError...")
    try:
        garden_operations("FileNotFoundError")
    except FileNotFoundError as err:
        print("Caught FileNotFoundError:", err)
    print("\nTesting KeyError...")
    try:
        garden_operations("KeyError")
    except KeyError as err:
        print("Caught KeyError:", err)
    print("\nTesting multiple errors together...")
    try:
        garden_operations("ValueError")
    except (ValueError, KeyError, ZeroDivisionError, FileNotFoundError):
        print("Caught an error, but program continues!")


if __name__ == "__main__":
    test_error_types()
    print("\nAll error types tested successfully!")
