LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def askRow() -> str:
    rows= []
    print("In the row asking function.")
    while True:
        row = input ("Insert row(empty stop): ")
        if row == '':
            break
        rows.append(row)
    print ("In the row asking function")
    return '\n'.join(rows)

def row13(Content : str )-> str:
    NewContent = ""
    shift = 13
    for Character in LOWER_ALPHABETS:
        if Character in LOWER_ALPHABETS:
            NewContent += shiftCharacter(Character, LOWER_ALPHABETS ,shift)
        elif Character in UPPER_ALPHABETS:
            NewContent += shiftCharacter(Character, UPPER_ALPHABETS ,shift)
        else:
            NewContent += shiftCharacter(Character,UPPER_ALPHABETS ,shift)

    return NewContent

def shiftCharacter(Character:str, Alphabets: str , shift : int) ->str :
    if Character in Alphabets:
        index = Alphabets.index (Character)
        shifted_index = (index = shift)% len(Alphabets)
        return Alphabets[shifted_index]
    return Character
def writeFile(Filename, Content) -> None :
    with open (Filename, 'w', encoding='utf-8') as file:
        file.write(Content)
        file.close()

def main() -> None :
    print("Program starting.")
    Rows = askRow()
    CipherdText = row13(Rows)
    print(CipherdText)
    print("##### Chipher text ###")
    Filename = input("insert filename to save: ")
    writeFile(Filename, CipherdText)
    print(Rows)
    print("Program ending")
    return None

main()