# Author: Ross Kieser
# GitHub Username: RossKieser
# Date: 8/3/2022
# Description: Ludo Board Game with 2-4 players

"""
Halfway Progress report questions
1. Determining whether you will need a board class and how to store and update the token positions with the movement of tokens
The storage of token positions will be done using the player class, with each player represented by a unique player object.
the board state for each player will be stored in the Player objects data members and updated by the LudoGame class' methods
therefore a separate board class will not be necessary.

2.Initializing the Player and LudoGame classes
The player objects will be created in the play_game method, and the player __init__ method will initialize everything
based on the chosen position on the board. most data members will be standard for all possible board positions,
so the player __init__ method will only take one parameter, player_position (A,B,C,D). The LudoGame class will be initialized
with 2  data members, a player_list and a turn_list. these data members will initially be empty and updated in the play_game method.

3. Determining how to implement get_space_name method in the Players class for different player positions
if steps = 57 return E
if steps > 50: take get_token_step_count - 50, return Letter of starting position + result as string (Ex: 'A3')
for 1-50 steps taken: for A, just return number of steps taken. For B,C,D: if starting location + steps taken < 56, return starting
location + steps taken. if > 56: return get_token_step_count- (56 - starting)+ 1

4. Determining how to implement move_token method in the LudoGame class and what parameters need to be updated after the move of the token
move tokens and update p/q_token_location based on move priority. also update steps taken for moved piece.  if the tokens go on the same space (if get_space_name is the same for both players),
either kick to home (different player) or set is_stacked to true and move both pieces in subsequent rolls.

5. Determining where to implement the priority rule and how many different cases there will be with the combinations of different token states
The priority rules will be implemented in the move_token method with the following:
- Rolled a 6
• Moving from your ‘H’ to ‘R’ is first priority (if you still have tokens in your Home Yard).
• If both tokens are in ‘H’, token ‘p’ is moved out first.
-If token is in the home square and die roll is exactly what is needed to reach the final space, move token
to final space.
-If token can move and land on opponent’s token(s), then land on opponent’s token.
-Furthest token away from final space moves

6. Determining how you will implement and use the get_token_p(q)_step_count method
the step count will have its own data member in the Player class and will update along with the position of the token.
this step count will be used by the get_space_name method to calculate which space the token is on based on the starting location.

7. Determining how you will implement the stacking state of two tokens for one player
if two tokens land on the same spot from the same player, the is_stacked data member will be set to True and both tokens will
move on subsequent rolls.
"""

class Player:
    """
    This class represents a player in the Ludo game. Each player has a certain starting position.
    The player class keeps track of the current position and state of the player.
    """

    def __init__(self, player_position):
        """
        This method initializes a Player object representing the data associated with a player in the Ludo Game.
        it contains 9 (possibly more) data members: position, start_space, end_space, p_steps,  p_token_location,
        q_steps, q_token_location, current_state, and is_stacked
        """

    def get_completed(self):
        """
        This method takes no parameters and returns true or false depending on if the player completed the game or not.
        """

    def get_token_p_step_count(self):
        """
        This method takes no parameters and returns the total number of steps token p has taken.
        """

    def get_token_q_step_count(self):
        """
        This method takes no parameters and returns the total number of steps token q has taken.
        """

    def get_space_name(self, steps):
        """
        This method takes the number of steps a token has taken as a parameter and returns the name of the space the
        token has landed on as a string
        """



class LudoGame:
    """
    This class represents the Ludo game as played. It contains information about the players and the board.
    """

    def __init__(self):
        """
        This method initializes the LudoGame object with 2 (possibly more) data members:
        turns_list and players_list when a LudoGame object is created
        """

    def play_game(self, player_list, turn_list):
        """
        This method takes two parameters: player_list and turn_list. It creates player objects based on the player_list
        passed in, moves the tokens according to the turn_list and the movement priority, updates the token position,
        updates the players game state (finished or not), and returns a list of strings representing the current
        location of all tokens in the game.
        """

    def get_player_by_position(self, player_position):
        """
        This method takes a players position (A,B,C,D) as a string as a parameter and returns that player object.
        returns Player Not Found! if no player at that position does not exist.
        """

    def move_token(self, player, token_name, steps):
        """
        This method takes three parameters: the player object, the token name (p or q), and the number of steps to take.
        it will move a single token along the board and update a tokens total steps, will kick out opponent as needed,
        and will be used by the play game method.
        """
