import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style

# Define the questions and answers
quiz_data = [
    {
        "question": "What is the time complexity of a binary search algorithm?",
        "choices": [
            "A. O(log n)",
            "B. O(n)",
            "C. O(n^2)",
            "D. O(1)"
        ],
        "answer": "A. O(log n)"
    },
    {
        "question": "Which data structure uses a Last-In-First-Out (LIFO) order?",
        "choices": [
            "A. Queue",
            "B. Linked List",
            "C. Stack",
            "D. Tree"
        ],
        "answer": "C. Stack"
    },
    {
        "question": "What does the acronym 'HTTP' stand for?",
        "choices": [
            "A. Hypertext Transfer Protocol",
            "B. High-Tech Transfer Protocol",
            "C. Hyperlink and Text Transfer Protocol",
            "D. Host and Text Transfer Protocol"
        ],
        "answer": "A. Hypertext Transfer Protocol"
    },
    {
        "question": "In object-oriented programming, what is encapsulation?",
        "choices": [
            "A. A process of reducing code duplication",
            "B. A way to define variables in a class",
            "C. Binding of data and methods that operate on the data",
            "D. A type of data structure"
        ],
        "answer": "C. Binding of data and methods that operate on the data"
    },
    {
        "question": "Which programming language is often used for web development and server-side scripting?",
        "choices": [
            "A. Java",
            "B. C++",
            "C. Python",
            "D. PHP"
        ],
        "answer": "D. PHP"
    },
    {
        "question": "What is the purpose of the 'git' version control system?",
        "choices": [
            "A. To write and execute code",
            "B. To manage and track changes in code",
            "C. To test and debug code",
            "D. To design user interfaces"
        ],
        "answer": "B. To manage and track changes in code"
    },
    {
        "question": "Which sorting algorithm has the best average-case time complexity?",
        "choices": [
            "A. Bubble Sort",
            "B. Insertion Sort",
            "C. Merge Sort",
            "D. Selection Sort"
        ],
        "answer": "C. Merge Sort"
    },
    {
        "question": "What is the main purpose of an API (Application Programming Interface)?",
        "choices": [
            "A. To create user interfaces",
            "B. To provide a way for different software components to communicate",
            "C. To run background processes",
            "D. To manage file storage"
        ],
        "answer": "B. To provide a way for different software components to communicate"
    },
    {
        "question": "In Python, what is the difference between '==' and 'is' when comparing objects?",
        "choices": [
            "A. '==' compares values, 'is' compares memory addresses",
            "B. '==' compares memory addresses, 'is' compares values",
            "C. They are equivalent and can be used interchangeably",
            "D. '==' is used for string comparison, 'is' is used for integer comparison"
        ],
        "answer": "A. '==' compares values, 'is' compares memory addresses"
    },
    {
        "question": "Which data structure is used to implement a First-In-First-Out (FIFO) order?",
        "choices": [
            "A. Queue",
            "B. Stack",
            "C. Hash Table",
            "D. Linked List"
        ],
        "answer": "A. Queue"
    }
]

# Function to display the current question and choices
def show_question():
    question = quiz_data[current_question]
    qs_label.config(text=question["question"])

    choices = question["choices"]
    for i in range(4):
        choice_btns[i].config(text=choices[i], state="normal")
    
    feedback_label.config(text="")
    next_btn.config(state="disabled")

# Function to check the selected answer and provide feedback
def check_answer(choice):
    question = quiz_data[current_question]
    selected_choice = choice_btns[choice].cget("text")

    if selected_choice == question["answer"]:
        global score
        score += 1
        score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))
        feedback_label.config(text="Correct!", foreground="green")
    else:
        feedback_label.config(text="Incorrect!", foreground="red")
    
    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal")

# Function to move to the next question
def next_question():
    global current_question
    current_question +=1

    if current_question < len(quiz_data):
        show_question()
    else:
        messagebox.showinfo("Quiz Completed",
                            "Quiz Completed! Final score: {}/{}".format(score, len(quiz_data)))
        root.destroy()

# Create the main window
root = tk.Tk()
root.title("Quiz App")
root.geometry("600x500")
style = Style(theme="flatly")

# Configure the font size for the question and choice buttons
style.configure("TLabel", font=("Helvetica", 20))
style.configure("TButton", font=("Helvetica", 16))

# Create the question label
qs_label = ttk.Label(
    root,
    anchor="center",
    wraplength=500,
    padding=10
)
qs_label.pack(pady=10)

# Create the choice buttons
choice_btns = []
for i in range(4):
    button = ttk.Button(
        root,
        command=lambda i=i: check_answer(i)
    )
    button.pack(pady=5)
    choice_btns.append(button)

# Create the feedback label
feedback_label = ttk.Label(
    root,
    anchor="center",
    padding=10
)
feedback_label.pack(pady=10)

# Initialize the score
score = 0

# Create the score label
score_label = ttk.Label(
    root,
    text="Score: 0/{}".format(len(quiz_data)),
    anchor="center",
    padding=10
)
score_label.pack(pady=10)

# Create the next button
next_btn = ttk.Button(
    root,
    text="Next",
    command=next_question,
    state="disabled"
)
next_btn.pack(pady=10)

# Initialize the current question index
current_question = 0

# Show the first question
show_question()

# Start the main event loop
root.mainloop()
