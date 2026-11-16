import importlib
import importlib.metadata
import sys

REAGENTS = {
    "pandas": "Data manipulation",
    "numpy": "Numerical computation",
}


def main():
    print("REAGENT STATUS: Loading reagents...\n")
    print("Checking dependencies:")
    missing = []
    for name, purpose in REAGENTS.items():
        try:
            importlib.import_module(name)
            version = importlib.metadata.version(name)
            print(f"[OK] {name} ({version}) - {purpose} ready")
        except Exception:
            print(f"[MISSING] {name} - {purpose} unavailable")
            missing.append(name)

    print("\npip vs Poetry:")
    print(
        "requirements.txt declares what to install; "
        "pip resolves it at install time."
    )
    print(
        "pyproject.toml declares the same constraints, "
        "and Poetry pins the resolved"
    )
    print("versions in poetry.lock so every install is identical.")

    if missing:
        print(f"\nMissing reagents: {', '.join(missing)}")
        print("Install with pip:    pip install -r ex0/requirements.txt")
        print("Install with Poetry: poetry install")
        return 1

    print("\nAll reagents present and accounted for.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
