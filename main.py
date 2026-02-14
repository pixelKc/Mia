from screens import *

def play_game():
    """Handle the two-player dice rolling game with roll comparisons and bluffing"""
    # Initialize two-player game state variables
    player1_score = 0
    player2_score = 0
    current_player = 1
    roll_history = ""  # Track all rolls in the current game session (e.g., "63, 55, 66")
    game_over = False
    
    # Main game loop - continues until game_over is True
    while not game_over:
        # Display roll dice screen
        print_roll_dice_screen(current_player, player1_score, player2_score, roll_history)
        
        # Display make claim screen and get actual and claimed rolls
        actual_roll, claimed_roll = print_make_claim_screen(current_player, roll_history)
        
        # Update roll history with the claimed roll
        if roll_history == "":
            roll_history = claimed_roll
        else:
            roll_history = f"{roll_history}, {claimed_roll}"
        
        if current_player == 1:
            current_player = 2
        else:
            current_player = 1
        
        player1_score, player2_score = print_player_transition_screen(current_player, player1_score, player2_score, roll_history)
        if isGameOver(player1_score, player2_score):
            print_game_over()
        else:
            roll_history = ""
            

def main():
    """Main menu loop"""
    while True:
        print_main_menu()
        choice = input("Enter your choice (1-3): ").strip()
            
        if choice == "1":
            play_game()
        elif choice == "2":
            print_rules_screen()
        elif choice == "3":
            print("\nThanks for playing MIA!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")
            print("Press Enter to continue...")
            input()

if __name__ == "__main__":
    main()
