import random

# Predefined list of words
WORDS = ["python", "testing", "github", "programming", "assignment"]

def choose_word():
    """Selects a random word from the predefined list."""
    return random.choice(WORDS)

def display_word(word, guessed_letters):
    """Reveals correctly guessed letters and hides the rest."""
    return "".join(letter if letter in guessed_letters else "_" for letter in word)

def play_game():
    word = choose_word()
    guessed_letters = set()
    attempts = 6  # Maximum attempts

    print("Welcome to the Word Guessing Game!")
    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
        else:
            print("Wrong guess!")
            attempts -= 1
            print(f"Remaining attempts: {attempts}")

        if set(word).issubset(guessed_letters):
            print(f"Congratulations! You guessed the word: {word}")
            return

    print(f"Game Over! The word was: {word}")

if __name__ == "__main__":
    play_game()
