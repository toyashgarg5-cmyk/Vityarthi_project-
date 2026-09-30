from player import get_computer_run, get_computer_toss_number, get_computer_toss_decision

# test computer generation bounds
def test_bounds():
    # run multiple random trials
    for i in range(100):
        val = get_computer_run()
        # check run value range 1 to 6
        assert (val >= 1 and val <= 6), "Invalid run generated: " + str(val)
        
        toss_val = get_computer_toss_number()
        # check toss number range 1 to 6
        assert (toss_val >= 1 and toss_val <= 6), "Invalid toss number: %s" % toss_val

        dec = get_computer_toss_decision()
        # check toss choice is batting or bowling
        assert dec in ["Batting", "Bowling"], "Invalid decision: %s" % dec

    print("All unit tests passed successfully!")

# compatibility alias for test suite
test_computer_bounds = test_bounds

# run tests directly
if __name__ == "__main__":
    test_computer_bounds()