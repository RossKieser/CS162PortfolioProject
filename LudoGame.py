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
if steps = -1 return H
if steps = 0 return R
if steps = 57 return E
if steps > 50 and steps < 57: take get_token_step_count - 50, return Letter of starting position + result as string (Ex: 'A3')
for 1-50 steps taken: for A, just return number of steps taken. For B,C,D: if starting location + steps taken <= 56, return starting
location + steps taken - 1. if = 57: return 56. if > 57: return steps_taken - (56 - starting space + 1)

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
        it contains 10 (possibly more) data members: position, start_space, end_space, p_steps,  p_token_location,
        q_steps, q_token_location, current_state, is_stacked, finished_space
        """
        self._position = player_position
        if self._position == "A":
            self._start_space = 1
            self._end_space = 50
        elif self._position == "B":
            self._start_space = 15
            self._end_space = 8
        elif self._position == "C":
            self._start_space = 29
            self._end_space = 22
        elif self._position == "D":
            self._start_space = 43
            self._end_space = 36
        self._p_steps = 0
        self._p_token_location = "H"
        self._q_steps = 0
        self._q_token_location = "H"
        self._current_state = "Playing"
        self._is_stacked = False
        self._finished_space = "E"

    def get_position(self):
        """
        This method takes no parameters and returns the position of the player
        """
        return self._position

    def get_completed(self):
        """
        This method takes no parameters and returns true or false depending on if the player completed the game or not.
        """
        if self._current_state == "Won":
            return True
        elif self._current_state == "Playing":
            return False

    def set_completed(self, current_state):
        """
        This method takes one parameter (current_state) and sets the _current_state data member accordingly.
        """
        self._current_state = current_state

    def get_is_stacked(self):
        """
        This method takes no parameters and returns whether or not the players tokens are stacked.
        """
        return self._is_stacked

    def set_is_stacked(self, is_stacked):
        """
        This method takes one parameter (is_stacked) and sets the _is_stacked data member accordingly.
        """
        self._is_stacked = is_stacked


    def get_token_p_step_count(self):
        """
        This method takes no parameters and returns the total number of steps token p has taken.
        """
        return self._p_steps

    def get_token_q_step_count(self):
        """
        This method takes no parameters and returns the total number of steps token q has taken.
        """
        return self._q_steps

    def set_token_p_step_count(self, p_steps):
        """
        This method takes a number of steps as a parameter and increments (or decrements if negative parameter)
        the token_step_count. it then calls set_p_space_name with the new p_space to update the current space.
        """
        if p_steps == "Home":
            self._p_steps = -1
        elif p_steps == "Ready":
            self._p_steps = 0
        else:
            self._p_steps = self._p_steps + p_steps
            if (self._p_steps > 57) and (self._p_steps <= 62):
                kickback = (self._p_steps - 57)
                if kickback == 1:
                    self._p_steps = 56
                elif kickback == 2:
                    self._p_steps = 55
                elif kickback == 3:
                    self._p_steps = 54
                elif kickback == 4:
                    self._p_steps = 53
                elif kickback == 5:
                    self._p_steps = 52
        self.set_p_space_name(self._p_steps)

    def set_token_q_step_count(self, q_steps):
        """
        This method takes a number of steps as a parameter and increments (or decrements if negative parameter)
        the token_step_count. it then calls set_q_space_name with the new q_space to update the current space.
        """
        if q_steps == "Home":
            self._q_steps = -1
        elif q_steps == "Ready":
            self._q_steps = 0
        else:
            self._q_steps = self._q_steps + q_steps
            if (self._q_steps > 57) and (self._q_steps <= 62):
                kickback = (self._q_steps - 57)
                if kickback == 1:
                    self._q_steps = 56
                elif kickback == 2:
                    self._q_steps = 55
                elif kickback == 3:
                    self._q_steps = 54
                elif kickback == 4:
                    self._q_steps = 53
                elif kickback == 5:
                    self._q_steps = 52
        self.set_q_space_name(self._q_steps)

    def get_p_space_name(self):
        """
        This method returns the name of the space the p token is currently on as a string.
        """
        return self._p_token_location

    def get_q_space_name(self):
        """
        This method returns the name of the space the token is currently on as a string.
        """
        return self._q_token_location

    def get_space_name(self, total_steps):
        """
        This method takes the total steps moved and returns the name of the space landed on based on starting location.
        """
        if total_steps == -1:
            return "H"
        elif total_steps == 0:
            return "R"
        elif total_steps == 57:
            return "E"
        elif (total_steps > 50) and (total_steps < 57):
            number = total_steps - 50
            return self._position + str(number)
        elif (total_steps >= 1) and (total_steps <= 50):
            if self._position == "A":
                return total_steps
            else:
                if (self._start_space + total_steps) <= 56:
                    return self._start_space + total_steps - 1
                elif (self._start_space + total_steps) == 57:
                    return 56
                elif (self._start_space + total_steps) > 57:
                    return total_steps - (56 - self._start_space + 1)
        else:
            pass

    def set_p_space_name(self, p_steps):
        """
        This method takes the number of steps the p token has taken as a parameter and sets the name of the current token location.
        """
        if p_steps == -1:
            self._p_token_location = "H"
        elif p_steps == 0:
            self._p_token_location = "R"
        elif p_steps == 57:
            self._p_token_location = "E"
        elif (p_steps > 50) and (p_steps < 57):
            number = p_steps - 50
            self._p_token_location = self._position + str(number)
        elif (p_steps >= 1) and (p_steps <= 50):
            if self._position == "A":
                self._p_token_location = p_steps
            else:
                if (self._start_space + p_steps) <= 56:
                    self._p_token_location = self._start_space + p_steps - 1
                elif (self._start_space + p_steps) == 57:
                    self._p_token_location = 56
                elif (self._start_space + p_steps) > 57:
                    self._p_token_location = p_steps - (56 - self._start_space + 1)
        else:
            pass

    def set_q_space_name(self, q_steps):
        """
        This method takes the number of steps the p token has taken as a parameter and sets the name of the current token location.
        """
        if q_steps == -1:
            self._q_token_location = "H"
        elif q_steps == 0:
            self._q_token_location = "R"
        elif q_steps == 57:
            self._q_token_location = "E"
        elif (q_steps > 50) and (q_steps < 57):
            number = q_steps - 50
            self._q_token_location = self._position + str(number)
        elif (q_steps >= 1) and (q_steps <= 50):
            if self._position == "A":
                self._q_token_location = q_steps
            else:
                if (self._start_space + q_steps) <= 56:
                    self._q_token_location = self._start_space + q_steps - 1
                elif (self._start_space + q_steps) == 57:
                    self._q_token_location = 56
                elif (self._start_space + q_steps) > 57:
                    self._q_token_location = q_steps - (56 - self._start_space + 1)
        else:
            pass


class LudoGame:
    """
    This class represents the Ludo game as played. It contains information about the players and the board.
    """

    def __init__(self):
        """
        This method initializes the LudoGame object with 2 (possibly more) data members:
        turns_list and players_list when a LudoGame object is created
        """
        self._turns_list = []
        self._players_list = []

    def get_turns_list(self):
        """
        This method returns the turns_list of the current LudoGame
        """
        return self._turns_list

    def get_players_list(self):
        """
        This method returns the players_list of the current LudoGame
        """
        return self._players_list

    def play_game(self, player_list, turn_list):
        """
        This method takes two parameters: player_list and turn_list. It creates player objects based on the player_list
        passed in, moves the tokens according to the turn_list and the movement priority, updates the token position,
        updates the players game state (finished or not), and returns a list of strings representing the current
        location of all tokens in the game.
        """
        for player in player_list:                          # create a player object and save to _players_list data member
            self.get_players_list().append(Player(player))
        for turn in turn_list:                              # append each turn tuple (player, roll) to _turns_list data member
            self.get_turns_list().append(turn)
        for turn in self.get_turns_list():                  # iterate through every turn tuple in _turns_list
            current_player_position = turn[0]               # extract which player is currently moving from the turn tuple
            current_player = self.get_player_by_position(current_player_position)   # get the current player object via get_player_by_position
            if current_player != "Player not found!":                               # continue the current iteration only if an active player object is found
                if current_player.get_completed() == False:                         # If the current player has already finished, move to next turn
                    current_roll = turn[1]
                    if current_roll == 6:                                                   # if a 6 is rolled, the highest priority is moving from home
                        if current_player.get_p_space_name() == "H":
                            self.move_token(current_player, "p", "Ready")
                        elif current_player.get_q_space_name() == "H":                      # Move p or q out of home if possible
                            self.move_token(current_player, "q", "Ready")
                        elif current_player.get_token_p_step_count() == 51:
                            self.move_token(current_player, "p", 6)
                        elif current_player.get_token_q_step_count() == 51:                 # Move p or q to E if 6 away from goal (E)
                            self.move_token(current_player, "q", 6)
                        elif self.target_in_range(current_player, 6) == (True, "p"):        # move p or q if within range to knock back opponent to home
                            self.move_token(current_player, "p", 6)
                            for player in self.get_players_list():                          # Kick all pieces back home landed on by current player
                                if player != current_player:
                                    if current_player.get_space_name(current_player.get_token_p_step_count()) == player.get_space_name(player.get_token_p_step_count()):
                                        self.move_token(player, "p", "Home")
                                    if current_player.get_space_name(current_player.get_token_p_step_count()) == player.get_space_name(player.get_token_q_step_count()):
                                        self.move_token(player, "q", "Home")
                        elif self.target_in_range(current_player, 6) == (True, "q"):        # move p or q if within range to knock back opponent to home
                            self.move_token(current_player, "q", 6)
                            for player in self.get_players_list():                          # Kick all pieces back home landed on by current player
                                if player != current_player:
                                    if current_player.get_space_name(current_player.get_token_q_step_count()) == player.get_space_name(player.get_token_p_step_count()):
                                        self.move_token(player, "p", "Home")
                                    if current_player.get_space_name(current_player.get_token_q_step_count()) == player.get_space_name(player.get_token_q_step_count()):
                                        self.move_token(player, "q", "Home")
                        elif current_player.get_token_p_step_count() <= current_player.get_token_q_step_count():
                            self.move_token(current_player, "p", 6)
                        elif current_player.get_token_p_step_count() > current_player.get_token_q_step_count():     # Move whichever token is furthest from the end
                            self.move_token(current_player, "q", 6)
                    else:
                        if current_player.get_token_p_step_count() == 57 - current_roll:                            # Move token if one can move exactly to goal (E)
                            self.move_token(current_player, "p", current_roll)
                        elif current_player.get_token_q_step_count() == 57 - current_roll:
                            self.move_token(current_player, "q", current_roll)
                        elif self.target_in_range(current_player, current_roll) == (True, "p"):                     # move p or q if within range to knock back opponent to home
                            self.move_token(current_player, "p", current_roll)
                            for player in self.get_players_list():                                                  # Kick all pieces back home landed on by current player
                                if player != current_player:
                                    if current_player.get_space_name(current_player.get_token_p_step_count()) == player.get_space_name(player.get_token_p_step_count()):
                                        self.move_token(player, "p", "Home")
                                    if current_player.get_space_name(current_player.get_token_p_step_count()) == player.get_space_name(player.get_token_q_step_count()):
                                        self.move_token(player, "q", "Home")
                        elif self.target_in_range(current_player, current_roll) == (True, "q"):                     # move p or q if within range to knock back opponent to home
                            self.move_token(current_player, "q", current_roll)
                            for player in self.get_players_list():                                                  # Kick all pieces back home landed on by current player
                                if player != current_player:
                                    if current_player.get_space_name(current_player.get_token_q_step_count()) == player.get_space_name(player.get_token_p_step_count()):
                                        self.move_token(player, "p", "Home")
                                    if current_player.get_space_name(current_player.get_token_q_step_count()) == player.get_space_name(player.get_token_q_step_count()):
                                        self.move_token(player, "q", "Home")
                        elif current_player.get_token_p_step_count() <= current_player.get_token_q_step_count():
                            if current_player.get_p_space_name() != "H":
                                self.move_token(current_player, "p", current_roll)
                        elif current_player.get_token_p_step_count() > current_player.get_token_q_step_count():     # Move whichever token is furthest from the end
                            if current_player.get_q_space_name() != "H":
                                self.move_token(current_player, "q", current_roll)
        current_positions = []
        for player in self.get_players_list():
            current_positions.append(player.get_p_space_name())
            current_positions.append(player.get_q_space_name())
        return current_positions




    def target_in_range(self, current_player, roll):
        """
        This method takes two parameters (current_player object, and roll) and returns True/False and which token is in range based on if a token is within range to return another player back to home or not
        """
        for player in self.get_players_list():
            if player != current_player:
                if (current_player.get_space_name(current_player.get_token_p_step_count()+roll) == player.get_space_name(player.get_token_p_step_count()+roll)) or (current_player.get_space_name(current_player.get_token_p_step_count()+roll) == player.get_space_name(player.get_token_q_step_count()+roll)):
                    return True, "p"
                elif (current_player.get_space_name(current_player.get_token_q_step_count()+roll) == player.get_space_name(player.get_token_p_step_count()+roll)) or (current_player.get_space_name(current_player.get_token_q_step_count()+roll) == player.get_space_name(player.get_token_q_step_count()+roll)):
                    return True, "q"
        return False, None



    def get_player_by_position(self, player_position):
        """
        This method takes a players position (A,B,C,D) as a string as a parameter and returns that player object.
        returns Player Not Found! if no player at that position does not exist.
        """
        for player in self.get_players_list():
            if player.get_position() == player_position:
                return player
        return "Player not found!"

    def move_token(self, player, token_name, steps):
        """
        This method takes three parameters: the player object, the token name (p or q), and the number of steps to take.
        it will move a single token along the board and update a tokens total steps, will kick out opponent as needed,
        and will be used by the play game method.
        """

        if player.get_is_stacked() == True:
            player.set_token_p_step_count(steps)
            player.set_token_q_step_count(steps)
        elif token_name == "p":
            player.set_token_p_step_count(steps)
        elif token_name == "q":
            player.set_token_q_step_count(steps)

        if (player.get_token_p_step_count() == 57) and (player.get_token_q_step_count() == 57):
            player.set_completed("Won")

        if (player.get_token_p_step_count() <= 0) or (player.get_token_q_step_count() <= 0):
            player.set_is_stacked(False)
        elif (player.get_p_space_name() == player.get_q_space_name()):
            player.set_is_stacked(True)

        print(player.get_p_space_name())
        print(player.get_q_space_name())
        print("")


