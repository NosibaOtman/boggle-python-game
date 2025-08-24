import tkinter as tk
from tkinter import messagebox
import boggle_board_randomizer
import ex12_utils


class Menu_GUI:
    def __init__(self):
        """
        a class that starts a window asking the player if they want to play
        """
        root = tk.Tk()
        self._root = root
        self.image = tk.PhotoImage(file="bogglewallpaper.png")
        self.canvas = tk.Canvas(self._root, width=1280, height=720)
        self.canvas.create_image(640, 360, image=self.image)
        self.canvas.pack()
        self.button = tk.Button(self.canvas, text="start here", height=2, width=30, fg="white", bg="black",
                           command=self.call, font= ("Courier", 18),relief ="raised")
        self.button.place(x=400,y=530)

        self._root.mainloop()

    def call(self):
        """
        a function that destroys the root and starts the game
        :return:
        """
        self._root.destroy()
        boggle = Boggle()
        boggle.run()


class GUI:
    def __init__(self):
        """
        a class that opens a window with the game with all the buttons, score and time.
        """
        root = tk.Tk()
        self.__time = 100
        self._root = root
        self._frame = tk.Frame(root)
        self._frame.pack()
        self._display_label = tk.Label(self._frame, font=("Courier", 14), width=18, relief="ridge",
                                       text="remaining time: 180 seconds")
        self._display_label.pack(side=tk.TOP, fill=tk.BOTH)
        self._word_label = tk.Label(self._frame, font=("Courier", 30), width=18, relief="ridge")
        self._word_label.pack(side=tk.BOTTOM, fill=tk.BOTH)
        self._score_label = tk.Label(self._frame, text="score : 0", font=("Courier", 30), width=18, relief="ridge")
        self._score_label.pack(side=tk.BOTTOM, fill=tk.BOTH)
        self._correct_words_label = tk.Label(self._frame, text="correct words: ", font=("Courier", 14), width=18,
                                             relief="ridge")
        self._correct_words_label.pack(side=tk.BOTTOM, fill=tk.BOTH)
        self._lower_frame = tk.Frame(self._frame)
        self._lower_frame.pack()
        self._buttons = dict()
        self.create_buttons()
        self.countdown()

    def des_root(self):
        self._root.destroy()

    def update_word_list(self, word_list):
        """

        :param word_list: a list of words
        :return: a label with all the guessed words
        """
        t = "correct words: "
        for w in word_list:
            t += w
            t += " "
        self._correct_words_label.destroy()
        self._correct_words_label = tk.Label(self._frame, text=t, font=("Courier", 18), width=100,
                                             relief="ridge")
        self._correct_words_label.pack(side=tk.BOTTOM, fill=tk.BOTH)

    def start(self):
        self._root.mainloop()

    def set_word(self, new_word):
        self._word_label.configure(text=new_word)

    def button_command(self, button_coordinate, cmd):
        self._buttons[button_coordinate].configure(command=lambda: cmd(button_coordinate))

    def reset_button(self, button_coordinate):
        self._buttons[button_coordinate].configure(bg="white")

    def change_button_color(self, button_coordinate):
        self._buttons[button_coordinate].configure(bg="sky blue")

    def create_buttons(self):
        """
        a function that creates the different buttons in the game
        :return: the buttons of the game
        """
        for i in range(5):
            tk.Grid.columnconfigure(self._lower_frame, i, weight=1)  # type: ignore
        for i in range(5):
            tk.Grid.rowconfigure(self._lower_frame, i, weight=1)  # type: ignore
        for i in range(4):
            for j in range(4):
                button = tk.Button(self._lower_frame, height=5, width=10, fg="black", bg="white")
                button.grid(row=i, column=j)
                self._buttons[(i, j)] = button
        self.check_word_button = tk.Button(self._lower_frame,
                                           text="check word", height=5, width=10, fg="black", bg="green")
        self.check_word_button.grid(row=0, column=5, columnspan=5)
        tk.Button(self._lower_frame, command=self._root.destroy,
                  text="Exit Game", height=5, width=10, fg="black", bg="red") \
            .grid(row=3, column=5, columnspan=5)

    def set_word_check_button(self, check_word_button_command):
        self.check_word_button.configure(command=lambda: check_word_button_command())

    def set_score(self, new_score):
        self._score_label.configure(text="score : " + str(new_score))

    def set_button_text(self, button_coordinate, text):
        self._buttons[button_coordinate].configure(text=text)

    def show_time(self):
        """
        a function that updates the remaining time on the label
        :return: none
        """
        self._display_label.destroy()
        self._display_label = tk.Label(self._frame, font=("Courier", 14), width=18, relief="ridge",
                                       text="remaining time: " + str(self.__time) + " seconds")
        self._display_label.pack(side=tk.TOP, fill=tk.BOTH)

    def bol(self):
        """
        a function that asks the player if they want to play again
        :return: a boolean value
        """
        ask_play = messagebox.askyesno("do you want to play again?", "if you want to play again click yes")
        return ask_play

    def countdown(self):
        """
        a function that reduces the time, one second at a time and when it reaches zero it asks they player if they want
        to play again
        :return: none
        """
        if self.__time == 0:
            self.play_again = self.bol()
            if self.play_again:
                self._root.destroy()
                boggle = Boggle()
                boggle.run()
            elif not self.play_again:
                self._root.destroy()
            return
        self.__time -= 1
        self.show_time()
        self._root.after(1000, self.countdown)


class Boggle:
    """
    a class that runs the game
    """
    def __init__(self):
        self.__board = boggle_board_randomizer.randomize_board()
        self.__words = ex12_utils.load_words_dict('boggle_dict.txt')
        self._boggle_gui = GUI()
        self._score = 0
        self.__path = []
        self.__correct_words = []
        self.__time = 60

    def ret_GUI(self):
        return self._boggle_gui

    def run(self):
        self.set_button_commands()
        self.set_button_text()
        self._boggle_gui.start()

    def set_button_text(self):
        """
        a function that sets the text of the buttons
        :return: none
        """
        for i in range(len(self.__board)):
            for j in range(len(self.__board)):
                self._boggle_gui.set_button_text((i, j), self.__board[i][j])

    def check_word_button_command(self):
        """
        a function that checks if the word is correct and adds to the score then adds the word to the list of correct
        words
        :return: new score, list
        """
        word = "".join([self.__board[i][j] for i, j in self.__path])
        if word not in self.__correct_words and word in self.__words:
            self._score += len(self.__path) * len(self.__path)
            self.__correct_words.append(word)
            self._boggle_gui.update_word_list(self.__correct_words)
        for button in self.__path:
            self._boggle_gui.reset_button(button)

        self.__path = []
        self._boggle_gui.set_score(self._score)
        self._boggle_gui.set_word("")

    def set_button_commands(self):
        for i in range(len(self.__board)):
            for j in range(len(self.__board)):
                self._boggle_gui.button_command((i, j), self.button_command)
        self._boggle_gui.set_word_check_button(self.check_word_button_command)

    def button_command(self, button_coordinate):
        """
        a fucntion that colors the buttons a different color if the chosen button is in the correct direction
        :param button_coordinate: the coordinates of the button
        :return: none
        """
        if self.__path:
            x, y = self.__path[-1]
            i, j = button_coordinate
            if not (abs(x - i) <= 1 and abs(y - j) <= 1):
                for button in self.__path:
                    self._boggle_gui.reset_button(button)
                self.__path = []
                self.button_command(button_coordinate)
                return
        if button_coordinate in self.__path:
            i = self.__path.index(button_coordinate)
            buttons_to_remove = self.__path[i:]
            self.__path = self.__path[:i]
            for button in buttons_to_remove:
                self._boggle_gui.reset_button(button)
        else:
            self._boggle_gui.change_button_color(button_coordinate)
            self.__path.append(button_coordinate)
        word = "".join([self.__board[i][j] for i, j in self.__path])
        self._boggle_gui.set_word(word)


if __name__ == '__main__':

        menu_gui = Menu_GUI()


