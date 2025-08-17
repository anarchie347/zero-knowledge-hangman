


        
def getWordHashesFromNumber():
    pass

def getWordNumber():
    print("Enter a number or leave blank to choose a random one:")
    numStr = input()
    while not numStr.isdecimal():
        print("Enter a non-negative integer")
        numStr = input()
    num = int(numStr)
    return num

def main():
    print("Welcome to Zero Knowledge Hangman")
    print(getWordNumber())



if __name__ == "__main__":
    main()
