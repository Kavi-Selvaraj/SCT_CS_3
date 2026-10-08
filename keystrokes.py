import tkinter as tk
from datetime import datetime

LOG_FILE = "keystrokes.txt"


def log_key(event):
    key = event.keysym

    # Convert special keys to readable names
    if key == "space":
        key = "[SPACE]"
    elif key == "Return":
        key = "[ENTER]"
    elif key == "BackSpace":
        key = "[BACKSPACE]"
    elif len(key) == 1:
        key = key

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"{timestamp} - {key}\n")

    status_label.config(text=f"Last key: {key}")


# Create application
root = tk.Tk()
root.title("Keylogging Demonstration")
root.geometry("500x300")

label = tk.Label(
    root,
    text="Type inside the box below:",
    font=("Arial", 14)
)
label.pack(pady=20)

text_box = tk.Text(root, width=50, height=8)
text_box.pack()

status_label = tk.Label(root, text="Last key: None")
status_label.pack(pady=15)

# Listen only to keys entered in this application
text_box.bind("<KeyPress>", log_key)

root.mainloop()