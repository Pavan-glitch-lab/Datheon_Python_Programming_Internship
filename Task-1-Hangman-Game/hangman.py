
import random

MAX_ATTEMPTS = 6

# Categorized words with hints
WORD_INFO = {
    "Programming": {
        "python": "A popular programming language",
        "algorithm": "Step-by-step instructions to solve a problem",
        "function": "A reusable block of code",
        "variable": "Stores data in a program",
        "database": "An organized collection of data",
        "software": "Programs used by a computer",
        "compiler": "Translates source code into machine code",
        "debugging": "Finding and fixing errors in code",
        "keyboard": "An input device used to type",
        "developer": "A person who creates software"
    },
    "Computers": {
        "monitor": "Displays information on a screen",
        "processor": "Often called the brain of a computer",
        "hardware": "The physical parts of a computer",
        "internet": "A worldwide network of connected computers",
        "network": "Connected devices that share information",
        "memory": "Stores data and instructions",
        "printer": "Produces a paper copy of a document",
        "browser": "An application used to visit websites"
    },
    "Science": {
        "gravity": "The force that attracts objects toward each other",
        "planet": "A large object that orbits a star",
        "energy": "The ability to do work",
        "oxygen": "A gas humans need to breathe",
        "electricity": "Powers many devices and appliances",
        "chemical": "A substance with a particular composition"
    },
    "Everyday English": {
        "journey": "The act of travelling from one place to another",
        "library": "A place where you can borrow books",
        "village": "A small community in the countryside",
        "weather": "The condition of the atmosphere",
        "picture": "An image or photograph",
        "holiday": "A day of celebration or time away from work",
        "friend": "Someone you know and like",
        "language": "A system people use to communicate"
    }
}

STAGES = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]


def load_words():
    words = set()

    # Add categorized words and their hints
    for category in WORD_INFO:
        words.update(WORD_INFO[category].keys())

    # Add words from the external word list
    try:
        with open("words.txt", "r", encoding="utf-8") as file:
            for line in file:
                word = line.strip().lower()

                if word.isalpha() and len(word) >= 4:
                    words.add(word)

    except FileNotFoundError:
        print("words.txt not found. Using built-in words.")

    return sorted(words)


def get_word_details(secret_word):
    for category, word_dictionary in WORD_INFO.items():
        if secret_word in word_dictionary:
            return category, word_dictionary[secret_word]

    # Fallback for words not in the categorized dictionary
    return "English Vocabulary", (
        f"This word contains {len(secret_word)} letters. "
        "Guess the hidden English word."
    )


def play_game():
    print("\n===== HANGMAN GAME =====")
    print("Guess the word one letter at a time.")
    print("You can make a maximum of 6 incorrect guesses.")

    secret_word = random.choice(load_words())
    category, hint = get_word_details(secret_word)

    guessed_letters = set()
    wrong_guesses = 0

    print("\nCategory:", category)
    print("Hint:", hint)

    while True:
        # Show the matching ASCII stage
        print(STAGES[wrong_guesses])

        # Show correctly guessed letters
        display_word = " ".join(
            letter.upper() if letter in guessed_letters else "_"
            for letter in secret_word
        )

        print("Word:", display_word)
        print(
            "Guessed letters:",
            ", ".join(sorted(guessed_letters))
            if guessed_letters else "None"
        )
        print("Incorrect guesses:", wrong_guesses, "/", MAX_ATTEMPTS)
        print("Attempts remaining:", MAX_ATTEMPTS - wrong_guesses)

        # Check for a win
        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations! You guessed the word!")
            print("Correct word:", secret_word.upper())
            print("Your score:", (MAX_ATTEMPTS - wrong_guesses) * 10)
            break

        # Check for a loss
        if wrong_guesses == MAX_ATTEMPTS:
            print("\nGame over! You ran out of attempts.")
            print("The correct word was:", secret_word.upper())
            print("Your score: 0")
            break

        guess = input("\nEnter one letter: ").strip().lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Enter one alphabetic letter.")
            continue

        # Prevent duplicate guesses
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Correct guess!")
        else:
            wrong_guesses += 1
            print("Wrong guess!")


while True:
    play_game()

    again = input("\nWould you like to play again? (yes/no): ")

    if again.strip().lower() not in ("yes", "y"):
        print("Thanks for playing Hangman!")
        break
