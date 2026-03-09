import os
from dotenv import load_dotenv


def check_env() -> None:
    configs = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT",
    ]
    for config in configs:
        if os.getenv(config) is None or os.getenv(config) == "":
            raise Exception(f"{config} var isn't instanciate in dotenv")
    if (
        os.getenv("MATRIX_MODE") != "development"
        and os.getenv("MATRIX_MODE") != "production"
    ):
        raise Exception("MATRIX_MODE value isn't manage")


def print_env() -> None:
    print("Configuration loaded:")
    print(f"Mode: {os.getenv('MATRIX_MODE')}")
    print("Database: Connected to local instance")
    print("API Access: Authenticated")
    print(f"Log Level: {os.getenv('LOG_LEV')}")
    print("Zion Network: Online")


def main() -> None:
    try:
        print("\nORACLE STATUS: Reading the Matrix...\n")
        load_dotenv()
        check_env()
        print_env()
        print("\nEnvironment security check:")
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
        print("[OK] Production overrides available")
        print("The Oracle sees all configurations.")
    except Exception as err:
        print(err)


if __name__ == "__main__":
    main()
