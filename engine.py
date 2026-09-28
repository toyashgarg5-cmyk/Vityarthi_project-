from validator import get_run_input
from player import get_computer_run
from display import show_delivery, show_innings_end

MAX_BALLS = 12
MAX_WICKETS = 1

def play_batting_innings(target=None):
    print("\n--- BATTING INNINGS ---")
    score = 0
    wicket = 0
    
    for ball in range(1, MAX_BALLS + 1):
        user_choice = get_run_input(f"Ball {ball}/{MAX_BALLS} - Choose your run (1-6): ")
        comp_choice = get_computer_run()
        
        if user_choice == comp_choice:
            print("Computer matched your number! You got OUT!")
            wicket += 1
            break
        else:
            score += user_choice
            show_delivery("Your choice", user_choice, "Computer choice", comp_choice, score)
            
        if target is not None and score >= target:
            print("Target reached!")
            break
            
    show_innings_end(score)
    return score

def play_bowling_innings(target=None):
    print("\n--- BOWLING INNINGS ---")
    score = 0
    wicket = 0
    
    for ball in range(1, MAX_BALLS + 1):
        user_choice = get_run_input(f"Ball {ball}/{MAX_BALLS} - Choose your bowling number (1-6): ")
        comp_choice = get_computer_run()
        
        if user_choice == comp_choice:
            print("You got a wicket! Computer is OUT!")
            wicket += 1
            break
        else:
            score += comp_choice
            show_delivery("Computer choice", comp_choice, "Your choice", user_choice, score)
            
        if target is not None and score >= target:
            print("Computer reached the target!")
            break
            
    show_innings_end(score)
    return score