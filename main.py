import random

# Global Mia hierarchy list - rolls ordered from highest (index 0) to lowest
# Mia (21) is the highest, followed by doubles, then mixed rolls
mia_hierarchy = ["21", "66", "55", "44", "33", "22", "11", "65", "64", "63", "62", "61", "54", "53", "52", "51", "43", "42", "41", "32", "31"]

def print_rules():
    """Display the rules of the Mia game"""
    print("\n" + "="*60)
    print("MIA GAME RULES".center(60))
    print("="*60)
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
    print("- Mia (21): The highest possible roll (2 and 1)")
    print("- Doubles: 66 > 55 > 44 > 33 > 22 > 11")
    print("- Mixed Rolls: 65 > 64 > 63 > 62 > 61 > 54 > 53 > 52 > 51")
    print("           > 43 > 42 > 41 > 32 > 31")
    print("\nEXAMPLES:")
    print("- Mia beats all doubles and mixed rolls")
    print("- 66 beats 55, 44, 33, 22, 11, and all mixed rolls")
    print("- 65 beats 64, 63, 62, 61, 54, 53, 52, 51, etc.")
    print("="*60)
    input("\nPress Enter to return to main menu...")

def roll_dice():
    """Roll two dice and return them as a string with higher roll first"""
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    
    # Compare the rolls as integers to find the higher one
    if die1 >= die2:
        # Use f-string formatting to return higher roll first
        return f"{die1}{die2}"
    else:
        return f"{die2}{die1}"

def get_index_of_roll(roll):
    """Get the index of a roll in the mia_hierarchy list"""
    for i in range(len(mia_hierarchy)):
        if mia_hierarchy[i] == roll:
            return i
    return -1 

def does_a_beat_b(roll_a, roll_b):
    """Compare two rolls to see if roll_a beats roll_b"""
    index_a = get_index_of_roll(roll_a)
    index_b = get_index_of_roll(roll_b)
    
    if index_a == 0:
        return True
    else:
        return index_a < index_b

def validate_claim(claim, previous_roll):
    """Validate a claimed roll and return True if valid, False otherwise"""
    claim_length = len(claim)
    if claim_length == 2:
        if claim.isdigit():
            if int(claim[0]) > 6 and int(claim[1]) > 6:
                print("Your claimed roll contains digits greater than 6")
            else:
                if int(claim[0]) >= int(claim[1]):
                    if get_index_of_roll(claim) > -1:
                        does_a_beat_b(claim, previous_roll)
                        return True
                    else:
                        return True
                else:
                    print(f"The first digit of your claim must be higher than the second (Suggestion {claim[1]}{claim[2]}")
        else:
            print("Your claimed roll must contain only numbers")
            return False
    else:
        print(f"Your claimed roll must be exactly 2 characters long. You entered {claim} (Length: {claim_length})")
        return False

def run_bluffing_phase(actual_roll, previous_roll):
    """Run the bluffing phase where players claim their rolls"""
    while True:
        print("\n=== BLUFFING PHASE ===")
        print(f"Your actual roll: {actual_roll}")
        print(f"Previous roll to beat: {previous_roll}")
        print("What roll would you like to claim?")
        
        claim = input("Enter your claimed roll: ").strip()

        if claim == actual_roll:
            print("Great you're not bluffing!")
            print("However let's still check if you're forced to bluff!")
        validate_claim(claim, previous_roll)

def print_rolls_that_beat(roll):
    """Print all rolls that can beat the given roll"""
    if roll is None:
        return
    roll_index = get_index_of_roll(roll)
    
    print(f"\nRolls that can beat {roll}:")
    
    for i in range(len(mia_hierarchy)):
        if i < roll_index:
            print(f"  {mia_hierarchy[i]}")

def play_game():
    """Handle the dice rolling game with roll comparisons and bluffing"""
    print("\n=== DICE ROLLING GAME ===")
    roll_history = ""
    
    while True:
        roll_result = roll_dice()

        previous_roll = roll_history[-2:]
        print(f"Roll History: {roll_history}")
        print(f"\nYou rolled a {roll_result}")
        if previous_roll is not None:
            print(f"\n=== ROLL COMPARISON ===")
            if does_a_beat_b(roll_result, previous_roll):
                print(f"Your roll {roll_result} BEATS your previous roll {previous_roll}!")
            else:
                print(f"Your roll {roll_result} does NOT beat your previous roll {previous_roll}.")
        else:
            print(f"\n=== FIRST ROLL ===")
            print("This is your first roll of the game!")
        
        final_claim = run_bluffing_phase(roll_result, roll_history)
        print(f"\nFinal claim: {final_claim}")
        
        print("\nWould you like to:")
        print("1. Roll again")
        print("2. Return to main menu")
        
        choice = input("Enter your choice (1-2): ").strip()
        
        if choice == "1":
            if roll_history is None:
                roll_history = roll_history + final_claim
            else:
                roll_history = roll_history + ", " + final_claim
            continue
        elif choice == "2":
            print("\nReturning to main menu...")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
            continue

def main():
    """Main menu loop"""
    while True:
        print("\n" + "="*40)
        print("MIA DICE GAME - WEEK 11".center(40))
        print("="*40)
        print("\n1. Play Game")
        print("2. See Rules")
        print("3. Exit Game")
        print("\n")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == "1":
            play_game()
        elif choice == "2":
            print_rules()
        elif choice == "3":
            print("\nThanks for playing MIA!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")
            print("Press Enter to continue...")
            input()

if __name__ == "__main__":
    print("Welcome to MIA!")
    print("\nLet's begin the game!")
    input("\nPress Enter to continue...")
    
    # Call the main() function to start the game
    main()
