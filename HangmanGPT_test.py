import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.word_list = [
            "apple", "banana", "carrot", "donut", "eggplant",
            "fajitas", "grapefruit", "honeydew", "icecream", "jalapeno",
            "kiwifruit", "lemonade", "mango", "nectarine", "orange",
            "papaya", "quinoa", "raspberry", "spaghetti", "tomato",
            "ugli", "vanilla", "watermelon", "xigua", "yogurt", "zucchini"
        ]
        self.setup_ui()
        self.new_game()
    
    def setup_ui(self):
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg='white')
        self.canvas.grid(row=0, column=0, rowspan=6, columnspan=2)

        self.label = tk.Label(self.root, text="Guess the word:")
        self.label.grid(row=0, column=2)
        
        self.word_display = tk.StringVar()
        self.word_label = tk.Label(self.root, textvariable=self.word_display, font=("Helvetica", 18))
        self.word_label.grid(row=1, column=2, columnspan=2)
        
        self.guess_label = tk.Label(self.root, text="Enter a letter:")
        self.guess_label.grid(row=2, column=2)
        
        self.guess_entry = tk.Entry(self.root)
        self.guess_entry.grid(row=2, column=3)
        self.guess_entry.bind("<Return>", self.process_guess_event)  # Bind Enter key
        
        self.guess_button = tk.Button(self.root, text="Guess", command=self.process_guess)
        self.guess_button.grid(row=3, column=2, columnspan=2)
        
        self.new_game_button = tk.Button(self.root, text="New Game", command=self.new_game)
        self.new_game_button.grid(row=4, column=2, columnspan=2)
        
    def new_game(self):
        self.current_word = random.choice(self.word_list)
        self.guessed_letters = []
        self.remaining_attempts = 6
        self.update_display()
        self.canvas.delete("all")

    def process_guess_event(self, event):
        self.process_guess()
    
    def process_guess(self):
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)
        if guess in self.guessed_letters or len(guess) != 1 or not guess.isalpha():
            return
        self.guessed_letters.append(guess)
        if guess not in self.current_word:
            self.remaining_attempts -= 1
        self.update_display()
        self.draw_hangman()
        if "_" not in self.word_display.get():
            messagebox.showinfo("Hangman", "Congratulations, you won!")
            self.new_game()
        elif self.remaining_attempts == 0:
            messagebox.showinfo("Hangman", f"Game Over! The word was {self.current_word}")
            self.new_game()
    
    def update_display(self):
        display_word = " ".join([letter if letter in self.guessed_letters else "_" for letter in self.current_word])
        self.word_display.set(display_word)
    
    def draw_hangman(self):
        parts = [
            (50, 350, 150, 350),  # base
            (100, 350, 100, 50),  # pole
            (100, 50, 250, 50),   # top bar
            (250, 50, 250, 100),  # rope
            (225, 100, 275, 150), # head
            (250, 150, 250, 250), # body
            (250, 170, 200, 220), # left arm
            (250, 170, 300, 220), # right arm
            (250, 250, 200, 300), # left leg
            (250, 250, 300, 300)  # right leg
        ]
        for i in range(6 - self.remaining_attempts):
            self.canvas.create_line(parts[i])

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
