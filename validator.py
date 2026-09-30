# ask user odd or even for toss
def ask_odd_even():
    while 1:
        ch = input("Enter Odd or Even: ")
        ch = ch.strip().lower()
        # validate parity input
        if ch == "odd" or ch == "even":
            return ch
        print("Invalid choice! Please enter Odd or Even.")

# get toss number from user (1 to 6)
def ask_number():
    while 1:
        raw_inp = input("Enter your number from 1 to 6: ")
        try:
            n = int(raw_inp)
            # check 1-6 bounds
            if n >= 1 and n <= 6:
                return n
            else:
                print("Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# user choice for batting or bowling after winning toss
def ask_bat_bowl():
    while 1:
        ans = input("Choose Batting or Bowling: ")
        ans = ans.strip().lower()
        # check bat or bowl selection
        if ans == "batting" or ans == "bowling":
            return ans.capitalize()
        print("Invalid choice! Please type Batting or Bowling.")

# get run / delivery input with custom prompt
def ask_run(prompt):
    while 1:
        val = input(prompt)
        try:
            r = int(val)
            # check valid range
            if r >= 1 and r <= 6:
                return r
            else:
                err = "Invalid choice! Choose a number from %d to %d." % (1, 6)
                print(err)
        except ValueError:
            print("Invalid input! Please enter a number.")

# compatibility aliases
get_odd_even = ask_odd_even
get_number = ask_number
get_batting_bowling = ask_bat_bowl
get_run_input = ask_run