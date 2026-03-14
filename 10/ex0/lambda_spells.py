def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    try:
        return sorted(artifacts, key=lambda artifact: artifact["power"])
    except KeyError as err:
        print(err)
        return artifacts


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    try:
        return list(filter(lambda x: x["power"] >= min_power, mages))
    except KeyError as err:
        print(err)
        return mages


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: "* " + x + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    try:
        max_power = max(mages, key=lambda mage: mage["power"])
        min_power = min(mages, key=lambda mage: mage["power"])
        avg_power = sum(map(lambda mage: mage["power"], mages)) / len(mages)
        return {
            "max_power": max_power["power"],
            "min_power": min_power["power"],
            "avg_power": round(avg_power, 2),
        }
    except Exception:
        return {
            "max_power": 0,
            "min_power": 0,
            "avg_power": 0,
        }


def main() -> None:
    try:
        artifacts = [
            {"power": 30},
            {"power": 10},
            {"power": 300},
            {"power": 400},
            {"power": 200},
            {"power": 3},
            {"power": 10},
        ]
        str_list = [
            "Hello",
            "World",
            "Lorem",
            "ipsum",
        ]

        print("=== artifact_sorter ===")
        print(f"Sorted artifacts: {artifact_sorter(artifacts)}")

        print("\n=== power_filter ===")
        print(f"Filtered artifacts: {power_filter(artifacts, 100)}")

        print("\n=== spell_transformer ===")
        print(f"Transformed str: {spell_transformer(str_list)}")

        print("\n=== mage_stats ===")
        print(f"Get power info: {mage_stats(artifacts)}")
    except Exception as err:
        print(err)


if __name__ == "__main__":
    main()
