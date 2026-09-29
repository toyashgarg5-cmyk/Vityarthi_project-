#Function for odd even cricket game instructions
def show_welcome():
    print("=" * 40)
    print("        ODD-EVEN CRICKET GAME        ")
    print("=" * 40)
    print("This game consists of 2 innings.")
    print("Each innings has a maximum of 12 balls and 1 wicket.\n")

#Function for showing if user won the toss or lost
def show_toss_result(user_num, comp_num, total, winner_is_user):
    print(f"\nYour number: {user_num}")
    print(f"Computer number: {comp_num}")
    print(f"Total: {total}")
    if winner_is_user:
        print("You won the toss!")
    else:
        print("Computer won the toss!")

#Function for showing mid game scores 
def show_delivery(batter_label, batter_val, bowler_label, bowler_val, current_score):
    print(f"{batter_label}: {batter_val}")
    print(f"{bowler_label}: {bowler_val}")
    print(f"Score: {current_score}\n")

#Function for showing final score
def show_innings_end(final_score):
    print(f"\nFinal score: {final_score}\n")

#Function for declaring who won the match and shows final scorecard
def show_match_result(user_score, comp_score):
    print("=" * 30)
    print("            RESULT            ")
    print("=" * 30)
    print(f"Your score: {user_score}")
    print(f"Computer score: {comp_score}\n")
    if user_score > comp_score:
        print("YOU WON THE GAME!")
    elif comp_score > user_score:
        print("YOU LOST THE GAME!")
    else:
        print("IT'S A TIE!")
    print("=" * 30)