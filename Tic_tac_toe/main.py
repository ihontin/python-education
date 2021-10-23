"""Main module start program"""
import tictaktoe
from console_version import console_version


def tictac():
    """Open GUI or console version of tic tac toe"""
    console_gui = input("c:console    g:gui").lower()
    if console_gui == "g":
        wind = tictaktoe.Window(406, 520, "Toe Tic Toe Tac")
        wind.run()
    elif console_gui == "c":
        console_version()
    else:
        print("Your game over)")



if __name__ == '__main__':
    tictac()
