def readFile(Filename: str) -> str: 
    filehandler = open(Filename, 'r', encoding ="utf-8")
    content= ''
    Row = filehandler.readline()
    while Row != '':
        content += Row
        Row = filehandler.readline()
    filehandler.close()
    return content

def main():
    print("program starting.")
    print("This program can read a file.")
    Filename =input("Insert filename: ")
    filecontent = readFile (Filename)
    print(f"### START {Filename} ###")
    print(filecontent)
    print(f"#### END {Filename} ####")
    print("program ending.")
    return None
main()
