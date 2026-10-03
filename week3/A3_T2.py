print("Program starting.")
print("string comparisons")
first_word= input("Insert first word: ")
character= input("Insert a character: ")
if character in first_word:
    print("word "+'"'+ first_word +'"'+ " contains character "+'"'+ character +'"')
else:
    print("word "+'"'+ first_word +'"'+ " doesn't contain character "+'"'+ character +'"')
second_word= input("Insert second word: ")

if first_word < second_word:
    print(f'The first word "{first_word}" is before the second word "{second_word}" alphabetically.')
elif first_word > second_word:
    print(f'The second word "{second_word}" is before the first word "{first_word}" alphabetically.')
else:
    print(f'Both inserted words are the same alphabetically, "{first_word}" ')

print("Program ending.")