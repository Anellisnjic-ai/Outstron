import tkinter as tk
from tkinter import ttk
import threading
import time

# Function to simulate loading
def start_loading():
    for percent in range(101):
        if percent == 99:
            label_text.set("Outstron")
        progress_bar['value'] = percent
        percent_label.config(text=f"{percent}%")
        root.update()  # update the GUI
        time.sleep(0.03)  # faster loading for smoothness
    label_text.set("Done! Game Started!")

# Automatically start loading
def auto_start():
    start_button.pack_forget()  # hide start button
    threading.Thread(target=start_loading).start()

# Create full screen window
root = tk.Tk()
root.title("Start Game")
root.attributes('-fullscreen', True)  # FULLSCREEN
root.configure(bg='#0a0a0a')  # dark background like Minecraft

# Minecraft-style label
label_text = tk.StringVar()
label_text.set("Loading")
label = tk.Label(root, textvariable=label_text, font=("Minecraft", 48, "bold"), fg="#ffffff", bg="#0a0a0a")
label.pack(pady=100)

# Progress bar style
style = ttk.Style()
style.theme_use('clam')
style.configure("red.Horizontal.TProgressbar", foreground='green', background='green', thickness=30)

progress_bar = ttk.Progressbar(root, length=800, style="red.Horizontal.TProgressbar")
progress_bar.pack(pady=20)

# Percent label
percent_label = tk.Label(root, text="0%", font=("Minecraft", 32, "bold"), fg="#ffffff", bg="#0a0a0a")
percent_label.pack(pady=20)

# Start button (optional)
start_button = tk.Button(root, text="Start Game", font=("Minecraft", 24, "bold"), fg="#ffffff", bg="#333333", command=auto_start)
start_button.pack(pady=50)

# Automatically start after 1 second for single-click effect
root.after(1000, auto_start)

root.mainloop()
