def secure_archive(filename: str, action: str = "read", content: str = "") -> tuple:
    try:
        if action == "read":
            with open(filename, "r") as f:
                return (True, f.read())
        elif action == "write":
            with open(filename, "w") as f:
                f.write(content)
            return (True, "Content successfully written to file")
        else:
            return (False, "Invalid action: use 'read' or 'write'")
    except Exception as e:
        return (False, str(e))
    

def main ():
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))

    print("Using 'secure_archive' to read from a regular file:")
    ok, data = secure_archive("ancient_fragment.txt")
    print((ok, data))

    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_fragment.txt", "write", data))


if __name__ == "__main__":
    main()