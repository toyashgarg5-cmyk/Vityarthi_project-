#This function inputs Odd or Even from user
def get_odd_even():
    while True:
        choice = input("Enter Odd or Even: ").strip().lower()
        if choice in ["odd", "even"]:
            return choice
        print("Invalid choice! Please enter Odd or Even.")

#This function inputs number from user between 1-6
def get_number():
    while True:
        try:
            val = int(input("Enter your number from 1 to 6: "))
            if 1 <= val <= 6:
                return val
            print("Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

#This function inputs the user's choice for batting or bowling if they won the toss
def get_batting_bowling():
    while True:
        choice = input("Choose Batting or Bowling: ").strip().lower()
        if choice in ["batting", "bowling"]:
            return choice.capitalize()
        print("Invalid choice! Please type Batting or Bowling.")

#This function handles the error
def get_run_input(prompt):
    while True:
        try:
            val = int(input(prompt))
            if 1 <= val <= 6:
                return val
            print("Invalid choice! Choose a number from 1 to 6.")
        except ValueError:
            print("Invalid input! Please enter a number.")