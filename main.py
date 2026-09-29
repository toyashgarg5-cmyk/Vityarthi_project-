from validator import get_odd_even, get_number, get_batting_bowling
from player import get_computer_toss_number, get_computer_toss_decision
from display import show_welcome, show_toss_result, show_match_result
from engine import play_batting_innings, play_bowling_innings

# This function runs the toss
def conduct_toss():
    print("\n--- TOSS ---")
    user_choice = get_odd_even()
    user_num = get_number()
    comp_num = get_computer_toss_number()
    
    total = user_num + comp_num
    
    # Check if sum is odd or even
    if total % 2 != 0:
        toss_outcome = "odd"
    else:
        toss_outcome = "even"
        
    user_won = (user_choice == toss_outcome)
    show_toss_result(user_num, comp_num, total, user_won)
    
    if user_won:
        user_role = get_batting_bowling()
    else:
        comp_decision = get_computer_toss_decision()
        print(f"Computer won the toss and chose to {comp_decision} first.")
        if comp_decision == "Batting":
            user_role = "Bowling"
        else:
            user_role = "Batting"
            
    return user_role

# This function runs the actual game 
def play_match():
    show_welcome()
    user_first_role = conduct_toss()
    
    if user_first_role == "Batting":
        print("\n--- You are batting first ---")
        user_score = play_batting_innings()
        target = user_score + 1
        print(f"\nTarget for computer is {target} runs.")
        
        comp_score = play_bowling_innings(target)
    else:
        print("\n--- Computer is batting first (You are bowling) ---")
        comp_score = play_bowling_innings()
        target = comp_score + 1
        print(f"\nTarget to chase is {target} runs.")
        
        user_score = play_batting_innings(target)
        
    show_match_result(user_score, comp_score)

#This function asks the user if they want to play again
def main():
    while True:
        play_match()
        play_again = input("\nDo you want to play again? (yes/no): ").lower().strip()
        if play_again not in ["yes", "y"]:
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()