LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def rot13(text: str) -> str:
    result: str = ""
    for char in text:
        if char in LOWER_ALPHABETS:
            index = LOWER_ALPHABETS.find(char)
            result += LOWER_ALPHABETS[(index + 13) % 26]
        elif char in UPPER_ALPHABETS:
            index = UPPER_ALPHABETS.find(char)
            result += UPPER_ALPHABETS[(index + 13) % 26]
        else:
            result += char
    return result


def collect_rows() -> str:
    print("Collecting plain text rows for ciphering.")
    text: str = ""
    while True:
        row = input("Insert row(empty stops): ")
        if len(row) == 0:
            break
        text += row + "\n"
    return text


def show_text(ciphered: str) -> None:
    print()
    print("#### Ciphered text ####")
    print(ciphered)
    print("#### Ciphered text ####")


def save_text(ciphered: str) -> None:
    filename: str = input("Insert filename to save: ")
    file = open(filename, "w", encoding="utf-8")
    file.write(ciphered)
    file.close()
    print("Ciphered text saved!")


def main() -> None:
    print("Program starting.")
    print()
    plain: str = collect_rows()
    ciphered: str = rot13(plain)
    choice: str = input("Show (s) or save (f) the ciphered text? ").strip().lower()
    if choice == "s":
        show_text(ciphered)
    else:
        save_text(ciphered)
    print("Program ending.")


main()