from validator import get_odd_even, get_number, get_batting_bowling
from player import get_computer_toss_number, get_computer_toss_decision
from display import show_welcome, show_toss_result, show_match_result
from engine import play_batting_innings, play_bowling_innings

def conduct_toss():
    print("--- TOSS ---")
    user_call = get_odd_even()
    user_num = get_number()
    comp_num = get_computer_toss_number()
    total = user_num + comp_num
    
    is_odd = (total % 2 != 0)
    user_won = (user_call == "odd" and is_odd) or (user_call == "even" and not is_odd)
    
    show_toss_result(user_num, comp_num, total, user_won)
    
    if user_won:
        decision = get_batting_bowling()
    else:
        decision = get_computer_toss_decision()
        print(f"Computer chose to {decision} first.")
        
    return decision if user_won else ("Batting" if decision == "Bowling" else "Bowling")

def play_match():
    show_welcome()
    first_innings_role = conduct_toss()
    
    if first_innings_role == "Batting":
        print("\nYou are batting first.")
        user_score = play_batting_innings()
        target = user_score + 1
        print(f"\nTarget for Computer: {target} runs from 12 balls.")
        comp_score = play_bowling_innings(target=target)
    else:
        print("\nComputer is batting first. You are bowling.")
        comp_score = play_bowling_innings()
        target = comp_score + 1
        print(f"\nTarget for You: {target} runs from 12 balls.")
        user_score = play_batting_innings(target=target)
        
    show_match_result(user_score, comp_score)

def main():
    while True:
        play_match()
        replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if replay not in ["yes", "y"]:
            print("Thank you for playing Odd-Even Cricket!")
            break

if __name__ == "__main__":
    main()