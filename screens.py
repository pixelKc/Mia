from logic import *
from utils import *

# 1. Main Menu Screen
def print_main_menu():
    print_screen_header("MIA DICE GAME")
    print("\n1. Start Game")
    print("2. See Rules")
    print("3. Exit Game")
    print("\n")

# 1.a Rules Screen
def print_rules_screen():
    """Display the rules of the Mia game"""
    print_screen_header("MIA GAME RULES")
    print("Mia is a bluffing dice game where players roll dice in secret")
    print("and take turns making claims about their rolls.")
    print("\nGAMEPLAY:")
    print("- Each player rolls 2 dice in secret")
    print("- Players take turns making claims about their roll's rank")
    print("- First player can claim any roll (no previous roll to beat)")
    print("- Though there is little reason to bluff, you can if you want")
    print("- Subsequent players who roll MUST claim higher than the previous roll")
    print("- You can either challenge the previous claim OR roll your own dice")
    print("- If you roll, you MUST claim higher than the previous roll")
    print("- The round continues until someone challenges")
    print("- When challenged, both players reveal their dice")
    print("- If you challenge and are WRONG, you get a point")
    print("- If you challenge and are RIGHT, they get a point for bluffing")
    print("- If someone bluffs on or challenges a Mia, they get 2 points")
    print("- Once Mia is claimed, next player must also roll Mia to match")
    print("- After a challenge, the round ends and a new round begins")
    print("- New round starts with the next player who was about to roll")
    print("- First player to reach 10 points loses the game!")
    print("\nROLL HIERARCHY (from highest to lowest):")
    print("- Mia: 21 (highest possible roll)")
    print("- Doubles: 66 > 55 > 44 > 33 > 22 > 11")
    print("- Mixed Rolls: 65 > 64 > 63 > 62 > 61 >")
    print("               54 > 53 > 52 > 51 >")
    print("               43 > 42 > 41 >")
    print("               32 > 31")
    print("\nEXAMPLES:")
    print("- Mia beats all doubles and mixed rolls")
    print("- 66 beats 55, 44, 33, 22, 11, and all mixed rolls")
    print("- 65 beats 64, 63, 62, 61, 54, 53, 52, 51, etc.")
    input("Press Enter to return to main menu...")

# 2. Roll Dice Screen
def print_roll_dice_screen(current_player, player1_score, player2_score, roll_history):
    print_screen_header(f"PLAYER {current_player}'S TURN")
    print(f"\nPlayer 1: {player1_score}/10 points")
    print(f"Player 2: {player2_score}/10 points")
    print()
    
    previous_roll = get_last_roll_from_history(roll_history)
    if previous_roll is not None:
        print(f"Roll History: {roll_history}\n")
        print(f"Previous Roll to Beat: {previous_roll}")
    else:
        print("This is the first roll of the round!")
    print()
    
    input("Press Enter to roll the dice!")

# 3. Make Claim Screen
def print_make_claim_screen(current_player, roll_history):
    print_screen_header(f"PLAYER {current_player}'S TURN")
    print()
    
    # Roll the dice
    actual_roll = roll_dice()
    print(f"Roll value: {actual_roll}")
    print()

    # Get the previous roll to beat from roll history
    previous_roll = get_last_roll_from_history(roll_history)
    # Display roll history
    # Display previous roll to beat
    if previous_roll is None:
        print(f"Your roll of {actual_roll} is the first of the round!")
        print("You can claim any roll.")
    else:
        print(f"Roll History: {roll_history}")
        print(f"Previous roll to beat: {previous_roll}")
        # Check if the actual roll beats the previous roll
        if does_a_beat_b(actual_roll, previous_roll):
            print(f"Your roll {actual_roll} BEATS the previous roll {previous_roll}!")
        else:
            print(f"Your roll {actual_roll} does NOT beat the previous roll {previous_roll}.")
            print("You will need to BLUFF!!")
    print()
    
    # Get the player's claimed roll
    claimed_roll = run_bluffing_phase(actual_roll, previous_roll)
    
    return actual_roll, claimed_roll

# 3.a Make Claim Screen - Run Bluffing Phase
def run_bluffing_phase(actual_roll, previous_roll):
    """Run the bluffing phase where players claim their rolls"""
    
    while True:
        print("What roll would you like to claim?")
        print()
        
        claim = input("Enter your claimed roll: ").strip()

        if claim == actual_roll:
            print("Great you're not bluffing!")
            print("However let's still check if you're forced to bluff!")
        
        # Use the validate_claim function properly
        if validate_claim(claim, previous_roll):
            return claim  # Validation passed, return the claim
        # If validation failed, continue the loop to get a new claim

# 4. Player Transition Screen
def print_player_transition_screen(current_player, player1_score, player2_score, roll_history):
    """Display the player transition screen"""
    print_screen_header(f"Player {current_player}'s Turn")
    print(f"""
          Player 1: {player1_score}\n
          Player 2: {player2_score}\n
          Roll History: {roll_history}\n
          Roll to beat {get_last_roll_from_history(roll_history)}\n\n
          Select an option:\n
          1. Roll the dice\n
          2. Challenge the previous claim\n
""")
    userOption = input("Select an option 1 or 2\n")
    actual_roll = None
    if int(userOption) == 1:
        print_roll_dice_screen(current_player, player1_score, player2_score, roll_history)
        actual_roll, = print_make_claim_screen(current_player, roll_history)
    elif int(userOption) == 2:
        player1_score, player2_score = print_challenge_results_screen(current_player, player1_score, player2_score, actual_roll, roll_history)
    else:
        pass
    return player1_score, player2_score

# 5. Challenge Results Screen
def print_challenge_results_screen(challenger_player, player1_score, player2_score, actual_roll, roll_history):
    """Display the challenge results screen"""
    print_screen_header("CHALLENGE RESULTS SCREEN")
    print(f"{challenger_player} chooses to CHALLENGE!")
    print(f"\n Roll History: {roll_history}")
    if challenger_player == "Player 1":
        print(f"Player 2's claimed roll{get_last_roll_from_history(roll_history)}")
        print(f"Player 2's actual roll{actual_roll}")
        if actual_roll == get_last_roll_from_history(roll_history):
            player1_score, player2_score = update_scores(1, player1_score, player2_score, 1)
            print("\n Challenge Result: FAIL")
            print("Player 2 was, in fact, not bluffing")
        else:
                player1_score, player2_score = update_scores(2, player1_score, player2_score, 1)
                print("\n Challenge Result: SUCCESS")
                print("Player 2 was, in fact, bluffing")
                print("\n Player 2 gets +1")
                print("Player 1 gets +0")
    else:
        print(f"Player 1's claimed roll{get_last_roll_from_history(roll_history)}")
        print(f"Player 1's actual roll{actual_roll}")
        if actual_roll == get_last_roll_from_history(roll_history):
            player1_score, player2_score = update_scores(2, player1_score, player2_score, 1)
            print("\n Challenge Result: FAIL")
            print("Player 1 was, in fact, not bluffing")
        else:
            player1_score, player2_score = update_scores(1, player1_score, player2_score, 1)
            print("\n Challenge Result: SUCCESS")
            print("Player 1 was, in fact, bluffing")
            print("\n Player 1 gets +1")
            print("Player 2 gets +0")
    print("\n New Scores: ")
    print(f"Player 1: {player1_score}/10")
    print(f"Player 2: {player2_score}/10")

    input("\n Press Enter to continue to the next round...")
    return player1_score, player2_score

def print_game_over(player1_score, player2_score):
    print_screen_header("Game Over")

    print("\n Scores:")
    print(f"Player 1 Score: {player1_score}")
    print(f"Player 2 Score: {player2_score}")

    if player1_score == 10:
        print("Player 2 Wins")
    else:
        print("Player 1 Wins")

    print("\n Thank you for playing Mia")