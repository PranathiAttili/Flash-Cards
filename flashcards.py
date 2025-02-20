import tkinter as tk
from tkinter import messagebox
import random
flashcards = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "Who wrote 'Romeo and Juliet'?", "answer": "William Shakespeare"},
    {"question": "What is the square root of 64?", "answer": "8"},
    {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
    {"question": "Who painted the Mona Lisa?", "answer": "Leonardo da Vinci"}
]
current_card = None
score = 0
question_index = 0
def start_quiz():
    """Initialize quiz and show first question."""
    global score, question_index
    score = 0
    question_index = 0
    random.shuffle(flashcards)
    next_question()

def next_question():
    """Load the next flashcard question."""
    global current_card, question_index
    
    if question_index < len(flashcards):
        current_card = flashcards[question_index]
        question_label.config(text=current_card["question"])
        answer_entry.delete(0, tk.END)
        question_index += 1
    else:
        show_results()

def check_answer():
    """Check user's answer and update score."""
    global score
    user_answer = answer_entry.get().strip().lower()
    
    if user_answer == current_card["answer"].lower():
        score += 1
    
    next_question()

def show_results():
    """Display final quiz score."""
    messagebox.showinfo("Quiz Complete", f"You got {score} out of {len(flashcards)} correct!")

def add_flashcard():
    """Add a new flashcard to the list."""
    question = new_question_entry.get().strip()
    answer = new_answer_entry.get().strip()
    
    if question and answer:
        flashcards.append({"question": question, "answer": answer})
        messagebox.showinfo("Success", "Flashcard added successfully!")
        new_question_entry.delete(0, tk.END)
        new_answer_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter both a question and an answer.")

# GUI Setup
root = tk.Tk()
root.title("Flashcard App")
root.geometry("400x400")

# Quiz Section
question_label = tk.Label(root, text="Press 'Start Quiz' to begin", font=("Arial", 14), wraplength=350)
question_label.pack(pady=10)

answer_entry = tk.Entry(root, font=("Arial", 12))
answer_entry.pack(pady=5)

submit_button = tk.Button(root, text="Submit Answer", font=("Arial", 12), command=check_answer)
submit_button.pack(pady=5)

start_button = tk.Button(root, text="Start Quiz", font=("Arial", 12), command=start_quiz)
start_button.pack(pady=5)

# Add Flashcard Section
tk.Label(root, text="Add a New Flashcard", font=("Arial", 14)).pack(pady=10)

new_question_entry = tk.Entry(root, font=("Arial", 12), width=40)
new_question_entry.pack(pady=5)
new_question_entry.insert(0, "Enter question here...")

new_answer_entry = tk.Entry(root, font=("Arial", 12), width=40)
new_answer_entry.pack(pady=5)
new_answer_entry.insert(0, "Enter answer here...")

add_flashcard_button = tk.Button(root, text="Add Flashcard", font=("Arial", 12), command=add_flashcard)
add_flashcard_button.pack(pady=5)

# Start the Tkinter main loop
root.mainloop()

