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
        root.update()  # update GUI
        time.sleep(0.03)  # smooth speed
    label_text.set("Done! Game Started!")

# Automatically start loading
def auto_start():
    start_button.pack_forget()  # hide start button
    threading.Thread(target=start_loading).start()

# Create main window
root = tk.Tk()
root.title("Start Game")

# Force fullscreen and remove window decorations
root.attributes('-fullscreen', True)  # fullscreen
root.attributes('-topmost', True)  # always on top
root.overrideredirect(True)  # remove title bar
root.configure(bg='#0a0a0a')  # dark background like Minecraft

# Minecraft-style label
label_text = tk.StringVar()
label_text.set("Loading")
label = tk.Label(root, textvariable=label_text, font=("Arial", 48, "bold"), fg="#ffffff", bg="#0a0a0a")
label.pack(expand=True, pady=50)

# Progress bar style
style = ttk.Style()
style.theme_use('clam')
style.configure("green.Horizontal.TProgressbar", foreground='green', background='green', thickness=40)

progress_bar = ttk.Progressbar(root, length=root.winfo_screenwidth() - 200, style="green.Horizontal.TProgressbar")
progress_bar.pack(pady=20)

# Percent label
percent_label = tk.Label(root, text="0%", font=("Arial", 32, "bold"), fg="#ffffff", bg="#0a0a0a")
percent_label.pack(pady=20)

# Optional Start button
start_button = tk.Button(root, text="Start Game", font=("Arial", 24, "bold"), fg="#ffffff", bg="#333333", command=auto_start)
start_button.pack(pady=50)

# Automatically start after 1 second for single-click effect
root.after(1000, auto_start)

# Close window on Escape key (useful for testing)
root.bind("<Escape>", lambda e: root.destroy())

root.mainloop()

import pygame
import sys

pygame.init()

# Start in windowed mode
screen = pygame.display.set_mode((800, 600))
pygamedisplay.set_caption("Outstron")

fullscreen = False

while True:
    for event in pygameevent.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:  # Press F to toggle full screen
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((800, 600))

    screen.fill((50, 50, 50))  # background color
    pygame.display.flip()
