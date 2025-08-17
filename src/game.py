import hashlib
HASHES_FILE_PATH = "hashes"

def printGuessed(guessed):
    print(" ".join(guessed))

def isWon(guessed):
    return not any(map(lambda c : c == "_", guessed))

def makeGuess(hashes, guessed, letter):
    correct = False
    for i,[h,s] in enumerate(hashes):
        generatedHash = hashlib.sha512(letter.encode() + s.encode()).hexdigest()
        if generatedHash == h:
            guessed[i] = letter
            correct = True
    return correct


def play(hashes):
    remainingGuesses = 8
    wordLen = len(hashes)
    guessed = ["_"] * wordLen
    print("Start guessing letters")
    print(f"You have {remainingGuesses} wrong guesses left")
    while (not isWon(guessed)) and remainingGuesses > 0:
        printGuessed(guessed)
        guesses = input()
        for g in guesses:
            correct = makeGuess(hashes,guessed,g)
            if correct:
                print(f"'{g}' was correct!")
            else:
                remainingGuesses -= 1
                print(f"'{g}' was wrong!")
                print(f"You have {remainingGuesses} wrong guesses left")
    if remainingGuesses > 0:
        print("Correct!")
        print(f"You still had {remainingGuesses} wrong guesses left")
        print("The word was " + "".join(guessed))
    else:
        print("Failed!")
        print("I cant tell you the answer because I don't know either")


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
    play(hashes)


if __name__ == "__main__":
    main()
