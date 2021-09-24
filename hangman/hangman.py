from random import randint
import re

sum_strings = sum(1 for line in open("words.txt", 'r'))  # amount of strings in file with words
group = ""
word = "0"
words = []
end_game = 0
let_check = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
answer, an = "", ""
l_pattern = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S",
             "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M"]


def rand_word(one_str):  # assign random value to word
    num_words = one_str.strip().count(" ")
    cocount, choice_w, the_word = 0, randint(1, num_words), ""
    for fin in re.finditer(r"\w+", one_str):
        if cocount == choice_w:
            the_word = fin[0]
            break
        cocount += 1
    return the_word


def choice():  # assign random value to group of words (from txt file) and return word
    global group
    with open("words.txt", "r", encoding='utf-8') as file:
        cocount, choice_w = 0, randint(1, sum_strings)
        for i_str in file:
            cocount += 1
            if cocount == choice_w:
                group = re.search(r"\w+", i_str)[0]
                wordz = rand_word(i_str.strip().upper())
                break
    return wordz


def start_check():  # check! We mast not to play the same word twice
    wordz = choice()
    if wordz in words:
        return start_check()
    else:
        return wordz


def write_words(wo):  # Show played words
    if words:
        w_file_words(wo)
        print(*wo)
    else:
        print("No words")


def w_file_words(wo):
    wor = " ".join(wo)
    with open("played_words.txt", "w", encoding="utf-8") as filen:
        filen.write(wor)


while end_game != 3:
    w_file_words(words)
    print("1:START GAME ", " 2:SHOW and SAVE PLAYED WORDS ", " 3:END")
    mnu = int(input("CHOOSE NUMBER: "))
    if not isinstance(mnu, int) or mnu not in (1, 2, 3):
        print(f"'{mnu}' is irrelevant symbol. Try again.")
        continue
    if mnu == 3:
        end_game = 3
        break
    elif mnu == 2:
        write_words(words)
        continue
    elif mnu == 1:
        end_play = 0
        attempts = 6
        letters = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S",
                   "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M"]
        word = start_check()
        answer = "_" * len(word)
        while end_play != 3:
            if attempts == 0:
                words.append(answer)
                w_file_words(words)
                print("ATTEMPT ENDED IN FAILURE")
                input("Push any button to exit: ")
                break
            print("1:NEW GAME ", " 2:SHOW and SAVE PLAYED WORDS ", " 3:END")
            print("**************", group, "**************", f"  {attempts} attempts left")
            print(letters[0:10], f"  {letters[10:19]}", f"       {letters[19:26]}", sep="\n")
            print("****answer****", answer, "****answer****")
            print()
            letter = input("Input letter or menu number: ")
            if letter.isdigit():
                letter = int(letter)
                if letter == 1:
                    end_play = 0
                    attempts = 6
                    word = "0"
                    letters = l_pattern
                    continue
                elif letter == 2:
                    write_words(words)
                    continue
                elif letter == 3:
                    end_play = 3
                    break
                else:
                    print(f"There is no letter '{letter}' in the word, try again")
                    continue
            elif letter in let_check:
                letter = letter.upper()
                if letter not in word:
                    if letter in letters:
                        letters[letters.index(letter)] = "_"
                    attempts -= 1
                    print(f"There is no letter '{letter}' in the word, try again")
                    continue
                elif letter in word:
                    if letter in answer:
                        print(f"Letter '{letter}' is already in answer")
                        continue
                    elif letter not in answer:
                        if letter in letters:
                            letters[letters.index(letter)] = "_"
                        an = list(answer)
                        for i in range(len(word)):
                            if word[i] == letter:
                                an[i] = letter
                        answer = "".join(an)
                        if answer == word:
                            words.append(answer)
                            w_file_words(words)
                            print(f"YOU WIN! The answer is {answer}")
                            input("Push any button to exit: ")
                            break
            else:
                print(f"'{letter}' is irrelevant symbol. Try again.")
                continue
