"""Draw main window and control panel"""
from tkinter import Tk, IntVar, Checkbutton, Label, Entry, CENTER, SUNKEN, Button, GROOVE, DISABLED
from interaction import Interaction


class Window:
    """Window(406 x 520) with menu buttons, entry fields, labels"""

    def __init__(self, width, heght, title):
        """Constructor of variables, menu buttons and labels"""
        self.win = Tk()
        self.win.title(title)
        self.win.geometry(f"{width}x{heght}+50+50")
        self.win.resizable(False, False)
        self.win["bg"] = "white"
        self.check_first_start = 0
        self.new_interaction = Interaction()
        self.player_pos = None
        self.game_party = 0
        self.choose_sign = IntVar()
        self.x_or_0 = 0  # Checkbutton Select 0 for first move
        # two inscriptions "player-1" "player-2"
        self.lab_pleer1, self.lab_pleer2 = 0, 0
        # two fields for entering names
        self.ent_pl1, self.ent_pl2 = None, None  # create entry field player1, player2
        # main buttons - start, show_log_file, clear_log_file, quit_program
        self.start = 0
        self.show_log = 0
        self.del_log = 0
        self.exit_game = 0
        # game fields with signs
        self.s1c1, self.s1c2, self.s1c3 = None, None, None
        self.s2c1, self.s2c2, self.s2c3 = None, None, None
        self.s3c1, self.s3c2, self.s3c3 = None, None, None

    def run(self):
        """Draw main window, launch from main.py"""
        self.drow_widgets()
        self.win.mainloop()

    def drow_widgets(self):
        """Draw menu buttons and labels. (x, y) - is the pixel coordinates inside the Window"""
        # Checkbutton Select 0 for first move
        self.x_or_0 = Checkbutton(self.win, text=" Push to make the Player-2 going first."
                                                 " Its sign is 0", variable=self.choose_sign)
        # two inscriptions "player-1" "player-2"
        self.lab_pleer1 = Label(self.win, text="Player-1", font=('Vardana', 9, 'bold'), bg="white")
        self.lab_pleer2 = Label(self.win, text="Player-2", font=('Vardana', 9, 'bold'), bg="white")
        # two fields for entering names
        self.ent_pl1 = Entry(self.win, width=15, bg="#BDFFC4", fg="#180a57", font=("Verdana", 9),
                             selectbackground="#007322", selectforeground="#ffff1f",
                             justify=CENTER, relief=SUNKEN, bd=3)  # create entry field player1
        self.ent_pl2 = Entry(self.win, width=15, bg="#FEFFBD", fg="#180a57", font=("Verdana", 9),
                             selectbackground="#007322", selectforeground="#ffff1f",
                             justify=CENTER, relief=SUNKEN, bd=3)  # create entry field player2
        # main buttons - start, show_log_file, clear_log_file, quit_program
        self.start = Button(self.win, text="Start", font=('Arial', 20, "bold"), justify=CENTER,
                            command=self.input_names_check, bg="#dae0e8",
                            relief=GROOVE, bd=1, width=4, height=1)
        self.show_log = Button(self.win, text="Show victory log", font=('Arial', 12, "bold"),
                               justify=CENTER, command=self.new_interaction.showlogfile,
                               bg="#dae0e8", relief=GROOVE, bd=1, width=14, height=1)
        self.del_log = Button(self.win, text="Clean victory log", font=('Arial', 12, "bold"),
                              justify=CENTER, command=self.new_interaction.clearlogfile,
                              bg="#dae0e8", relief=GROOVE, bd=1, width=14, height=1)
        self.exit_game = Button(self.win, text="Quit", font=('Arial', 12, "bold"),
                                justify=CENTER, command=self.win.destroy, bg="#dae0e8",
                                relief=GROOVE, bd=1, width=3, height=1)

        self.start.place(x=160, y=90)
        self.show_log.place(x=10, y=45)
        self.del_log.place(x=178, y=45)
        self.exit_game.place(x=345, y=45)
        self.x_or_0.place(x=24, y=10)  # locate Checkbutton Select 0 for first move
        self.ent_pl1.place(x=15, y=110)  # locate entry field pleer1
        self.ent_pl2.place(x=260, y=110)  # locate entry field pleer2
        self.lab_pleer2.place(x=295, y=93)
        self.lab_pleer1.place(x=50, y=93)

    def start_game(self):
        """Draw main battle field, 9 squares buttons"""
        # create Tic Tac Toe field and stores the positions occupied by X and O
        self.player_pos = {'X': [], '0': []}
        self.check_first_start = 1
        self.s1c1 = Button(self.win, text="", font=('Arial', 72, "bold"), justify=CENTER,
                           command=self.push_s1c1, bg="#dae0e8",
                           relief=GROOVE, bd=1, width=2, height=1)
        self.s1c2 = Button(self.win, text="", font=('Arial', 72, "bold"), justify=CENTER,
                           command=self.push_s1c2, bg="#dae0e8",
                           relief=GROOVE, bd=1, width=2, height=1)
        self.s1c3 = Button(self.win, text="", font=('Arial', 72, "bold"), justify=CENTER,
                           command=self.push_s1c3, bg="#dae0e8",
                           relief=GROOVE, bd=1, width=2, height=1)
        self.s2c1 = Button(self.win, text="", font=('Arial', 72, "bold"), justify=CENTER,
                           command=self.push_s2c1, bg="#dae0e8",
                           relief=GROOVE, bd=1, width=2, height=0)
        self.s2c2 = Button(self.win, text="", font=('Arial', 72, "bold"), justify=CENTER,
                           command=self.push_s2c2, bg="#dae0e8",
                           relief=GROOVE, bd=1, width=2, height=0)
        self.s2c3 = Button(self.win, text="", font=('Arial', 72, "bold"), justify=CENTER,
                           command=self.push_s2c3, bg="#dae0e8",
                           relief=GROOVE, bd=1, width=2, height=0)
        self.s3c1 = Button(self.win, text="", font=('Arial', 72, "bold"), justify=CENTER,
                           command=self.push_s3c1, bg="#dae0e8",
                           relief=GROOVE, bd=1, width=2, height=0)
        self.s3c2 = Button(self.win, text="", font=('Arial', 72, "bold"), justify=CENTER,
                           command=self.push_s3c2, bg="#dae0e8",
                           relief=GROOVE, bd=1, width=2, height=0)
        self.s3c3 = Button(self.win, text="", font=('Arial', 72, "bold"), justify=CENTER,
                           command=self.push_s3c3, bg="#dae0e8",
                           relief=GROOVE, bd=1, width=2, height=0)
        self.s1c1.place(x=0, y=150)
        self.s1c2.place(x=136, y=150)
        self.s1c3.place(x=272, y=150)
        self.s2c1.place(x=0, y=274)
        self.s2c2.place(x=136, y=274)
        self.s2c3.place(x=272, y=274)
        self.s3c1.place(x=0, y=398)
        self.s3c2.place(x=136, y=398)
        self.s3c3.place(x=272, y=398)
        self.game_party = '0'
        if self.choose_sign.get():
            self.game_party = 'X'

    def input_names_check(self):
        """check for completeness of fields Player-1 and Player-2 and save them"""
        if self.new_interaction.inputnamescheck(self.ent_pl1.get(), self.ent_pl2.get()):
            self.start_game()
        else:
            if self.check_first_start != 0:  # if game didn't starting DISABLED fields
                self.block_all_field("#A1A1A1")

    def whatsigndrow(self):
        """Players take their turns depending on who made the last move"""
        return self.new_interaction.what_sign_drow(self.game_party)

    def updategameinformation(self, move):
        """update game information dict {"X or 0":[move]}"""
        self.player_pos[self.game_party].append(move)

    def push_s1c1(self):
        """Check the game winner, DISABLE field 0, update game information"""
        self.game_party = self.whatsigndrow()
        self.s1c1.config(text=self.game_party, state=DISABLED, disabledforeground="black")
        self.updategameinformation(0)
        self.verification()

    def push_s1c2(self):
        """Check the game winner, DISABLE field 1, update game information"""
        self.game_party = self.whatsigndrow()
        self.s1c2.config(text=self.game_party, state=DISABLED, disabledforeground="black")
        self.updategameinformation(1)
        self.verification()

    def push_s1c3(self):
        """Check the game winner, DISABLE field 2, update game information"""
        self.game_party = self.whatsigndrow()
        self.s1c3.config(text=self.game_party, state=DISABLED, disabledforeground="black")
        self.updategameinformation(2)
        self.verification()

    def push_s2c1(self):
        """Check the game winner, DISABLE field 3, update game information"""
        self.game_party = self.whatsigndrow()
        self.s2c1.config(text=self.game_party, state=DISABLED, disabledforeground="black")
        self.updategameinformation(3)
        self.verification()

    def push_s2c2(self):
        """Check the game winner, DISABLE field 4, update game information"""
        self.game_party = self.whatsigndrow()
        self.s2c2.config(text=self.game_party, state=DISABLED, disabledforeground="black")
        self.updategameinformation(4)
        self.verification()

    def push_s2c3(self):
        """Check the game winner, DISABLE field 5, update game information"""
        self.game_party = self.whatsigndrow()
        self.s2c3.config(text=self.game_party, state=DISABLED, disabledforeground="black")
        self.updategameinformation(5)
        self.verification()

    def push_s3c1(self):
        """Check the game winner, DISABLE field 6, update game information"""
        self.game_party = self.whatsigndrow()
        self.s3c1.config(text=self.game_party, state=DISABLED, disabledforeground="black")
        self.updategameinformation(6)
        self.verification()

    def push_s3c2(self):
        """Check the game winner, DISABLE field 7, update game information"""
        self.game_party = self.whatsigndrow()
        self.s3c2.config(text=self.game_party, state=DISABLED, disabledforeground="black")
        self.updategameinformation(7)
        self.verification()

    def push_s3c3(self):
        """Check the game winner, DISABLE field 8, update game information"""
        self.game_party = self.whatsigndrow()
        self.s3c3.config(text=self.game_party, state=DISABLED, disabledforeground="black")
        self.updategameinformation(8)
        self.verification()

    def verification(self):
        """Change bg color and deactivate fields, then show and save game info"""
        color, title, message = self.new_interaction.check_all(self.player_pos)
        if color != "":
            self.block_all_field(color)
            self.new_interaction.show_and_game_info(color, title, message)

    def block_all_field(self, color):
        """Deactivate and paint all fields in the color of winner"""
        self.s1c1.config(bg=color, state=DISABLED, disabledforeground="#A1A1A1")
        self.s1c2.config(bg=color, state=DISABLED, disabledforeground="#A1A1A1")
        self.s1c3.config(bg=color, state=DISABLED, disabledforeground="#A1A1A1")
        self.s2c1.config(bg=color, state=DISABLED, disabledforeground="#A1A1A1")
        self.s2c2.config(bg=color, state=DISABLED, disabledforeground="#A1A1A1")
        self.s2c3.config(bg=color, state=DISABLED, disabledforeground="#A1A1A1")
        self.s3c1.config(bg=color, state=DISABLED, disabledforeground="#A1A1A1")
        self.s3c2.config(bg=color, state=DISABLED, disabledforeground="#A1A1A1")
        self.s3c3.config(bg=color, state=DISABLED, disabledforeground="#A1A1A1")
