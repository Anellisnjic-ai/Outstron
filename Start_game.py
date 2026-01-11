import tkinter as tk
from tkinter import ttk
import time
import threading

# Function to simulate loading
def start_loading():
    for percent in range(101):
        if percent == 99:
            label_text.set("Outstron")
        progress_bar['value'] = percent
        percent_label.config(text=f"{percent}%")
        time.sleep(0.05)  # speed of loading
    label_text.set("Done! Game Started!")

# Function to start game in a separate thread
def start_game():
    start_button.config(state="disabled")
    threading.Thread(target=start_loading).start()

# Create main window
root = tk.Tk()
root.title("Start Game")
root.geometry("400x200")
root.resizable(False, False)

# Label
label_text = tk.StringVar()
label_text.set("Loading")
label = tk.Label(root, textvariable=label_text, font=("Arial", 24))
label.pack(pady=20)

# Progress bar
progress_bar = ttk.Progressbar(root, length=300)
progress_bar.pack(pady=10)

# Percent label
percent_label = tk.Label(root, text="0%", font=("Arial", 16))
percent_label.pack()

# Start button
start_button = tk.Button(root, text="Start Game", font=("Arial", 16), command=start_game)
start_button.pack(pady=10)

# Run the window
root.mainloop()
