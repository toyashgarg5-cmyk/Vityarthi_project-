from player import get_computer_run, get_computer_toss_number

def test_computer_bounds():
    for _ in range(100):
        val = get_computer_run()
        assert 1 <= val <= 6, f"Invalid run generated: {val}"
        
        toss_val = get_computer_toss_number()
        assert 1 <= toss_val <= 6, f"Invalid toss number: {toss_val}"
    print("All unit tests passed successfully!")

if __name__ == "__main__":
    test_computer_bounds()