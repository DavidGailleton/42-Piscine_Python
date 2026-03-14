from typing_extensions import Self
import datetime
from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator
import json


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime.datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def format_validation(self) -> Self:
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC"')
        if (
            self.contact_type == ContactType.PHYSICAL
            and self.is_verified == False
        ):
            raise ValueError("Physical contact reports must be verified")
        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages"
            )
        return self


def main() -> None:
    try:
        with open("../generated_data/alien_contacts.json") as valids, open(
            "../generated_data/invalid_contacts.json"
        ) as invalids:
            print("=== invalids ===")
            data = json.load(invalids)
            for contact in data:
                try:
                    print("======================================\n")
                    ac = AlienContact(**contact)
                    print(
                        f"Valid contact report:\n"
                        f"ID: {ac.contact_id}\n"
                        f"Type: {ac.contact_type}\n"
                        f"Location: {ac.location}\n"
                        f"Signal: {ac.signal_strength:.1f}/10\n"
                        f"Duration: {ac.duration_minutes} minutes\n"
                        f"Witness: {ac.witness_count}\n"
                        f"Message: {ac.message_received}\n"
                        f"Is verified: {ac.is_verified}\n"
                    )
                except ValidationError as err:
                    print(err.errors()[0]["msg"])

            print("=== valids ===")
            data = json.load(valids)
            for contact in data:
                try:
                    print("======================================\n")
                    ac = AlienContact(**contact)
                    print(
                        f"Valid contact report:\n"
                        f"ID: {ac.contact_id}\n"
                        f"Type: {ac.contact_type}\n"
                        f"Location: {ac.location}\n"
                        f"Signal: {ac.signal_strength:.1f}/10\n"
                        f"Duration: {ac.duration_minutes} minutes\n"
                        f"Witness: {ac.witness_count}\n"
                        f"Message: {ac.message_received}\n"
                        f"Is verified: {ac.is_verified}\n"
                    )
                except ValidationError as err:
                    print(err.errors()[0]["msg"])
    except Exception as err:
        print(err)


if __name__ == "__main__":
    main()
