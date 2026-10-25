DELIMITER = ","
def collectWords() -> str:
    Words = ""

    while True:
        Word = input("Insert word(empty stops): ")

        if Word == "":
            break

        if Words == "":
            Words = Word
        else:
            Words = Words + DELIMITER + Word

        print()

    return Words


def analyseWords(PWords: str) -> None:
    if PWords == "":
        WordCount = 0
        CharacterCount = 0
        Average = 0.0
    else:
        WordList = PWords.split(DELIMITER)

        WordCount = len(WordList)
        CharacterCount = 0

        for Word in WordList:
            CharacterCount = CharacterCount + len(Word)

        Average = CharacterCount / WordCount

    print(f"- {WordCount} Words")
    print(f"- {CharacterCount} Characters")
    print("- {:.2f} Average word length".format(Average))


def main() -> None:
    print("Program starting.")

    Words = collectWords()
    analyseWords(Words)

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
