"""log og gemes"""
import logging
from tkinter import messagebox as mb


class Datalog:
    """Create, save, show and clear log"""
    def __init__(self):
        """Create logger"""
        self.logger = logging.getLogger(__name__)

    def logger_set(self):
        """Create logger to save and output info about games"""
        self.logger.setLevel(logging.INFO)
        logger_handler = logging.FileHandler('logging.log')
        logger_handler.setLevel(logging.INFO)
        logger_formatter = logging.Formatter('%(asctime)s\n%(message)s', datefmt='%d-%b-%y %H:%M')
        logger_handler.setFormatter(logger_formatter)
        self.logger.addHandler(logger_handler)

    @staticmethod
    def show_log_file():
        """Open reed and show the logging file in little messagebox windows"""
        with open('logging.log', 'r', encoding='utf-8') as read_f:
            last_l = read_f.read()
        mb.showinfo("Players", last_l)

    @staticmethod
    def clear_log_file():
        """Clear the logging file"""
        with open('logging.log', 'w', encoding='utf-8') as clear_f:
            clear_f.write("")

    def end_game_info(self, info):
        """Show log file"""
        self.logger.info(info)
