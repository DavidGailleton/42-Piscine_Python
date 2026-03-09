import datetime
from typing import Optional
from pydantic import BaseModel, Field, ValidationError

SPACE_STATIONS = [
    {
        "station_id": "LGW125",
        "name": "Titan Mining Outpost",
        "crew_size": 6,
        "power_level": 76.4,
        "oxygen_level": 95.5,
        "last_maintenance": "2023-07-11T00:00:00",
        "is_operational": True,
        "notes": None,
    },
    {
        "station_id": "QCH189",
        "name": "Deep Space Observatory",
        "crew_size": 3,
        "power_level": 70.8,
        "oxygen_level": 88.1,
        "last_maintenance": "2023-08-24T00:00:00",
        "is_operational": False,
        "notes": "System diagnostics required",
    },
    {
        "station_id": "ISS674",
        "name": "Europa Research Station",
        "crew_size": 11,
        "power_level": 82.0,
        "oxygen_level": 91.4,
        "last_maintenance": "2023-10-21T00:00:00",
        "is_operational": True,
        "notes": None,
    },
    {
        "station_id": "ISS877",
        "name": "Mars Orbital Platform",
        "crew_size": 9,
        "power_level": 79.7,
        "oxygen_level": 87.2,
        "last_maintenance": "2023-10-06T00:00:00",
        "is_operational": False,
        "notes": "System diagnostics required",
    },
    {
        "station_id": "LGW194",
        "name": "Deep Space Observatory",
        "crew_size": 4,
        "power_level": 80.2,
        "oxygen_level": 89.9,
        "last_maintenance": "2023-10-25T00:00:00",
        "is_operational": False,
        "notes": "System diagnostics required",
    },
    {
        "station_id": "ISS847",
        "name": "Solar Wind Monitor",
        "crew_size": 11,
        "power_level": 73.6,
        "oxygen_level": 98.1,
        "last_maintenance": "2023-12-11T00:00:00",
        "is_operational": False,
        "notes": "System diagnostics required",
    },
    {
        "station_id": "QCH400",
        "name": "Asteroid Belt Relay",
        "crew_size": 12,
        "power_level": 75.5,
        "oxygen_level": 86.0,
        "last_maintenance": "2023-07-15T00:00:00",
        "is_operational": False,
        "notes": "System diagnostics required",
    },
    {
        "station_id": "ERS891",
        "name": "Titan Mining Outpost",
        "crew_size": 4,
        "power_level": 94.4,
        "oxygen_level": 97.3,
        "last_maintenance": "2023-09-25T00:00:00",
        "is_operational": True,
        "notes": "All systems nominal",
    },
    {
        "station_id": "ABR266",
        "name": "Asteroid Belt Relay",
        "crew_size": 8,
        "power_level": 76.0,
        "oxygen_level": 88.8,
        "last_maintenance": "2023-07-10T00:00:00",
        "is_operational": False,
        "notes": "System diagnostics required",
    },
    {
        "station_id": "LGW723",
        "name": "Mars Orbital Platform",
        "crew_size": 11,
        "power_level": 90.8,
        "oxygen_level": 87.3,
        "last_maintenance": "2023-09-25T00:00:00",
        "is_operational": False,
        "notes": "System diagnostics required",
    },
]


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
        valid_station = {
            "station_id": "ISS001",
            "name": "International Space Station",
            "crew_size": 6,
            "power_level": 85.5,
            "oxygen_level": 92.3,
            "last_maintenance": "2023-09-25T00:00:00",
        }

        invalid_station = {
            "station_id": "ISS001",
            "name": "International Space Station",
            "crew_size": 26,
            "power_level": 85.5,
            "oxygen_level": 92.3,
            "last_maintenance": "2023-09-25T00:00:00",
        }

        try:
            print("\nValid station:n\n")
            ss = SpaceStation(**valid_station)
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
            print(err)

        try:
            print("\nInvalid station:\n")
            ss = SpaceStation(**invalid_station)
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
            print(err)

        print("\nBatch stations:\n")
        for station in SPACE_STATIONS:
            try:
                ss = SpaceStation(**station)
                print("========================================")
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
            except ValidationError as e:
                print(e.errors())
    except Exception as err:
        print(err)


if __name__ == "__main__":
    main()
