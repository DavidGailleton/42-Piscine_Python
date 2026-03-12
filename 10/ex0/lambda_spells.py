def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda artifact: artifact["power"])


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    pass


def mage_stats(mages: list[dict]) -> dict:
    pass
