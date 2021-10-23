"""Battlefield, computing, interaction with logs"""
from tkinter import messagebox as mb
from data_log import Datalog


class Interaction:
    """Gives the commands to create, save, and show logs, handles button presses"""

    def __init__(self):
        """Create logger initiate players names"""
        self.new_log = Datalog()
        self.new_log.logger_set()
        self.names_of_players, self.name_and_win_score = [], {}
        self.batch_of_game = 0
        self.player_1_name, self.player_2_name = "", ""

    def showlogfile(self):
        """if we wont to see the log, we need to fill in entry fields"""
        if self.player_1_name in self.names_of_players and self.player_2_name in \
                self.names_of_players and len(self.player_1_name) != 0 or \
                len(self.player_2_name) != 0:
            self.new_log.show_log_file()
        else:
            mb.showinfo("Players", "Fill in both fields\nPlayer-1 and Player -2")

    def clearlogfile(self):
        """Clear the log file"""
        self.new_log.clear_log_file()

    def inputnamescheck(self, check1, check2):
        """check for completeness of fields Player-1 and Player-2 and save them"""
        self.player_1_name = check1
        self.player_2_name = check2
        if len(self.player_1_name) == 0 or len(self.player_2_name) == 0:
            mb.showinfo("Before playing:", "Fill in both fields\nPlayer-1 and Player -2")
            return False
        if self.player_1_name not in self.names_of_players:
            self.names_of_players.append(self.player_1_name)
            self.name_and_win_score[self.player_1_name] = 0
        if self.player_2_name not in self.names_of_players:
            self.names_of_players.append(self.player_2_name)
            self.name_and_win_score[self.player_2_name] = 0
        return True  # Game start function

    @staticmethod
    def what_sign_drow(sign):
        """Players take their turns depending on who made the last move"""
        if sign == 'X':
            return '0'
        return 'X'

    def check_all(self, position):
        """Function to check all variants ending of the game"""
        nobody_win = 0
        if self.check_win(position, 'X'):
            self.name_and_win_score[self.player_1_name] += 1
            nobody_win += 1
            return "#BDFFC4", "WINNER", "Player-1 WIN!  "
        if self.check_win(position, '0'):
            self.name_and_win_score[self.player_2_name] += 1
            nobody_win += 1
            return "#FEFFBD", "WINNER", "Player-2 WIN!  "
        # Function call for checking draw game
        if self.check_draw(position) and nobody_win == 0:
            return "#A1A1A1", "Game Drawn", "lats play again!   "
        return "", "", ""

    def show_and_game_info(self, color, title, message):
        """Apply color to field and display message"""
        self.batch_of_game += 1
        mb.showinfo(title, message)
        if self.batch_of_game > 1 and self.player_1_name in self.names_of_players and \
                self.player_2_name in self.names_of_players:
            self.new_log.end_game_info(f"'{self.player_1_name}' "
                                       f"{self.name_and_win_score[self.player_1_name]}:"
                                       f"{self.name_and_win_score[self.player_2_name]} "
                                       f"'{self.player_2_name}'")
        else:
            if color == "#BDFFC4":
                self.new_log.end_game_info(f"'{self.player_1_name}' win")  # save data in log file
            elif color == "#FEFFBD":
                self.new_log.end_game_info(f"'{self.player_2_name}' win")

    @staticmethod
    def check_win(player_pos, cur_player):
        """Function to check if any player has won"""
        # All possible winning combinations
        win_combination = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                           [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        # Loop to check if any winning combination is satisfied
        for win in win_combination:
            if all(y in player_pos[cur_player] for y in win):
                return True  # Return True if any winning combination satisfies
        return False

    @staticmethod
    def check_draw(player_pos):
        """Function to check if the game is drawn"""
        if len(player_pos['X']) + len(player_pos['0']) == 9:
            return True
        return False
