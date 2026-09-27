import random

def get_odd_even():
    while True:
        choice = input("Enter Odd or Even: ").strip().title()
        if choice  == "Odd" or choice  == "Even":
            return choice
        else:
            print("Invalid choice! Please enter Odd or Even.")
            
def get_number(message):
    while True:
        number = int(input(message))
        if 1 <= number <= 6:
            return number
        print("Please enter a number between 1 and 6.")

def get_batting_bowling():
    while True:
        choice = input("Choose Batting or Bowling: ").strip().title()
        if choice  == "Batting" or choice  == "Bowling":
            return choice
        print("Invalid choice! Please enter Batting or Bowling.")

def toss():
    print("\nTOSS")
    user_choice = get_odd_even()
    user_number = get_number("Enter your number from 1 to 6: ")
    computer_number = random.randint(1, 6)
    total = user_number + computer_number
    print("\nYour number:", user_number)
    print("Computer number:", computer_number)
    print("Total:", total)
    if user_choice  == "Even":
        user_wins = total % 2  == 0
    else:
        user_wins = total % 2 != 0
    if user_wins:
        print("\nYou won the toss!")
        return get_batting_bowling()
    else:
        print("\nComputer won the toss!")
        computer_choice = random.choice(["Batting", "Bowling"])
        print("Computer chose:", computer_choice)
        if computer_choice  == "Batting":
            return "Bowling"
        else:
            return "Batting"

def batting(target=None):
    print("\nBATTING")

    score = 0
    balls = 0
    wicket = 0

    while balls < 12 and wicket < 1:
        user_run = get_number("Choose your run (1-6): ")
        computer_run = random.randint(1, 6)
        balls = balls + 1
        print("Your choice:", user_run)
        print("Computer choice:", computer_run)
        if user_run  == computer_run:
            print("You got OUT!")
            wicket = wicket + 1
            break
        else:
            score = score + user_run
            print("Your score:", score)
        if target is not None and score >= target:
            print("You reached the target!")
            break
    print("\nYour final score:", score)
    return score

def bowling(target=None):
    print("\nBOWLING")
    score = 0
    balls = 0
    wicket = 0
    while balls < 12 and wicket < 1:
        user_number = get_number("Choose your bowling number (1-6): ")
        computer_run = random.randint(1, 6)
        balls = balls + 1
        print("Your choice:", user_number)
        print("Computer choice:", computer_run)
        if user_number  == computer_run:
            print("You got a wicket!")
            wicket = wicket + 1
            break
        else:
            score = score + computer_run
            print("Computer score:", score)
        if target is not None and score >= target:
            print("Computer reached the target!")
            break
    print("\nComputer's final score:", score)
    return score

def result(your_score, computer_score):
    print("RESULT")
    print("Your score:", your_score)
    print("Computer score:", computer_score)
    if your_score > computer_score:
        print("\nYOU WON THE GAME!")
    elif your_score < computer_score:
        print("\nYOU LOST THE GAME!")
    else:
        print("\nITS A TIE!")

def play_game():

    print("ODD-EVEN CRICKET GAME")
    print("\nThis game consists of 2 innings.")
    print("Each innings has a maximum of 12 balls and 1 wicket.")
    choice = toss()
    if choice  == "Batting":
        print("\nYou are batting first.")
        your_score = batting()
        print("\nNow you are bowling.")
        print("Computer is batting.")
        computer_score = bowling(your_score + 1)
    else:
        print("\nYou are bowling first.")
        computer_score = bowling()
        print("\nNow you are batting.")
        print("You need", computer_score + 1, "runs to win.")
        your_score = batting(computer_score + 1)

    result(your_score, computer_score)
while True:
    play_game()
    while True:
        again = input("\nDo you want to play again? (Yes/No): ").strip().title()
        if again  == "Yes":
            break
        elif again  == "No":
            print("\nThank you for playing!")
            exit()
        else:
            print("Invalid input! Please enter Yes or No.")

