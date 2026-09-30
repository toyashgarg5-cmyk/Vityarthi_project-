# intro banner and rules
def welcome():
    bar = "=" * 40
    print(bar)
    print("        ODD-EVEN CRICKET GAME        ")
    print(bar)
    print("This game consists of 2 innings.")
    print("Each innings has a maximum of 12 balls and 1 wicket.\n")

# print toss outcome
def toss_result(u_num, c_num, total, u_won):
    s1 = "\nYour number: %s" % u_num
    s2 = "Computer number: %s" % c_num
    tot_str = "Total: " + str(total)
    print(s1)
    print(s2)
    print(tot_str)
    if u_won:
        print("You won the toss!")
    else:
        print("Computer won the toss!")

# display each ball delivery and score
def delivery(bat_lbl, bat_val, bowl_lbl, bowl_val, cur_score):
    b_info = "%s: %s" % (bat_lbl, bat_val)
    bw_info = "%s: %s" % (bowl_lbl, bowl_val)
    sc = "Score: " + str(cur_score) + "\n"
    print(b_info)
    print(bw_info)
    print(sc)

# innings finish score
def innings_end(tot):
    res_str = "\nFinal score: %s\n" % str(tot)
    print(res_str)

# declare match winner
def match_result(u_score, c_score):
    sep = "=" * 30
    print(sep)
    print("            RESULT            ")
    print(sep)
    u_msg = "Your score: %d" % u_score
    c_msg = "Computer score: %d\n" % c_score
    print(u_msg)
    print(c_msg)
    if u_score > c_score:
        print("YOU WON THE GAME!")
    elif c_score > u_score:
        print("YOU LOST THE GAME!")
    else:
        print("IT'S A TIE!")
    print(sep)

# aliases for project compatibility
show_welcome = welcome
show_toss_result = toss_result
show_delivery = delivery
show_innings_end = innings_end
show_match_result = match_result