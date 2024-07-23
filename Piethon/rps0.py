import tkinter as tk
import random

def play(player_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    
    result = ""
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
    else:
        result = "Computer wins!"
    
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors")

# Create buttons
rock_button = tk.Button(root, text="Rock", command=lambda: play("Rock"))
paper_button = tk.Button(root, text="Paper", command=lambda: play("Paper"))
scissors_button = tk.Button(root, text="Scissors", command=lambda: play("Scissors"))

# Create result label
result_label = tk.Label(root, text="", font=("Helvetica", 14))

# Layout buttons and label
rock_button.pack(pady=10)
paper_button.pack(pady=10)
scissors_button.pack(pady=10)
result_label.pack(pady=20)

# Start the main loop
root.mainloop()
