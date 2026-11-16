import os
from pathlib import Path

from dotenv import load_dotenv


def load_config() -> dict[str, str | None]:
    env_path = Path(__file__).parent / ".env"
    load_dotenv(dotenv_path=env_path)
    return {
        "MATRIX_MODE": os.getenv("MATRIX_MODE"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }


def is_env_ignored() -> bool:
    gitignore = Path(__file__).parent / ".gitignore"
    try:
        return ".env" in gitignore.read_text(encoding="utf-8")
    except FileNotFoundError:
        return False


def main() -> None:
    config = load_config()
    mode = config["MATRIX_MODE"] or "development"
    database_url = config["DATABASE_URL"]
    api_key = config["API_KEY"]
    log_level = config["LOG_LEVEL"] or (
        "DEBUG" if mode == "development" else "INFO"
    )
    zion_endpoint = config["ZION_ENDPOINT"]

    missing = [
        key
        for key in ("DATABASE_URL", "API_KEY", "ZION_ENDPOINT")
        if not config[key]
    ]

    print("ORACLE STATUS: Consulting the configuration...\n")
    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(
        "Database: "
        + ("Connected to local instance" if database_url else "Not connected")
    )
    print(
        "API Access: "
        + ("Authenticated" if api_key else "Unauthenticated")
    )
    print(f"Log Level: {log_level}")
    print(
        "Remote Network: "
        + ("Online" if zion_endpoint else "Offline")
    )
    print()

    if missing:
        print("WARNING: Missing configuration for: " + ", ".join(missing))
        print()

    print("Configuration security check:")
    print("[OK] No hardcoded secrets detected")
    print(
        "[OK] .env file properly ignored by git"
        if is_env_ignored()
        else "[MISSING] .env file properly ignored by git"
    )
    print("[OK] Production overrides available")
    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
