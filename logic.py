import random

# Global Mia hierarchy list - rolls ordered from highest (index 0) to lowest
# Mia (21) is the highest, followed by doubles, then mixed rolls
mia_hierarchy = ["21", "66", "55", "44", "33", "22", "11", "65", "64", "63", "62", "61", "54", "53", "52", "51", "43", "42", "41", "32", "31"]

def roll_dice():
    """Roll two dice and return them as a string with higher roll first"""
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    
    # Compare the rolls as integers to find the higher one
    if die1 >= die2:
        # Use f-string formatting to return higher roll first
        print(f"You rolled: {die1} and {die2}")
        return f"{die1}{die2}"
    else:
        print(f"You rolled: {die2} and {die1}")
        return f"{die2}{die1}"

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
    
    # Check if claim is exactly 2 characters long
    if len(claim) != 2:
        print(f"\nInvalid claim! Your claimed roll must be exactly 2 characters long.")
        print(f"You entered: {claim} (length: {len(claim)})")
        print("Please enter a valid 2-digit roll.")
        return False
    
    # Check if claim contains only numbers
    if not claim.isdigit():
        print(f"\nInvalid claim! Your claimed roll must contain only numbers.")
        print(f"You entered: {claim}")
        print("Please enter a valid 2-digit number.")
        return False
    
    # Check if each digit is between 1-6
    if int(claim[0]) > 6 or int(claim[1]) > 6:
        print(f"\nInvalid claim! Your claimed roll contains digits greater than 6.")
        print(f"You entered: {claim} (digits: {claim[0]}, {claim[1]})")
        print("Dice only have values 1-6. Please enter a valid roll.")
        return False
    
    # Check if larger number comes first
    if int(claim[0]) < int(claim[1]):
        print(f"\nInvalid claim! Your claimed roll is {claim} but you need to have the larger number first.")
        print(f"{claim[1]} -> {claim[0]} to make your roll {claim[1]}{claim[0]} instead.")
        print("Please enter a valid roll with the larger number first.")
        return False
    
    # Check if roll exists in Mia hierarchy
    if get_index_of_roll(claim) == -1:
        print(f"\nInvalid claim! {claim} is not a valid roll.")
        print_rolls_that_beat(previous_roll)
        print("\nPlease enter a valid roll (largest number first e.g. 21 not 12).")
        return False
    elif previous_roll is None:
        print(f"\nGreat! Since this is the first roll, you can claim {claim} since it's valid!")
        return True
    elif does_a_beat_b(claim, previous_roll):
        print(f"\nGreat! Your claimed roll {claim} beats {previous_roll}!")
        return True
    else:
        print(f"\nInvalid claim! {claim} is a valid roll but does not beat {previous_roll}.")
        print_rolls_that_beat(previous_roll)
        print("\nPlease enter a valid claim that beats the previous roll.")
        return False

def print_rolls_that_beat(roll):
    """Print all rolls that can beat the given roll"""
    if roll is None:
        return
    roll_index = get_index_of_roll(roll)

    if roll == "21":
        print(f"\nThe only roll that can beat 21 (Mia) is another 21 (Mia)")
        return
    else:
        print(f"\nRolls that can beat {roll}:")
        
        for i in range(len(mia_hierarchy)):
            if i < roll_index:
                print(f"  {mia_hierarchy[i]}")

def get_index_of_roll(roll):
    """Get the index of a roll in the mia_hierarchy list"""
    for i in range(len(mia_hierarchy)):
        if mia_hierarchy[i] == roll:
            return i
    return -1
