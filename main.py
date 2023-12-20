import customtkinter as ctk
from tkinter import messagebox

class App(ctk.CTk):
    def __init__(self):

        #window
        super().__init__()
        self.geometry("450x600")
        self.title("Tic Tac Toe!")
        self.resizable(False, False)
        self._set_appearance_mode("light")
        self.iconbitmap("tictactoe.ico")

        #variables
        self.player = "X"
        self.x_winner = False
        self.o_winner = False
        self.tie = False

        #dialog box
        DialogBox(self, self.player)

        #buttons
        Buttons(self, self.player, self.x_winner, self.o_winner, self.tie)

        #mainloop
        self.mainloop()

class Buttons(ctk.CTkFrame):
    def __init__(self, parent, variable, x_winner_var, o_winner_var, tie_var):
        
        #variables setup
        self.player = variable
        self.x_winner = x_winner_var
        self.o_winner = o_winner_var
        self.tie = tie_var
        self.button_count = 0

        #frame setup
        super().__init__(parent, fg_color = "black")
        self.rowconfigure((0,1,2), weight = 1)
        self.columnconfigure((0,1,2), weight = 1)
        self.pack(expand = True, fill = "both")

        #buttons setup
        self.b1 = ctk.CTkButton(self, text = " ", 
        corner_radius = 0, 
        border_color = "black",
        border_width = 2, command = lambda: self.play(self.b1),
        font = ("Helvetica", 40, "bold"))

        self.b2 = ctk.CTkButton(self, text = " ", 
        corner_radius = 0, 
        border_color = "black",
        border_width = 2, command = lambda: self.play(self.b2),
        font = ("Helvetica", 40, "bold"))

        self.b3 = ctk.CTkButton(self, text = " ", 
        corner_radius = 0, 
        border_color = "black",
        border_width = 2, command = lambda: self.play(self.b3),
        font = ("Helvetica", 40, "bold"))

        self.b4 = ctk.CTkButton(self, text = " ", 
        corner_radius = 0, 
        border_color = "black",
        border_width = 2, command = lambda: self.play(self.b4),
        font = ("Helvetica", 40, "bold"))

        self.b5 = ctk.CTkButton(self, text = " ", 
        corner_radius = 0, 
        border_color = "black",
        border_width = 2, command = lambda: self.play(self.b5),
        font = ("Helvetica", 40, "bold"))

        self.b6 = ctk.CTkButton(self, text = " ", 
        corner_radius = 0, 
        border_color = "black",
        border_width = 2, command = lambda: self.play(self.b6),
        font = ("Helvetica", 40, "bold"))

        self.b7 = ctk.CTkButton(self, text = " ", 
        corner_radius = 0, 
        border_color = "black",
        border_width = 2, command = lambda: self.play(self.b7),
        font = ("Helvetica", 40, "bold"))

        self.b8 = ctk.CTkButton(self, text = " ", 
        corner_radius = 0, 
        border_color = "black",
        border_width = 2, command = lambda: self.play(self.b8),
        font = ("Helvetica", 40, "bold"))

        self.b9 = ctk.CTkButton(self, text = " ", 
        corner_radius = 0, 
        border_color = "black",
        border_width = 2, command = lambda: self.play(self.b9),
        font = ("Helvetica", 40, "bold"))

        #button placing
        self.b1.grid(column = 0, row = 0, sticky = "news")
        self.b2.grid(column = 1, row = 0, sticky = "news")
        self.b3.grid(column = 2, row = 0, sticky = "news")

        self.b4.grid(column = 0, row = 1, sticky = "news")
        self.b5.grid(column = 1, row = 1, sticky = "news")
        self.b6.grid(column = 2, row = 1, sticky = "news")

        self.b7.grid(column = 0, row = 2, sticky = "news")
        self.b8.grid(column = 1, row = 2, sticky = "news")
        self.b9.grid(column = 2, row = 2, sticky = "news")

    def play(self, button):
        
        if self.player == "X":
            if button.cget("text") != "O":
                button.configure(text = "X")
                self.player = "O"
                self.button_count += 1
            else:
                self.button_count += 0
                messagebox.showerror("Invalid!", "Cannot Click On The Same Button")
        else:
            if button.cget("text") != "X":
                button.configure(text = "O")
                self.player = "X"
                self.button_count += 1
            else:
                self.button_count += 0
                messagebox.showerror("Invalid!", "Cannot Click On The Same Button")

        #check if x is winner   
        if self.b1.cget("text") == "X" and self.b2.cget("text") == "X" and self.b3.cget("text") == "X":
            self.x_winner = True
        elif self.b1.cget("text") == "X" and self.b4.cget("text") == "X" and self.b7.cget("text") == "X":
            self.x_winner = True
        elif self.b2.cget("text") == "X" and self.b5.cget("text") == "X" and self.b8.cget("text") == "X":
            self.x_winner = True
        elif self.b3.cget("text") == "X" and self.b6.cget("text") == "X" and self.b9.cget("text") == "X":
            self.x_winner = True
        elif self.b1.cget("text") == "X" and self.b5.cget("text") == "X" and self.b9.cget("text") == "X":
            self.x_winner = True
        elif self.b3.cget("text") == "X" and self.b5.cget("text") == "X" and self.b7.cget("text") == "X":
            self.x_winner = True
        elif self.b4.cget("text") == "X" and self.b5.cget("text") == "X" and self.b6.cget("text") == "X":
            self.x_winner = True
        elif self.b7.cget("text") == "X" and self.b8.cget("text") == "X" and self.b9.cget("text") == "X":
            self.x_winner = True
        
        #check if y is winner
        elif self.b1.cget("text") == "O" and self.b2.cget("text") == "O" and self.b3.cget("text") == "O":
            self.o_winner = True
        elif self.b1.cget("text") == "O" and self.b4.cget("text") == "O" and self.b7.cget("text") == "O":
            self.o_winner = True
        elif self.b2.cget("text") == "O" and self.b5.cget("text") == "O" and self.b8.cget("text") == "O":
            self.o_winner = True
        elif self.b3.cget("text") == "O" and self.b6.cget("text") == "O" and self.b9.cget("text") == "O":
            self.o_winner = True
        elif self.b1.cget("text") == "O" and self.b5.cget("text") == "O" and self.b9.cget("text") == "O":
            self.o_winner = True
        elif self.b3.cget("text") == "O" and self.b5.cget("text") == "O" and self.b7.cget("text") == "O":
            self.o_winner = True
        elif self.b4.cget("text") == "O" and self.b5.cget("text") == "O" and self.b6.cget("text") == "O":
            self.o_winner = True
        elif self.b7.cget("text") == "O" and self.b8.cget("text") == "O" and self.b9.cget("text") == "O":
            self.o_winner = True
        
        #game is tie
        else:
            self.tie = True

        self.button_list = [
            self.b1,
            self.b2,
            self.b3,
            self.b4,
            self.b5,
            self.b6,
            self.b7,
            self.b8,
            self.b9
        ]

        #if x is winner show x has won and reset the game 
        if self.x_winner:
            messagebox.askokcancel("X Wins", "Congratulations X Has Won")
            for button in self.button_list:
                button.configure(text = " ")
            self.x_winner = False
            self.player = "X"
            self.button_count = 0

        #if o is winner show o has won and reset the game 
        if self.o_winner:
            messagebox.askokcancel("O Wins", "Congratulations O Has Won")
            for button in self.button_list:
                button.configure(text = " ")
            self.o_winner = False
            self.player = "X"
            self.button_count = 0

        #if game is tie, show game is tie and reset the game
        if self.tie and self.button_count == 9 and not self.x_winner and not self.o_winner:
            messagebox.askokcancel("Tie!", "The Game Is A Tie!")
            for button in self.button_list:
                button.configure(text = " ")
            self.player = "X"
            self.tie = False
            self.button_count = 0

class DialogBox(ctk.CTkFrame):
    def __init__(self, parent, player):
        super().__init__(parent, width = 400, 
                         height = 70, corner_radius = 0)
        self.pack(fill = "both")

        self.title_text = ctk.CTkLabel(self,text = "Tic Tac Toe", font = ("Helvetica", 40, "bold"))
        self.title_text.pack()

        self.info_text = ctk.CTkLabel(self,text = "X To Play First!", font = ("Helvetica", 30))
        self.info_text.pack()

App()   