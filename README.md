# zero-knowledge-hangman
A hangman game where the program doesnt actually know the word

The idea of this is to make a hangman game that can be played fully clientside. There is no need for external server requests to hide what the word is rom the client, because the client doesnt know in the first place.

How this works is the `src/hasher.py` file can be run once to generate a hash list from a word list. Each line of the hash list is a string of multiple salt and hash pairs separated by vertical bars.

Each hash is the result of hashing the correct letter for that position in the word with the salt. This means that the program can validate if a guess is correct without actually knowing the answer. This means a malicious user trying to cheat cannot simply read the correct word from program memory

Of course a malicious user could still extract the hash list and brute force the answer (very quickly as hangman only has 26 letters to guess) but there is no way to stop this


# Usage - Playing

To play, you fist need a hashlist. If you do not have one, follow the hash generation instructions

Save your hashes file to `src/hashes`, This is the output of the hash generation script

run `python src/game.py` to play

You can either choose a word number or generate one at random

Have fun

# Usage - Hash generation

To generate the hashes list from a word list, place a file called 'words' in `src/` which contains a list of words, one per line

run `python src/hasher.py` to generate the hashes

