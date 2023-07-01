import tkinter as tk
from tkinter import Tk,PhotoImage,Canvas
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score = tk.Label(
            text="Score: 0",
            fg='white',
            background=THEME_COLOR,
            font=('Arial',15,'bold'))
        self.score.grid(row=0,column=1)
        self.canvas = Canvas(width=300,height=250,bg="white")
        self.question = self.canvas.create_text(
            150,
            125,
            font=('Arial',15,'italic'),
            fill=THEME_COLOR,
            text="some text",
            width=290,
            )
        self.canvas.grid(row=1,column=0,columnspan=2,pady=20)

        self.good = PhotoImage(file="./trivia_quiz/images/true.png")
        self.g_button = tk.Button(image=self.good,highlightthickness=0,borderwidth=0,command=self.correct)
        self.g_button.grid(row=2,column=0)
        self.wrong = PhotoImage(file="./trivia_quiz/images/false.png")
        self.w_button = tk.Button(image=self.wrong,highlightthickness=0,borderwidth=0,command=self.fail)
        self.w_button.grid(row=2,column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            print("Questions remaining")
            self.score["text"] = f"Score: {self.quiz.score}"
            self.canvas.itemconfig(self.question,fill=THEME_COLOR)
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question,text=q_text)
        else:
            print("No more questions")
            self.canvas.itemconfig(self.question,text="You've reached the end of the quiz.",fill=THEME_COLOR)
            self.w_button.config(state="disabled")
            self.g_button.config(state="disabled")
    def correct(self):
        self.feedback(self.quiz.check_answer("True"))
    def fail(self):
        self.feedback(self.quiz.check_answer("False"))
    def feedback(self,is_right):
        if is_right==True:
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.question,fill="white")
        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.question,fill="white")
        self.window.after(1000,self.get_next_question)
