from abc import ABC
from typing import Any, List, Protocol, Union
from typing_extensions import override


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        pass


class InputStage:
    def process(self, data: Any) -> Dict:
        pass


class TransformStage:
    def process(self, data: Any) -> Dict:
        pass


class OutputStage:
    def process(self, data: Any) -> str:
        pass


class ProcessingPipeline(ABC):
    def __init__(self) -> None:
        self.stages: List[InputStage | TransformStage | OutputStage] = []

    def add_stage(
        self, stage: Union[InputStage, TransformStage, OutputStage]
    ) -> None:
        pass

    def process(self, data: Any) -> Any:
        pass


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id
        super().__init__()

    @override
    def process(self, data: Any) -> Any:
        return super().process(data)


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id
        super().__init__()

    @override
    def process(self, data: Any) -> Any:
        return super().process(data)


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id
        super().__init__()

    @override
    def process(self, data: Any) -> Any:
        return super().process(data)


def tester():
    pass


if __name__ == "__main__":
    pass
