from abc import ABC, abstractmethod
from re import error
import re
from typing import Any, List, Optional, Dict, Union
from typing_extensions import override


class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str) -> None:
        self.stream_id = stream_id
        self.stream_type = stream_type
        self.data_batch: List[str] = []

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        res = []
        for data in data_batch:
            if data.split(":", 1)[0] in criteria:
                res += [data]
        return res

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "nb_process": len(self.data_batch),
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str, stream_type: str) -> None:
        super().__init__(stream_id, stream_type)

    def process_batch(self, data_batch: List[Any]) -> str:
        res: List[str] = []
        for data in data_batch:
            try:
                if len(data.split(":", 1)) == 2:
                    if data.split(":", 1)[0] == "temp":
                        float(data.split(":", 1)[1])
                    elif (
                        data.split(":", 1)[0] == "humidity"
                        or data.split(":", 1)[0] == "pressure"
                    ):
                        int(data.split(":", 1)[1])
                    else:
                        continue
                    res += [data]
            except Exception:
                continue
        self.data_batch += res
        return f"{res}"

    @override
    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        return super().filter_data(data_batch, criteria)

    @override
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        temp_data: List[float] = []
        for temp in self.filter_data(self.data_batch, "temp"):
            temp_data += [float(temp.split(":", 1)[1])]
        res: Dict[str, Union[str, int, float]] = {}
        res["nb_process"] = len(self.data_batch)
        res["avg_temp"] = sum(temp_data) / len(temp_data)
        return res


class TransactionStream(DataStream):
    def __init__(self, stream_id: str, stream_type: str) -> None:
        super().__init__(stream_id, stream_type)

    def process_batch(self, data_batch: List[Any]) -> str:
        res: List[str] = []
        for data in data_batch:
            try:
                if len(data.split(":", 1)) == 2:
                    if (
                        data.split(":", 1)[0] == "buy"
                        or data.split(":", 1)[0] == "sell"
                    ):
                        int(data.split(":", 1)[1])
                    else:
                        continue
                    res += [data]
            except Exception:
                continue
        self.data_batch += res
        return f"{res}"

    @override
    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        res: List[Any] = []
        if criteria and ">" == criteria[0]:
            try:
                higher_than = int(criteria.split(">")[1])
                for data in data_batch:
                    if int(data.split(":", 1)[1]) > higher_than:
                        res += [data]
            except Exception as err:
                print(err)
            return res
        else:
            return super().filter_data(data_batch, criteria)

    @override
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        net_flow = 0
        for data in self.data_batch:
            if data.split(":", 1)[0] == "buy":
                net_flow += int(data.split(":", 1)[1])
            else:
                net_flow -= int(data.split(":", 1)[1])
        res: Dict[str, Union[str, int, float]] = {}
        res["nb_process"] = len(self.data_batch)
        res["net_flow"] = net_flow
        return res


class EventStream(DataStream):
    def __init__(self, stream_id: str, stream_type: str) -> None:
        super().__init__(stream_id, stream_type)

    def process_batch(self, data_batch: List[Any]) -> str:
        res: List[str] = []
        for data in data_batch:
            try:
                if data not in ["login", "logout", "error"]:
                    continue
                res += [data]
            except Exception:
                continue
        self.data_batch += res
        return f"{res}"

    @override
    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        return super().filter_data(data_batch, criteria)

    @override
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        nb_error = 0
        for data in self.data_batch:
            if data == "error":
                nb_error += 1
        res: Dict[str, Union[str, int, float]] = {}
        res["nb_process"] = len(self.data_batch)
        res["nb_error"] = nb_error
        return res


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: Dict[
            str, List[Union[SensorStream, TransactionStream, EventStream]]
        ] = {"sensor": [], "transaction": [], "event": []}

    def process_batch(
        self,
        data_batch: List[Any],
        stream: Union[SensorStream, TransactionStream, EventStream],
    ) -> Union[SensorStream, TransactionStream, EventStream]:
        try:
            stream.process_batch(data_batch)
            if isinstance(stream, SensorStream):
                self.streams["sensor"] += [stream]
            elif isinstance(stream, TransactionStream):
                self.streams["transaction"] += [stream]
            elif isinstance(stream, EventStream):
                self.streams["event"] += [stream]
        except Exception as err:
            print(err)
        return stream

    def get_stats(
        self, stream: Union[SensorStream, TransactionStream, EventStream]
    ) -> Dict[str, Union[str, int, float]]:
        return stream.get_stats()

    def get_high_priority(
        self,
    ) -> Dict[str, int]:
        res: Dict[str, int] = {}
        for stream in self.streams["transaction"]:
            try:
                res["large transaction"] = len(
                    stream.filter_data(stream.data_batch, ">100")
                )
            except Exception:
                print("Error on catching large transaction")
                continue
        for stream in self.streams["event"]:
            res["error detected"] = len(
                stream.filter_data(stream.data_batch, "error")
            )
        return res


def data_stream_tester():
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    sensor_stream = SensorStream("SENSOR_001", "Environmental Data")
    print(f"Stream ID: {sensor_stream.stream_id},\
 Type: {sensor_stream.stream_type}")
    print(f"Processing sensor batch:\
 {sensor_stream.process_batch(['temp:22.5', 'humidity:65', 'pressure:1013'])}")
    sensor_analysis = sensor_stream.get_stats()
    print(f"Sensor analysis: {sensor_analysis['nb_process']} reading\
 process, avg temp: {sensor_analysis['avg_temp']}°C")
    print()
    transaction_stream = TransactionStream("TRANS_001", "Financial Data")
    print(f"Stream ID: {transaction_stream.stream_id},\
 Type: {transaction_stream.stream_type}")
    print(f"Processing transaction batch:\
 {transaction_stream.process_batch(['buy:100', 'sell:150', 'buy:75'])}")
    transaction_analysis = transaction_stream.get_stats()
    print(f"Transaction analysis: {transaction_analysis['nb_process']}\
 operations, net flow: {transaction_analysis['net_flow']} units")
    print()
    event_stream = EventStream("EVENT_001", "System Events")
    print(f"Stream ID: {event_stream.stream_id},\
 Type: {event_stream.stream_type}")
    print(f"Processing event batch:\
 {event_stream.process_batch(['login', 'error', 'logout'])}")
    event_analysis = event_stream.get_stats()
    print(f"Sensor analysis: {event_analysis['nb_process']}\
 events, {event_analysis['nb_error']} error detected")


def stream_processor_tester():
    print("=== Polymorphic Stream Processing ===\n")
    processor = StreamProcessor()
    data_batch = [
        ["temp:22.5", "humidity:65", "pressure:1013"],
        ["buy:100", "sell:150"],
        ["login", "error", "logout", "login", "error"],
    ]
    streams = [
        SensorStream("SENSOR_001", "Environmental Data"),
        TransactionStream("TRANS_001", "Financial Data"),
        EventStream("EVENT_001", "System Events"),
    ]
    for i in range(0, len(data_batch)):
        streams[i] = processor.process_batch(data_batch[i], streams[i])
    print("Batch 1 results:")
    for stream in streams:
        stat = stream.get_stats()
        print(f"- {stream.stream_id}: {stat['nb_process']}")
    print("\nHigh priority data:")
    hp_data = processor.get_high_priority()
    for data in hp_data:
        print(f"- {hp_data[data]} {data}")


if __name__ == "__main__":
    data_stream_tester()
    stream_processor_tester()
