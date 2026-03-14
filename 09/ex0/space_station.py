import datetime
from pydantic import BaseModel, Field, ValidationError
from json import load


class SpaceStation(BaseModel):
    station_id: str = Field(max_length=10, min_length=3)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(le=20, ge=1)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime.datetime
    is_operational: bool = Field(default=True)
    notes: str | None = Field(default=None, max_length=200)


def main() -> None:
    try:
        with open("../generated_data/space_stations.json") as valids, open(
            "../generated_data/invalid_stations.json"
        ) as invalids:
            print("\ninvalid stations:\n")
            data = load(invalids)
            for station in data:
                try:
                    print("========================================")
                    ss = SpaceStation(**station)
                    print("Valid station created")
                    print(
                        f"ID: {ss.station_id}\n"
                        f"Name {ss.name}\n"
                        f"Crew: {ss.crew_size} people\n"
                        f"Power: {ss.power_level}%\n"
                        f"Oxygen: {ss.oxygen_level}%\n"
                        f"Status: {'operational' if ss.is_operational else 'not operational'}\n"
                        f"Note: {ss.notes}\n"
                    )
                except ValidationError as err:
                    print(err.errors()[0]["msg"])

            print("\nvalid stations:\n")
            data = load(valids)
            for station in data:
                try:
                    print("========================================")
                    ss = SpaceStation(**station)
                    print("Valid station created")
                    print(
                        f"ID: {ss.station_id}\n"
                        f"Name {ss.name}\n"
                        f"Crew: {ss.crew_size} people\n"
                        f"Power: {ss.power_level}%\n"
                        f"Oxygen: {ss.oxygen_level}%\n"
                        f"Status: {'operational' if ss.is_operational else 'not operational'}\n"
                        f"Note: {ss.notes}\n"
                    )
                except ValidationError as err:
                    print(err.errors()[0]["msg"])
    except Exception as err:
        print(err)


if __name__ == "__main__":
    main()
