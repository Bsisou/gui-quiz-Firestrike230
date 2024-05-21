from tkinter import *
import random
questions_answers = {
        1: ["What is 2 + 2?", ["Four (4)", "Five (5)", "Three (3)", "Six (6)", "Eight (8)"], "Four (4)"],
        2: ["What is 5 x 3?", ["Eight (8)", "Fifteen (15)", "Ten (10)", "Twenty (20)", "Eighteen (18)"], "Fifteen (15)"],
        3: ["What is 10 / 2?", ["Four (4)", "Two (2)", "Six (6)", "Five (5)", "Three (3)"], "Five (5)"],
        4: ["What is 8 - 4?", ["Five (5)", "Two (2)", "Three (3)", "Six (6)", "Four (4)"], "Four (4)"],
        5: ["What is 3 squared?", ["Six (6)", "Nine (9)", "Seven (7)", " Twelve (12)", "Five (5)"], "9"],
        6: ["What is the square root of 64?", ["Six (6)", "Nine (9)", "Eight (8)", "Seven (7)", "Five (5)"], "Eight (8)"],
        7: ["What is 12 x 10?", ["One-hundred and twenty (120)", "One-hundred (100)", "One-hundred and ten (110)", "One-hundred and thirty (130)", "One-hundred and five (105)"], "One-hundred and twenty (120)"],
        8: ["What is 20 / 4?", ["Four (4)", "Three (3)", "Five (5)", "Six (6)", "Two (2)"], "Five (5)"],
        9: ["What is 7 + 3?", ["Ten (10)", "Eight (8)", "Six (6)", "Twelve (12)", "Five (5)"], "Ten (10)"],
        10: ["What is 15 - 6?", ["Ten (10)", "Eight (8)", "Nine (9)", "Seven (7)", "Five (5)"], "Nine (9)"]
    }
class MathQuiz:
        def __init__(self, parent):
            self.parent = parent
            self.score = 0
            self.question_num = 0
            self.questions_order = random.sample(range(1, 11), 10)
            self.main_frame = Frame(parent, padx=20, pady=20)
            self.main_frame.pack()
            self.title_label = Label(self.main_frame, text="Welcome to Taufeeq's Math Quiz", font=("Helvetica", 16), fg="brown")
            self.title_label.grid(row=0, column=0, columnspan=2)
            self.name_label = Label(self.main_frame, text="Enter your name:")
            self.name_label.grid(row=5, column=0)
            self.name_entry = Entry(self.main_frame)
            self.name_entry.grid(row=5, column=1)
            self.start_button = Button(self.main_frame, text="Start Quiz", command=self.start_quiz, bg="green", fg="black", activebackground="light green")
            self.start_button.grid(row=8, column=0, columnspan=2, pady=10)
         
