
HASHES_FILE_PATH = "hashes"

# returns a 2d array, first index represents letter index, which each contains [salt, hash]
def parseLine(line):
    components = line.split("|")
    return [c.split(",") for c in components]
    
# gets parsed hashes for a given word number
def getWordHashesFromNumber(num):
    with open(HASHES_FILE_PATH) as file:
        for i,line in enumerate(file):
            if (i == 0):
                lineCount = int(line)
                num = num % lineCount
            if i == num:
                return parseLine(line.strip())

def getWordNumber():
    print("Enter a number or leave blank to choose a random one:")
    numStr = input()
    while (not numStr.isdecimal()) or int(numStr) == 0:
        print("Enter a positive integer")
        numStr = input()
    num = int(numStr)
    return num

def main():
    print("Welcome to Zero Knowledge Hangman")
    num = getWordNumber()
    hashes = getWordHashesFromNumber(num)
    print(hashes)


if __name__ == "__main__":
    main()
