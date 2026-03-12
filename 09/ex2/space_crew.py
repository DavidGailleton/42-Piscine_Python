from enum import Enum
from typing_extensions import Self
from pydantic import BaseModel, Field, model_validator
from datetime import datetime
from json import load


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validation(self) -> Self:
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')
        try:
            crew = {member.rank: member for member in self.crew}
            crew[Rank.CAPTAIN]
            crew[Rank.COMMANDER]
        except KeyError:
            raise ValueError("Must have at least one Commander or Captain")
        if (
            self.duration_days > 365
            and len(
                [
                    member
                    for member in self.crew
                    if member.years_experience >= 5
                ]
            )
            < len(self.crew) / 2
        ):
            raise ValueError(
                "Long missions (> 365 days) need 50% "
                "experienced crew (5+ years)"
            )
        for member in self.crew:
            if member.is_active == False:
                raise ValueError("All crew members must be active")
        return self


def main() -> None:
    try:
        with open("../generated_data/space_missions.json") as file:
            data = load(file)
            for mission in data:
                try:
                    print("=========================================")
                    sp = SpaceMission(**mission)
                    print(
                        "Valid mission created:\n"
                        f"Mission: {sp.mission_name}\n"
                        f"ID: {sp.mission_id}\n"
                        f"Destination: {sp.destination}\n"
                        f"Duration: {sp.duration_days} days\n"
                        f"Budget: ${sp.budget_millions}M\n"
                        f"Crew size: {len(sp.crew)}\n"
                        "Crew members:"
                    )
                    for member in sp.crew:
                        print(
                            f"- {member.name} ({member.rank}) - "
                            f"{member.specialization}"
                        )
                except Exception as err:
                    print(err)
    except Exception as err:
        print(err)


if __name__ == "__main__":
    main()
