from validator import get_run_input
from player import get_computer_run
from display import show_delivery, show_innings_end

# match rules setup
max_balls = 12
max_wickets = 1
MAX_BALLS = max_balls
MAX_WICKETS = max_wickets

# user batting innings
def bat_innings(target=None):
    sep = "=" * 30
    print("\n" + sep)
    print("TIME TO BAT! Let's put up a good score.")
    print(sep)
    
    score = 0
    wkt = 0
    
    for b in range(1, max_balls + 1):
        # target status when chasing
        if target is not None:
            req = target - score
            b_left = (max_balls - b) + 1
            print("\n[Target: %d | Need %d runs from %d balls]" % (target, req, b_left))
            
        msg = "Ball " + str(b) + "/" + str(max_balls) + " - Play your shot (1-6): "
        u_shot = get_run_input(msg)
        c_bowl = get_computer_run()
        
        # 4s and 6s celebration
        if u_shot in [4, 6]:
            if u_shot != c_bowl:
                print("Shot! You went for a big one...")
            
        # check wicket
        if u_shot == c_bowl:
            print("\nOh no! The bowler read your mind. You're OUT!")
            wkt = wkt + 1
            break
        else:
            score = score + u_shot
            show_delivery("Your shot", u_shot, "Bowl", c_bowl, score)
            
        if target is not None:
            if score >= target:
                print("\nBoom! Target chased down successfully! You legend!")
                break
            
    show_innings_end(score)
    return score

# user bowling innings
def bowl_innings(target=None):
    sep = "=" * 30
    print("\n" + sep)
    print("TIME TO BOWL! Let's defend this total.")
    print(sep)
    
    score = 0
    wkt = 0
    
    for b in range(1, max_balls + 1):
        if target is not None:
            rem = target - score
            print("\n[Target to defend: %s | Computer needs %s runs]" % (target, rem))
            
        msg = "Ball %d/%d - Set your delivery (1-6): " % (b, max_balls)
        u_bowl = get_run_input(msg)
        c_shot = get_computer_run()
        
        # check wicket
        if u_bowl == c_shot:
            print("\nWicket! YES! You outsmarted the computer!")
            wkt = wkt + 1
            break
        else:
            score = score + c_shot
            show_delivery("Computer's shot", c_shot, "Your delivery", u_bowl, score)
            
        if target is not None:
            if score >= target:
                print("\nHeartbreak! The computer chased down the target.")
                break
            
    show_innings_end(score)
    return score

# aliases for project compatibility
play_batting_innings = bat_innings
play_bowling_innings = bowl_innings