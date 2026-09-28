import random

def get_computer_toss_number():
    return random.randint(1, 6)

def get_computer_toss_decision():
    return random.choice(["Batting", "Bowling"])

def get_computer_run():
    return random.randint(1, 6)