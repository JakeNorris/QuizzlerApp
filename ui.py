from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    # Set the quiz_brain data type to only allow QuizBrain objects.
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # Create window.
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        # Create the Canvas and its text item.
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     text="Some Question text",
                                                     font=("Arial", 20, "italic"),
                                                     width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        # Create true button and set the image to the green check mark.
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)
        # Create the false button and set the image to the red x.
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)
        # Create the score label.
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        # Call the get_next_question method so the canvas text isn't blank.
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        # Utilize the QuizBrain method to check an answer that returns a boolean value.
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        # Utilize the QuizBrain method to check an answer that returns a boolean value.
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
