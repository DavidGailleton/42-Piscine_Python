from abc import ABC, abstractmethod
from typing import Any, Union
from typing_extensions import override


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Processed output: {result}"


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        try:
            return f"{data}"
        except Exception as err:
            print(err)
            return "error"

    def validate(self, data: Any) -> bool:
        try:
            for n in data:
                if type(n).__name__ != "int":
                    return False
            return True
        except Exception:
            return False

    @override
    def format_output(self, result: str) -> str:
        try:
            to_processed = result.split(", ")
            res_int: list[int] = []
            for n in to_processed:
                n = n.replace("[", "").replace("]", "")
                if n.isnumeric():
                    res_int = res_int + [int(n)]
            avg = sum(res_int) / len(res_int)
            return f"Processed {len(res_int)} numeric value,\
 sum={sum(res_int)}, avg={avg:.2f}"
        except Exception as err:
            print(f"NumericProcessor / format_output: {err}")
            return "error"


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        return str(data)

    def validate(self, data: Any) -> bool:
        try:
            for char in data:
                if type(char).__name__ != "str":
                    return False
            return True
        except Exception:
            return False

    @override
    def format_output(self, result: str) -> str:
        return f"Processed text: {len(result)}\
 characters, {len(result.split(' '))} words"


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        try:
            return f"{data[0]}: {data[1]}"
        except Exception as err:
            print(err)
            return "error"

    def validate(self, data: Any) -> bool:
        try:
            if len(data) == 2:
                for n in data:
                    if type(n).__name__ != "str":
                        return False
                return True
            return False
        except Exception:
            return False

    @override
    def format_output(self, result: str) -> str:
        try:
            log_res = result.split(":")[0]
            if log_res == "ERROR":
                header = "[ALERT]"
            elif log_res == "INFO":
                header = "[INFO]"
            elif log_res == "SUCCESS":
                header = "[SUCCESS]"
            else:
                header = "[UNKNOWN]"
            return (
                f"{header} {result.split(':', 1)[0]}{result.split(':', 1)[1]}"
            )
        except Exception as err:
            print(err)
            return "error"


def class_tester() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    print("Initializing Numeric Processor...")
    data: Union[list[int | str], str] = [1, 2, 3, 4, 5]
    processor: DataProcessor = NumericProcessor()
    res = processor.process(data)
    is_valid = processor.validate(data)
    formatted_output = processor.format_output(res)
    print(f"processing data: {res}")
    if is_valid:
        print("Validation: Numeric data verified")
    else:
        print("Validation: Invalid numeric data")
    print(f"Output: {formatted_output}")
    print("\nInitializing Text Processor...")
    data = "Hello Nexus World"
    processor = TextProcessor()
    res = processor.process(data)
    is_valid = processor.validate(data)
    formatted_output = processor.format_output(res)
    print(f"processing data: {res}")
    if is_valid:
        print("Validation: Text data verified")
    else:
        print("Validation: Invalid text data")
    print(f"Output: {formatted_output}")
    print("\nInitializing Log Processor...")
    data = ["ERROR", "Connection timeout"]
    processor = LogProcessor()
    res = processor.process(data)
    is_valid = processor.validate(data)
    formatted_output = processor.format_output(res)
    print(f"processing data: {res}")
    if is_valid:
        print("Validation: Log data verified")
    else:
        print("Validation: Invalid log data")
    print(f"Output: {formatted_output}")
    print("\n=== Polymorphic Processing Demo ===\n")
    print(f"Result 1:\
 {NumericProcessor().format_output('[1, 2, 3]')}")
    print(f"Result 2:\
 {TextProcessor().format_output('Hello World !')}")
    print(f"Result 3:\
 {LogProcessor().format_output('INFO: level detected: System ready')}")
    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    class_tester()
