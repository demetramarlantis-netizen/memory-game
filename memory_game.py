#this is where our code will be 
from game_logic import generate_colors, change_one_color
import time


def play_round():
    colors = generate_colors()

    print("Memorize these colors:")

    for i, color in enumerate(colors):
        print(f"{i}: {color}")
    time.sleep(2)


    print("\n" * 50)  # clears screen (simple way)

    new_colors, correct_index = change_one_color(colors)

    print("One color changed!")
    
    for i, color in enumerate(new_colors):
        print(f"{i}: {color}")  

    guess = int(input("Enter the index (0-9) of the changed square: "))

    if guess == correct_index:
        print("Correct!")
        return 1
    else:
        print(f"INCORRECT!! It was square {correct_index}")

def main():
    name = input("Enter your name: ")
    print(f"Welcome {name}!")

    score = 0

    while score < 5:
        score += play_round()
        print(f"Score: {score}/5\n")

    print("Congratulations! You won the game!")

if __name__ == "__main__":
    main()
    