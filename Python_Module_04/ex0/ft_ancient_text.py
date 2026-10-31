import sys
import typing


def recover(filename: str) -> None:
    try:
        f: typing.IO[str] = open(filename, "r")
        content = f.read()
        print(f"---\n\n{content}\n\n---")
        f.close()
        print(f"File '{filename}' closed.")
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")


def main() -> None:
    argc = len(sys.argv)
    if argc != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{sys.argv[1]}'")
        recover(sys.argv[1])


if __name__ == "__main__":
    main()
