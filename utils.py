import os

def print_screen_header(title):
    clear_screen()
    print("\n" + "="*60)
    print(title.center(60))
    print("="*60)
    
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def update_scores(player, player1_score, player2_score, points_to_gain):
    """Update the score for the specified player and return both updated scores"""
    if player == 1:
        player1_score += points_to_gain
    else:
        player2_score += points_to_gain
    return player1_score, player2_score

# TODO: STEP 1: Implement the get_last_roll_from_history() helper function
def get_last_roll_from_history(roll_history):
    """Extract the last roll from the roll history string"""
    # TODO: STEP 1: Implement this function using string slicing
    # a. Takes a roll_history string as input (e.g., "63, 55, 66")
    # b. Returns None if the roll_history is empty (first roll of the game)
    # c. Uses string slicing to extract the last roll from the history:
    #    - Use string slicing with negative index: roll_history[-2:] to get the last 2 characters
    #    - This works because each roll is exactly 2 digits, so the last 2 characters are always the most recent roll
    # d. Handle the empty string case with an if statement
    # e. Returns the most recent roll as a string (e.g., "66")
    pass