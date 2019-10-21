#
# 2019-10-21
# This is a (very) slightly modified version of the program posted at:
#   https://www.ohjelmointiputka.net/koodivinkit/25050
# by user Hassu.
#


from tkinter import *
import random

class Lotto(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.buildGUI()

    def buildGUI(self):
        # add a button in the GUI
        self.main_button = Button (self, width=20, bg="brown", fg="white", text="Draw the numbers", cursor="trek", command=self.respond)
        # make the button visible
        self.main_button.pack()

        # add a field where the numbers will be shown
        self.tulos = Label (self, bg="yellow", font=('times', 20, 'bold'), width=20, height=2)
        # make the field visible
        self.tulos.pack()

    def respond(self):
        # seven random integers from the range 1..40
        numbers = random.sample(range(1, 40), 7)
        numbers.sort()
        # show the numbers
        self.tulos.config(text=numbers)


program = Lotto()
program.master.title("Are you ready for Lotto?")
program.mainloop()
