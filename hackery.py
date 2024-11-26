import random

# Function to generate a random number (0 or 1)
def zero_or_one():
    return random.choice([0, 1])

# ANSI escape code for green text
green_text = "\033[32m"

while True:
    print(f"{green_text}{zero_or_one()}", end="")