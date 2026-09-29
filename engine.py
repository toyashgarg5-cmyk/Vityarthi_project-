from validator import get_run_input
from player import get_computer_run
from display import show_delivery, show_innings_end

MAX_BALLS = 12
MAX_WICKETS = 1

def play_batting_innings(target=None):
    print("\n" + "="*30)
    print("🏏 TIME TO BAT! Let's put up a good score.")
    print("="*30)
    
    score = 0
    wicket = 0
    
    for ball in range(1, MAX_BALLS + 1):
        # Show target reminder if chasing
        if target is not None:
            runs_needed = target - score
            print(f"\n[Target: {target} | Need {runs_needed} runs from {MAX_BALLS - ball + 1} balls]")
            
        user_choice = get_run_input(f"Ball {ball}/{MAX_BALLS} - Play your shot (1-6): ")
        comp_choice = get_computer_run()
        
        # Add a little flair for big hits
        if user_choice in [4, 6] and user_choice != comp_choice:
            print(f"💥 Shot! You went for a big one...")
            
        if user_choice == comp_choice:
            print("\n❌ Oh no! The bowler read your mind. You're OUT! 🚶‍♂️")
            wicket += 1
            break
        else:
            score += user_choice
            show_delivery("Your shot", user_choice, "Bowl", comp_choice, score)
            
        if target is not None and score >= target:
            print("\n🎉 Boom! Target chased down successfully! You legend!")
            break
            
    show_innings_end(score)
    return score

def play_bowling_innings(target=None):
    print("\n" + "="*30)
    print("🥎 TIME TO BOWL! Let's defend this total.")
    print("="*30)
    
    score = 0
    wicket = 0
    
    for ball in range(1, MAX_BALLS + 1):
        if target is not None:
            runs_needed = target - score
            print(f"\n[Target to defend: {target} | Computer needs {runs_needed} runs]")
            
        user_choice = get_run_input(f"Ball {ball}/{MAX_BALLS} - Set your delivery (1-6): ")
        comp_choice = get_computer_run()
        
        if user_choice == comp_choice:
            print("\n wicket! YES! You outsmarted the computer! 🎯🔥")
            wicket += 1
            break
        else:
            score += comp_choice
            show_delivery("Computer's shot", comp_choice, "Your delivery", user_choice, score)
            
        if target is not None and score >= target:
            print("\n💔 Heartbreak! The computer chased down the target.")
            break
            
    show_innings_end(score)
    return score