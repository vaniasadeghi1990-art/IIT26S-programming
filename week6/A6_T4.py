def read_file(filename: str) -> str:
    file = open(filename, "r", encoding="utf-8")
    content: str = ""
    while True:
        line = file.readline()
        if len(line) == 0:
            break
        content += line
    file.close()
    return content


def write_file(filename: str, content: str) -> None:
    file = open(filename, "w", encoding="utf-8")
    file.write(content)
    file.close()


def main() -> None:
    print("Program starting.")
    print("This program can copy a file.")
    source: str = input("Insert source filename: ")
    destination: str = input("Insert destination filename: ")

    print("Reading file '{0:s}' content.".format(source))
    content: str = read_file(source)
    print("File content ready in memory.")

    print("Writing content into file '{0:s}'.".format(destination))
    write_file(destination, content)
    print("Copying operation complete.")
    print("Program ending.")


main()