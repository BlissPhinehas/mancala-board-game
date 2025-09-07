"""
File:    mancala.py
Author:  Bliss Phinehas
Date:    2025-03-27
Description:  This program implements a simple two-player Mancala game
"""

# Constants
NUM_PITS = 6
PLAYER_1_STORE = 6
PLAYER_2_STORE = 13
TOTAL_PITS = 14


def initialize_board():
    """
    Initializes the Mancala game board.

    Returns:
        list: A list representing the board with initial stone distribution.
    """
    board = [4] * NUM_PITS + [0] + [4] * NUM_PITS + [0]
    return board


def print_board(board):
    """
    Displays the current state of the Mancala board.

    Args:
        board (list): The current state of the game board.
    """
    print("\nCurrent Board:")
    print("  " + "  ".join(map(str, board[12:6:-1])) + "  ")
    print(f"{board[PLAYER_2_STORE]}                   {board[PLAYER_1_STORE]}")
    print("  " + "  ".join(map(str, board[0:6])) + "  ")
    print()

PLAYER_1_VALUE = 1
PLAYER_2_VALUE = 2

def is_valid_move(board, pit, player):
    """
    Checks whether the selected pit is a valid move for the current player.

    Args:
        board (list): The current game board.
        pit (int): The pit chosen by the player.
        player (int): The current player (PLAYER_1_VALUE or PLAYER_2_VALUE).

    Returns:
        bool: True if the move is valid, False otherwise.
    """
    # Define valid pit ranges for each player
    player_1_pits = range(0, NUM_PITS)  # Pits 0 to 5 for Player 1
    player_2_pits = range(NUM_PITS + 1, PLAYER_2_STORE)  # Pits 7 to 12 for Player 2

    if player == PLAYER_1_VALUE and pit in player_1_pits and board[pit] > 0:
        return True
    elif player == PLAYER_2_VALUE and pit in player_2_pits and board[pit] > 0:
        return True
    else:
        return False


def make_move(board, pit, player):
    """
    Executes a move and updates the board state.

    Args:
        board (list): The current game board.
        pit (int): The selected pit to play.
        player (int): The current player (1 or 2).

    Returns:
        int: The index of the last pit where a stone was placed.
    """
    stones = board[pit]
    board[pit] = 0
    current_index = pit

    while stones > 0:
        current_index = (current_index + 1) % TOTAL_PITS

        # Skip opponent's store
        if not ((player == 1 and current_index == PLAYER_2_STORE) or
                (player == 2 and current_index == PLAYER_1_STORE)):
            board[current_index] += 1
            stones -= 1

    return current_index


def check_winner(board):
    """
    Determines if the game is over and declares a winner.

    Args:
        board (list): The current game board.

    Returns:
        str: The result of the game (winner or tie), or None if the game is not over.
    """
    if sum(board[:NUM_PITS]) == 0 or sum(board[NUM_PITS + 1:PLAYER_2_STORE]) == 0:
        board[PLAYER_1_STORE] += sum(board[:NUM_PITS])
        board[PLAYER_2_STORE] += sum(board[NUM_PITS + 1:PLAYER_2_STORE])
        board[:NUM_PITS] = [0] * NUM_PITS
        board[NUM_PITS + 1:PLAYER_2_STORE] = [0] * NUM_PITS

        if board[PLAYER_1_STORE] > board[PLAYER_2_STORE]:
            return "Player 1 wins!"
        elif board[PLAYER_1_STORE] < board[PLAYER_2_STORE]:
            return "Player 2 wins!"
        return "It's a tie!"

    return None


def play_game():
    """
    Runs the main loop of the Mancala game, handling player turns and interactions.
    """
    # Prompt players for their names
    player1_name = input("Player 1, please enter your name: ")
    player2_name = input("Player 2, please enter your name: ")

    # Initialize the game board
    board = initialize_board()
    player = 1  # Player 1 starts the game
    game_over = False  # Flag to track if the game is over

    while not game_over:
        print_board(board)  # Display the current board state

        # Check if the game has ended and announce the winner
        winner = check_winner(board)
        if winner:
            print(winner)
            game_over = True  # Set flag to end the loop
        else:
            # Prompt the current player to choose a pit
            pit_valid = False
            while not pit_valid:
                if player == 1:
                    pit_input = input(f"{player1_name}, choose a pit (0-5): ")
                else:
                    pit_input = input(f"{player2_name}, choose a pit (7-12): ")

                if pit_input.isdigit():
                    pit = int(pit_input)
                    if is_valid_move(board, pit, player):
                        pit_valid = True
                    else:
                        print("Invalid move. Choose another pit.")
                else:
                    print("Invalid input. Please enter a number.")

            # Execute the move and get the index of the last pit where a stone was placed
            last_pit = make_move(board, pit, player)

            # Check if the last stone landed in the player's store; if not, switch players
            if not ((player == 1 and last_pit == PLAYER_1_STORE) or
                    (player == 2 and last_pit == PLAYER_2_STORE)):
                player = 3 - player  # Toggle between Player 1 and Player 2



# Run the game
if __name__ == "__main__":
    play_game()