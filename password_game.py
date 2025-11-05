import random

# Password Guessing Game by Dushant Gautam

def play_game():
    easy_words = ["apple", "train", "tiger", "money", "india"]
    medium_words = ["python", "bottle", "monkey", "planet", "laptop"]
    hard_words = ["elephant", "diamond", "umbrella", "computer", "mountain"]

    print("====================================")
    print("   Welcome to the Password Game!   ")
    print("====================================")
    print("Choose a difficulty: easy / medium / hard")

    level = input("Enter difficulty: ").lower()

    if level == "easy":
        secret = random.choice(easy_words)
    elif level == "medium":
        secret = random.choice(medium_words)
    elif level == "hard":
        secret = random.choice(hard_words)
    else:
        print("Invalid choice! Defaulting to Easy level.")
        secret = random.choice(easy_words)

    attempts = 0
    max_attempts = 5
    score = 0
    guessed_words = []

    print("\nGuess the secret password!")
    print(f"You have {max_attempts} attempts.\n")

    while attempts < max_attempts:
        guess = input("Enter your guess: ").lower()
        attempts += 1
        guessed_words.append(guess)

        if guess == secret:
            score = (max_attempts - attempts + 1) * 10
            print(f"\n🎉 Correct! You guessed it in {attempts} attempt(s).")
            print(f"Your Score: {score} points")
            break
        else:
            hint = ""
            for i in range(len(secret)):
                if i < len(guess) and guess[i] == secret[i]:
                    hint += guess[i]
                else:
                    hint += "_"
            print(f"Hint: {hint}")
            print(f"Attempts left: {max_attempts - attempts}")
            print(f"Your previous guesses: {', '.join(guessed_words)}\n")

    if guess != secret:
        print("\n❌ Out of attempts!")
        print(f"The secret password was: {secret}")
        print("Better luck next time!")

    print("\nGame Over.")
    print("====================================")
    return score


# Main loop for replay option
total_score = 0

while True:
    total_score += play_game()
    choice = input("\nDo you want to play again? (yes/no): ").lower()
    if choice != "yes":
        print("\nThanks for playing!")
        print(f"Your total score: {total_score} points")
        print("Goodbye 👋")
        break
