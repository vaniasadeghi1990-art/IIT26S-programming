print("Program starting.")
print()

word_count = 0
char_count = 0

while True:
    word = input("Insert word (empty stops): ")
    if word == "":
        break
    word_count += 1
    char_count += len(word)

print()
print("You inserted:")
print(f"- {word_count} words")
print(f"- {char_count} characters")
print()
print("Program ending.")