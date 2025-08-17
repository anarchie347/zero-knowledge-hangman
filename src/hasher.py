import secrets, hashlib

WORDS_PATH = "words"
HASHES_PATH = "hashes"
SALT_LEN = 64


def saltAndHash(val):
    encoded = val.lower().encode()
    salt = secrets.token_urlsafe(SALT_LEN)
    hexdigest = hashlib.sha512(encoded + salt.encode()).hexdigest()
    return f"{hexdigest},{salt}"

def hashWord(word):
    return "|".join([ saltAndHash(letter) for letter in word])
    
def countWordsLen():
    with open(WORDS_PATH, "r") as file:
       for i,_ in enumerate(file):
           pass
    return i + 1



def main():
    with open(WORDS_PATH, "r") as wordList:
        wordCount = countWordsLen()
        with open(HASHES_PATH, "w") as hashList:
            hashList.write(f"{wordCount}\n")
            for line in wordList:
                hashList.write(hashWord(line.strip()) + "\n")




if __name__ == "__main__":
    main()
