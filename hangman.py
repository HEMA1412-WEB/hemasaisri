import random

def hangman():
    # List of predefined words
    words = ["python", "apple", "banana", "computer", "hangman"]
    word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("🎯 Welcome to the Hangman Game!")
    print("_ " * len(word))

    while attempts > 0:
        guess = input("\nGuess a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter only one letter.")
            continue

        # Check for repeated guesses
        if guess in guessed_letters:
            print("🔁 You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Good guess!")
        else:
            attempts -= 1
            print(f"❌ Wrong guess! Attempts left: {attempts}")

        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print("\nWord: ", display_word.strip())

        # Check win condition
        if "_" not in display_word:
            print("\n🎉 Congratulations! You guessed the word:", word)
            break
    else:
        print("\n😢 You ran out of attempts. The word was:", word)

# Run the game
if __name__ == "__main__":
    hangman()
