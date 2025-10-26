import random

# List of possible colors
COLORS = ["red", "blue", "green", "yellow", "orange", "black"]

def generate_secret():
    """Generate a random secret combination of 4 colors."""
    return [random.choice(COLORS) for _ in range(4)]

def get_player_guess():
    """
    Ask the player for a guess,
    check length and validate the colors.
    """
    while True:
        guess_input = input("Enter your guess (4 colors among {} separated by spaces): ".format(", ".join(COLORS)))
        guess = guess_input.strip().lower().split()
        if len(guess) != 4:
            print("Error: You must enter exactly 4 colors.")
        elif any(color not in COLORS for color in guess):
            print("Error: Invalid color in your guess.")
        else:
            return guess

def give_feedback(secret, guess):
    """
    Give feedback for the guess:
    '*' for each well-placed color,
    '-' for each correct color in wrong position.
    """
    secret_copy = secret.copy()
    guess_copy = guess.copy()
    well_placed = 0
    misplaced = 0

    # First, check well-placed
    for i in range(4):
        if guess_copy[i] == secret_copy[i]:
            well_placed += 1
            secret_copy[i] = guess_copy[i] = None  # Mark as checked

    # Now, check misplaced
    for i in range(4):
        if guess_copy[i] and guess_copy[i] in secret_copy:
            misplaced += 1
            idx = secret_copy.index(guess_copy[i])
            secret_copy[idx] = None

    return well_placed, misplaced

def mastermind():
    print("=== Mastermind Game ===")
    secret = generate_secret()
    max_attempts = 10

    for attempt in range(1, max_attempts + 1):
        print(f"\nAttempt {attempt}/{max_attempts}")
        guess = get_player_guess()
        well_placed, misplaced = give_feedback(secret, guess)
        print("Feedback: {} correct position(s) [*], {} correct color(s) but wrong position [-]".format(well_placed, misplaced))

        if well_placed == 4:
            print(f"Congratulations! You found the secret code in {attempt} attempts!")
            break
    else:
        print("Game over! The secret code was: {}".format(" ".join(secret)))

if __name__ == "__main__":
    mastermind()
