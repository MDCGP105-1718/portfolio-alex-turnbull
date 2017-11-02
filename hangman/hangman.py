# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    wordGuessed = True
    for char in secret_word:
        if char not in letters_guessed:
            wordGuessed = False

    return wordGuessed


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    progress = []
    for i in range(len(secret_word)):
        progress += "_"

    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            progress[i] = secret_word[i]

    wordRemaining = ' '.join(progress)

    return wordRemaining


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    fullList = []
    allCharacters = string.ascii_lowercase
    for char in allCharacters:
        fullList.append(char)

    for e in letters_guessed:
        if e in fullList:
            fullList.remove(e)

    listOfChars = ' '.join(fullList)
    return listOfChars


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game Hangman!")
    print("I am thinkin of a word that is",len(secret_word),"letters long.")
    print("-------------")
    numberOfGuesses = 6
    guessedCorrectly = is_word_guessed
    letters_guess = []
    while not is_word_guessed:
        print("You have",numberOfGuesses,"guesses left.")
        print("Available letters:",get_available_letters)
        userGuess = str(input("Please guess a letter: "))
        if userGuess in secret_word:
            print("Good guess: ")




secret_word = choose_word(wordlist)
hangman(secret_word)
