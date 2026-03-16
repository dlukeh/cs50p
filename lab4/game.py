import random

# Prompt for level
while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass

# Generate random number
number = random.randint(1, level)

# Prompt for guesses
while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            continue
    except ValueError:
        continue

    if guess < number:
        print("Too small!")
    elif guess > number:
        print("Too large!")
    else:
        print("Just right!")
        break
