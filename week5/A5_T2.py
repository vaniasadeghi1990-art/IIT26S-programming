def frameWord(PWord: str) -> None:
    print("*" * (len(PWord) + 4))
    print("* " + PWord + " *")
    print("*" * (len(PWord) + 4))


def main() -> None:
    print("Program starting.")
    print("Insert word: ", end="")
    word = input()

    print()
    frameWord(word)

    print()
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()