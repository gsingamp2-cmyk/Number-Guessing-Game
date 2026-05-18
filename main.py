import random
import os


def get_high_score():
    if os.path.exists("score.txt"):
        with open("score.txt", "r") as file:
            return file.read()
    return None


def save_high_score(score):
    with open("score.txt", "w") as file:
        file.write(str(score))


def play_game():

    print("\nSelect Difficulty")
    print("1. Easy (1-50)  | Attempts:10")
    print("2. Medium (1-100) | Attempts:7")
    print("3. Hard (1-500) | Attempts:5")

    difficulty = int(input("Enter choice: "))

    if difficulty == 1:
        max_num = 50
        max_attempts = 10

    elif difficulty == 2:
        max_num = 100
        max_attempts = 7

    elif difficulty == 3:
        max_num = 500
        max_attempts = 5

    else:
        print("Invalid choice. Medium selected.")
        max_num = 100
        max_attempts = 7

    ans = random.randint(1, max_num)

    print("\nGuess number between 1 and", max_num)

    high_score = get_high_score()

    if high_score:
        print("Current High Score:", high_score, "attempts")

    count = 0
    win = False

    while count < max_attempts:

        user_input = int(input("Enter guess: "))
        count += 1

        if user_input == ans:
            print("\nCorrect!")
            print("You guessed in", count, "attempts")

            if high_score is None or count < int(high_score):
                save_high_score(count)
                print("New High Score!")

            win = True
            break

        elif user_input < ans:
            print("Too Low")

        else:
            print("Too High")

        remaining = max_attempts-count
        print("Attempts left:", remaining)

        if remaining == 2:
            print("\nHint:")

            if ans % 2 == 0:
                print("Number is even")
            else:
                print("Number is odd")

    if not win:
        print("\nGame Over")
        print("Correct number was:", ans)


while True:

    play_game()

    choice = input("\nPlay Again? (y/n): ")

    if choice.lower() != 'y':
        print("Thanks for playing!")
        break