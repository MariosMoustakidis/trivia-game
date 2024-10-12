from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz=quiz_brain
        self.window = Tk()
        self.window.title("Quizz")
        self.window.config(padx= 20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 20))
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.q_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true = Button(image=true_image, highlightthickness=0, command=self.send_true)
        self.true.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false = Button(image=false_image, highlightthickness=0, command=self.send_false)
        self.false.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.q_text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.q_text, text=f"You have reached the end of the quiz with a score of {self.quiz.score}/10.")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def send_true(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def send_false(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
