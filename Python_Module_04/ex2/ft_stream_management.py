import sys
import typing


def edit(filename: str, content: str) -> None:
    print("Transform data:")
    content = content.replace("\r\n", "\n")
    lines = content.split("\n")
    if lines[-1] == "":
        lines.pop()
    new_lines = [line + "#" for line in lines]

    print("---")
    for line in new_lines:
        print(line)
    print("---")

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    save_as = sys.stdin.readline().strip()

    if save_as == "":
        print("Not saving data.")
        return

    try:
        print(f"Saving data to '{save_as}'")
        out: typing.IO[str] = open(save_as, "w")
        out.write("\n".join(new_lines) + "\n")
        out.close()
        print(f"Data saved in file '{save_as}'.")
    except OSError as e:
        print(f"[STDERR] Error opening file '{save_as}': {e}",
              file=sys.stderr)
        print("Data not saved.")


def recover(filename: str) -> None:
    try:
        f: typing.IO[str] = open(filename, "r")
        content = f.read()
        print("---\n")
        print(content, end="" if content.endswith("\n") else "\n")
        print("\n---")
        f.close()
        print(f"File '{filename}' closed.")
        edit(filename, content)
    except OSError as e:
        print(f"[STDERR] Error opening file '{filename}': {e}",
              file=sys.stderr)


def main() -> None:
    argc = len(sys.argv)
    if argc != 2:
        print("Usage: ft_stream_management.py <file>")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{sys.argv[1]}'")
        recover(sys.argv[1])


if __name__ == "__main__":
    main()