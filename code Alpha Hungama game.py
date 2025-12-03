import random

# Step 1: List of predefined words
words = ["python", "hangman", "coding", "simple", "random"]

# Step 2: Choose a random word
secret_word = random.choice(words)

# Step 3: Variables to track progress
guessed_letters = []  # letters the user has guessed
incorrect_guesses = 0
max_incorrect = 6

# Step 4: Game Loop
print("🎮 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses.\n")

# Create display word like _ _ _ _
display_word = ["_" for _ in secret_word]

while incorrect_guesses < max_incorrect and "_" in display_word:
    print("Word: ", " ".join(display_word))
    print(f"Incorrect guesses: {incorrect_guesses}/{max_incorrect}")
    print("Guessed letters:", guessed_letters)
    
    guess = input("\nEnter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter!\n")
        continue

    # Add the guess to list
    guessed_letters.append(guess)

    # Check the guess
    if guess in secret_word:
        print("✅ Good guess!\n")
        # Reveal the letter in display_word
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        incorrect_guesses += 1
        print("❌ Wrong guess!\n")

# Step 5: End of game
if "_" not in display_word:
    print("🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("💀 Game Over! The correct word was:", secret_word)