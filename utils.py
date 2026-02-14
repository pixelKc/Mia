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

def get_last_roll_from_history(roll_history):
    """Extract the last roll from the roll history string"""
    
    if roll_history == "":
        return None
    else:
        return roll_history[-2:]
    pass

def isGameOver(player1_score, player2_score):
    if player1_score == 10 or player2_score == 10:
        return True
    else:
        return False