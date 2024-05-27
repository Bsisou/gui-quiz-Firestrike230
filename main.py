#Import everything from tkinter

from tkinter import messagebox
from tkinter import *
import random

#Question/Answer dictionary for math quiz program.
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

#Creating class for the Math quiz to store all the data on how the program will work
class MathQuiz:
        def __init__(self, parent):
            self.parent = parent
            self.score = 0
            self.question_num = 0
            self.questions_order = random.sample(range(1, 11), 10)
            self.main_frame = Frame(parent, padx=20, pady=20)
            self.main_frame.pack()
            self.title_label = Label(self.main_frame, text="Welcome to Taufeeq's Math Quiz", font=("Helvetica", 16), fg="brown") #title
            self.title_label.grid(row=0, column=0, columnspan=2)
            self.name_label = Label(self.main_frame, text="Enter your name:") #entry box title
            self.name_label.grid(row=5, column=0)
            self.name_entry = Entry(self.main_frame)  #entry box
            self.name_entry.grid(row=5, column=1)
            self.start_button = Button(self.main_frame, text="Start Quiz", command=self.start_quiz, bg="green", fg="black", activebackground="light green") #start quiz button
            
            self.info = Label(self.main_frame, text="This is a math quiz, it will consist of 10 questions. This should be fairly easy, good luck. Scores will be given out at the end.", wraplength=175)  #info
            self.start_button.grid(row=7, column=0, columnspan=2, pady=10, sticky="nsew")
            self.info.grid(row=8, column=0, columnspan=2, pady=10, sticky="nsew")
        def start_quiz(self): #function of the "Start Quiz" button
            if len(self.name_entry.get()) == 0:
                messagebox.showerror("Error", "Please enter your name before beginning the quiz")  #checks whether the user has entered their name or not, if not, a dialogue box appears and gives an error message to the user to put their name or they cannot proceed
                return
            self.name = self.name_entry.get()
            self.name_label.config(text=f"Welcome, {self.name}!")
            self.start_button.destroy()
            self.display_question()
        def display_question(self):   #function for displaying questions 1 by 1 after clicking "Start Quiz" button
            self.question_num += 1
            if self.question_num > 10:
                self.show_result()
                return
            question_id = self.questions_order[self.question_num - 1]
            question_data = questions_answers[question_id]
            self.correct_answer = question_data[2]
            self.main_frame.destroy()
            self.main_frame = Frame(self.parent, padx=20, pady=20)
            self.main_frame.pack()
            self.question_label = Label(self.main_frame, text=f"Question {self.question_num}: {question_data[0]}")
            self.question_label.grid(row=0, column=0, columnspan=2)
            self.var = StringVar()
            self.var.set("")
            for idx, answer in enumerate(question_data[1]):
                rb = Radiobutton(self.main_frame, text=answer, variable=self.var, value=answer)
                rb.grid(row=idx + 1, column=0, columnspan=2, sticky=W)
            self.confirm_button = Button(self.main_frame, text="Confirm", command=self.check_answer, bg="green", activebackground="light green")
            self.confirm_button.grid(row=len(question_data[1]) + 1, column=0, columnspan=2, pady=10)
        def check_answer(self): #function for checking if the answer is correct or not.
            selected_answer = self.var.get()

            if not selected_answer:
                user_response = messagebox.askquestion("Error", "Are you sure you want to skip this question?") #checks whether the user has selected a radio button as an answer or not, if not, a dialogue box appears and asks the user if they really want to skip the question or not.
                if user_response == "yes":
                    self.display_question()  # Proceed to the next question
                return
            if selected_answer == self.correct_answer:
                self.score += 1
            self.display_question() 
            selected_answer = self.var.get()
            if selected_answer == self.correct_answer:
                self.score += 1
            self.display_question()
        def show_result(self):   #function for showing result on end page to the user and their congratulations/commiseration.
            self.main_frame.destroy()
            result_frame = Frame(self.parent, padx=20, pady=20)
            result_frame.pack()
            score_label = Label(result_frame, text=f"Final Score: {self.score}")
            score_label.pack()
            if self.score < 7:
                message_label = Label(result_frame, text=f"Scored a low {self.score}, Good luck next time, {self.name}!")  #Commiseration
            else:
                message_label = Label(result_frame, text=f"Congratulations, {self.name}! You scored {self.score}!")
            message_label.pack()  #Congratulations
            close_button = Button(result_frame, text="Close", command=self.parent.destroy, bg="green", activebackground="light green")
            close_button.pack()   #closes and destroys the quiz window completely.
root = Tk()
root.title(" Taufeeq's Math Quiz")
app = MathQuiz(root)
root.mainloop()  #mainloop for the quiz, (if this was not here, quiz won't work.)
