def main() -> None:
    print("Program starting.")
    first_name: str = input("Insert first name: ")
    last_name: str = input("Insert last name: ")
    filename: str = input("Insert filename: ")
    with open(filename, "w", encoding="utf-8") as file:
        file.write(first_name + "\n")
        file.write(last_name + "\n")
    print("Program ending.")


if __name__ == "__main__":
    main()