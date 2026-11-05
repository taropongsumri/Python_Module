import sys
import typing

def splitlines(text):
    lines = []
    current = ""
    i = 0
    while i < len(text):
        ch = text[i]
        if ch == "\r":
            lines.append(current)
            current = ""
            if i + 1 < len(text) and text[i + 1] == "\n":
                i += 1
        elif ch == "\n":
            lines.append(current)
            current = ""
        else:
            current += ch
        i += 1
    if current:
        lines.append(current)
    return lines

def edit(filename: str, content: str) -> None:
    print("Transform data:")
    lines = splitlines(content)
    new_lines = [line + "#" for line in lines]
    print("---\n")
    for line in new_lines:
        print(line)
    print("\n---")

    try:
        save_as = input("Enter new file name (or empty): ").strip()
    except EOFError:
        save_as = ""

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
        print(f"Error saving file '{save_as}': {e}")

def recover(filename: str) -> None:
    try:
        f: typing.IO[str] = open(filename, "r")
        content = f.read()
        print(f"---\n\n{content}\n\n---")
        f.close()
        print(f"File '{filename}' closed.")
        edit(filename, content)
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")


def main() -> None:
    argc = len(sys.argv)
    if argc != 2:
        print("Usage: ft_archive_creation.py <file>")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{sys.argv[1]}'")
        recover(sys.argv[1])


if __name__ == "__main__":
    main()
