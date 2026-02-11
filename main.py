import random

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
    number1 = random.randint(1, 6)
    number2 = random.randint(1, 6)
    if number1 > number2:
        return f"You rolled a {number1}{number2}"
    elif number2 > number1:
        return f"You rolled a {number2}{number1}"
    else:
        return f"You rolled a {number1}{number2}"
def play_game():
    while True:
        print(roll_dice())
        uin = input("Would you like to roll again? (y/n)")
        if uin == "y":
            continue
        elif uin == "n":
            break

def main():
    """Main menu loop"""
    while True:
        print("Welcome to Mia\n What would you like to do?\n 1. Roll Dice\n 2. See Rules\n 3. Exit")
        user_option = int(input(""))
        if user_option == 1:
            play_game()
        elif user_option == 2:
            print_rules()
        elif user_option == 3:
            break
        else:
            print("Please select a valid option (1-3)")
    
    pass

if __name__ == "__main__":
    print("Welcome to MIA!")
    print("\nLet's begin the game!")
    input("\nPress Enter to continue...")
    main()
