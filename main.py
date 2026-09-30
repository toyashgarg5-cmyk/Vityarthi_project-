from validator import get_odd_even, get_number, get_batting_bowling
from player import get_computer_toss_number, get_computer_toss_decision
from display import show_welcome, show_toss_result, show_match_result
from engine import play_batting_innings, play_bowling_innings

# conduct toss between user and computer
def conduct_toss():
    print("\n--- TOSS ---")
    u_call = get_odd_even()
    u_num = get_number()
    c_num = get_computer_toss_number()
    
    tot = u_num+c_num # calculate toss sum
    
    # check sum parity
    if tot % 2 == 0:
        outcome = "even"
    else:
        outcome = "odd"
        
    win = (u_call == outcome)
    show_toss_result(u_num, c_num, tot, win)
    
    # role decision based on toss
    if win:
        role = get_batting_bowling()
    else:
        c_pick = get_computer_toss_decision()
        pick_str = "Computer won the toss and chose to %s first." % c_pick
        print(pick_str)
        if c_pick == "Batting":
            role = "Bowling"
        else:
            role = "Batting"
            
    return role

# handle game flow for both innings
def play_match():
    show_welcome()
    first_role = conduct_toss()
    
    # innings 1 and 2 execution
    if first_role == "Batting":
        print("\n--- You are batting first ---")
        u_score = play_batting_innings()
        target = u_score + 1
        t_msg = "\nTarget for computer is %d runs." % target
        print(t_msg)
        
        c_score = play_bowling_innings(target)
    else:
        print("\n--- Computer is batting first (You are bowling) ---")
        c_score = play_bowling_innings()
        target = c_score + 1
        t_msg = "\nTarget to chase is %d runs." % target
        print(t_msg)
        
        u_score = play_batting_innings(target)
        
    show_match_result(u_score, c_score)

# main game loop with replay option
def main():
    while 1:
        play_match()
        again = input("\nDo you want to play again? (yes/no): ")
        again = again.lower().strip()
        if again not in ["yes", "y"]:
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()