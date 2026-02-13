from abc import ABC
from typing import Any, Dict, List, Protocol, Union
from typing_extensions import override


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        pass


class InputStage:
    def process(self, data: Any) -> Dict[int, float]:
        res: Dict[int, float] = {}
        i = 0
        for n in data:
            try:
                if not isinstance(n, float):
                    n = float(n)
                res[i] = n
                i += 1
            except ValueError:
                continue
        return res


class TransformStage:
    def process(self, data: Any) -> Dict[str, float]:
        res: Dict[str, Union[int, float]] = {}
        res["processed_data"] = len(data)
        try:
            res["avg"] = sum(data.values()) / len(data)
        except ZeroDivisionError:
            res["avg"] = 0
        return res


class OutputStage:
    def process(self, data: Any) -> str:
        return f"Summary:\n\t\
- Processed_data: {data['processed_data']}\n\t- avg temp: {data['avg']:.1f}°C"


class ProcessingPipeline(ABC):
    def __init__(self) -> None:
        self.stages: List[InputStage | TransformStage | OutputStage] = []

    def add_stage(
        self, stage: Union[InputStage, TransformStage, OutputStage]
    ) -> None:
        self.stages += [stage]

    def process(self, data: Any) -> Any:
        for stage in self.stages:
            data = stage.process(data)
        return data


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id
        super().__init__()

    @override
    def process(self, data: Any) -> Any:
        res: List[Any] = []
        for n in data:
            res += [data[n]]
        return super().process(res)


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id
        super().__init__()

    @override
    def process(self, data: Any) -> Any:
        return super().process(data.split(","))


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id
        super().__init__()

    @override
    def process(self, data: Any) -> Any:
        if not isinstance(data, List):
            raise Exception
        return super().process(data)


class NexusManager:
    def __init__(self, pipelines: List[ProcessingPipeline]) -> None:
        self.pipelines: List[ProcessingPipeline] = pipelines

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines += [pipeline]

    def process_data(self, data: Any) -> str:
        res: str | None = None
        for pipeline in self.pipelines:
            pipeline.add_stage(InputStage())
            pipeline.add_stage(TransformStage())
            pipeline.add_stage(OutputStage())
            try:
                res = pipeline.process(data)
                break
            except Exception:
                continue
        if res is None:
            return "[ERROR] Unknown format, incompatible with pipelines"
        return res


def tester() -> None:
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")
    print("Initializing Nexus Manager...")
    manager = NexusManager(
        [
            JSONAdapter("JSON_01"),
            CSVAdapter("CSV_01"),
            StreamAdapter("Stream_01"),
        ]
    )
    print("\n=== test JSONAdapter ===")
    data: Any = {"temp": 10, "est": "10.3", "t": 10.6, "p": "Hello"}
    print(f"input: {data}")
    res = manager.process_data(data)
    print(f"Output: {res}\n")
    print("\n=== test CSVAdapter ===")
    data = "10,20,40,30"
    print(f'input: "{data}"')
    res = manager.process_data(data)
    print(f"Output: {res}\n")
    print("\n=== test StreamAdapter ===")
    data = [10, 30, 0, "100"]
    print(f"input: {data}")
    res = manager.process_data(data)
    print(f"Output: {res}\n")
    print("\n=== test Invalid input ===")
    data = 10
    print(f"input: {data}")
    res = manager.process_data(data)
    print(f"Output: {res}\n")


if __name__ == "__main__":
    tester()
