import random

# bot options for toss
toss_opts = ["Batting", "Bowling"]

# comp toss roll
def comp_toss_num():
    n = random.randint(1,6)
    return n

# comp bat/bowl decision
def comp_decision():
    idx = random.randint(0,1)
    res = "%s" % toss_opts[idx]
    return res

# comp shot or delivery
def comp_run():
    r = random.randint(1,6)
    return r

# aliases for project compatibility
get_computer_toss_number = comp_toss_num
get_computer_toss_decision = comp_decision
get_computer_run = comp_run