import tkinter as tk

window = tk.Tk()

def rock():
    pass

def paper():
    pass

def scissors():
    pass

rock_button = tk.Button(window, text="Rock", command=rock)
rock_button.pack()

paper_button = tk.Button(window, text="Paper", command=paper)
paper_button.pack()

scissors_button = tk.Button(window, text="Scissors", command=scissors)
scissors_button.pack()

window.mainloop()
