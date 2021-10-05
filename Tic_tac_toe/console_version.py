"""Battlefield, computing, interaction with logs"""
import re
import logging


def what_sign_drow(sign_is):
    """Players take their turns depending on who made the last move"""
    if sign_is == 'X':
        return '0'
    return 'X'


def show_log_file():
    """Open reed and show the logging file in little messagebox windows"""
    with open('logging.log', 'r', encoding='utf-8') as read_f:
        last_l = read_f.read()
    print(last_l)


def clear_log_file():
    """Clear the logging file"""
    with open('logging.log', 'w', encoding='utf-8') as clear_f:
        clear_f.write("")


def show_and_game_info(winster, n_p1, n_p2, n_of_pl, n_w_score, bat_of_ga, logger):
    """Apply color to field and display message"""
    if bat_of_ga > 1 and n_p1 in n_of_pl and \
            n_p2 in n_of_pl:
        logger.info(f"'{n_p1}'  {n_w_score[n_p1]}:"
                    f"{n_w_score[n_p2]}  "
                    f"'{n_p2}'")
    else:
        if winster == "X":
            logger.info(f"'{n_p1}' win")  # save data in log file
        elif winster == "0":
            logger.info(f"'{n_p2}' win")


def check_win(p_p, cur_p):
    """Function to check if any player has won"""
    # All possible winning combinations
    win_combination = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                       [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    # Loop to check if any winning combination is satisfied
    for win in win_combination:
        if all(y in p_p[cur_p] for y in win):
            return cur_p  # Return True if any winning combination satisfies
    return False


def name_check(n_str):
    """Function checking names of players

    in the names should be numbers or/and letters
    """
    return re.search(r"\w+", n_str)


def field_check(field_input):
    """Function checking input field

    in the names should be numbers or/and letters
    """
    if field_input not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "e"):
        return False
    return True


def console_version():
    """Main function of console version of tic tac toe
    we playing here
    """
    name_player1, name_player2 = " ", " "
    batch_of_game = 0
    names_of_players, name_and_win_score = [], {}
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger_handler = logging.FileHandler('logging.log')
    logger_handler.setLevel(logging.INFO)
    logger_formatter = logging.Formatter('%(asctime)s\n%(message)s', datefmt='%d-%b-%y %H:%M')
    logger_handler.setFormatter(logger_formatter)
    logger.addHandler(logger_handler)

    while True:
        menu = input("s:start   l:show log   c:cliar log "
                     " e:enter new names  q:quit \nEnter: ").lower()
        if menu not in ("s", "l", "c", "e", "q"):
            print("menu have only 5 commands s, l, c, e, q. Try again")
            continue
        if menu == "s":
            if name_check(name_player1) is None or name_check(name_player2) is None:
                print("Enter players names first.")
                continue
            player_pos = {'X': [], '0': []}
            player_sign = "0"
            field = ["_"] * 9
            while True:
                print(field[0:3], field[3:6], field[6:9], sep="\n")
                if player_sign == "0":
                    field_num = input(f"Player-{name_player1}\n"
                                      f"Enter field number 1-9 or 'e':exit to main menu: ").lower()
                else:
                    field_num = input(f"Player-{name_player2}\n"
                                      f"Enter field number 1-9 or 'e':exit to main menu: ").lower()
                if not field_check(field_num):
                    print("Invalid value entered. Please try again.")
                    continue
                if field_num == "e":
                    break
                field_num = int(field_num)
                move = field_num - 1
                if field[move] != "_":
                    print(f"Field is busy by {field[move]}")
                    continue
                player_sign = what_sign_drow(player_sign)
                field[move] = player_sign
                player_pos[player_sign].append(move)
                player_winner = check_win(player_pos, player_sign)
                if player_winner:
                    if name_player1 not in names_of_players:
                        names_of_players.append(name_player1)
                        name_and_win_score[name_player1] = 0
                    if name_player2 not in names_of_players:
                        names_of_players.append(name_player2)
                        name_and_win_score[name_player2] = 0
                    if player_winner == "X":
                        name_and_win_score[name_player1] += 1
                        print(field[0:3], field[3:6], field[6:9], sep="\n")
                        input(f"Player {name_player1} win! Press 'Enter' to exit.")
                        batch_of_game += 1
                        show_and_game_info(player_winner, name_player1, name_player2,
                                           names_of_players, name_and_win_score,
                                           batch_of_game, logger)
                        break
                    if player_winner == "0":
                        name_and_win_score[name_player2] += 1
                        print(field[0:3], field[3:6], field[6:9], sep="\n")
                        input(f"Player {name_player2} win! Press 'Enter' to exit.")
                        batch_of_game += 1
                        show_and_game_info(player_winner, name_player1, name_player2,
                                           names_of_players, name_and_win_score,
                                           batch_of_game, logger)
                        break
                if "_" not in field:
                    input("DROW! Game Over! Press 'Enter' to exit.")
                    break
        elif menu == "e":
            batch_of_game = 0
            name_player1 = input("Enter player1 name using only letters and numbers: ")
            name_player2 = input("Enter player2 name using only letters and numbers: ")
            if name_check(name_player1) is None or name_check(name_player2) is None:
                print("Invalid value entered. Please try again.")
                continue
        elif menu == "l":
            if name_check(name_player1) is None or name_check(name_player2) is None:
                print("Please start the game first and enter names of pleers.")
                continue
            show_log_file()
        elif menu == "c":
            clear_log_file()
        if menu == "q":
            break
