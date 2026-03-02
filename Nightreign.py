import tkinter as tk
from tkinter import ttk
import time

# ---------------- Chronometer Logic ----------------
class Chronometer:
    def __init__(self, label):
        self.label = label
        self.running = False
        self.start_time = 0
        self.elapsed = 0

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed
            self.running = True
            self.update()

    def stop(self):
        if self.running:
            self.elapsed = time.time() - self.start_time
            self.running = False

    def reset(self):
        self.running = False
        self.elapsed = 0
        self.label.config(text="00:00:00")

    def update(self):
        if self.running:
            self.elapsed = time.time() - self.start_time
            hours, rem = divmod(int(self.elapsed), 3600)
            minutes, seconds = divmod(rem, 60)
            self.label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
            self.label.after(1000, self.update)

# ---------------- Main UI ----------------
root = tk.Tk()
root.title("Chronometer + Levels")
root.geometry("900x500")

main_frame = ttk.Frame(root, padding=10)
main_frame.pack(fill="both", expand=True)

# Left panel (Chronometer)
left_frame = ttk.Frame(main_frame)
left_frame.pack(side="left", fill="y", padx=10)

chrono_label = ttk.Label(left_frame, text="00:00:00", font=("Consolas", 32))
chrono_label.pack(pady=20)

chrono = Chronometer(chrono_label)

btn_start = ttk.Button(left_frame, text="Start", command=chrono.start)
btn_stop = ttk.Button(left_frame, text="Stop", command=chrono.stop)
btn_reset = ttk.Button(left_frame, text="Reset", command=chrono.reset)

btn_start.pack(fill="x", pady=5)
btn_stop.pack(fill="x", pady=5)
btn_reset.pack(fill="x", pady=5)

# Right panel (Table)
right_frame = ttk.Frame(main_frame)
right_frame.pack(side="right", fill="both", expand=True)

columns = ("Level", "Upgrade Cost", "Total Cost", "Optimal Equipment")
table = ttk.Treeview(right_frame, columns=columns, show="headings")

for col in columns:
    table.heading(col, text=col)
    table.column(col, anchor="center")

rows = [
    (1, "-", "-", "Common"),
    (2, "3,698", "3,698", "Common"),
    (3, "7,922", "11,620", "Rare"),
    (4, "12,348", "23,968", "Rare"),
    (5, "16,798", "40,946", "Rare"),
    (6, "21,818", "62,764", "Rare"),
    (7, "26,869", "89,633", "Epic"),
    (8, "32,137", "121,770", "Epic"),
    (9, "37,624", "159,394", "Epic"),
    (10, "43,335", "202,729", "Legendary"),
    (11, "49,271", "252,000", "Legendary"),
    (12, "55,439", "307,439", "Legendary"),
    (13, "61,840", "369,279", "Legendary"),
    (14, "68,479", "437,758", "Legendary"),
    (15, "75,358", "513,116", "Legendary"),
]

for row in rows:
    table.insert("", "end", values=row)

table.pack(fill="both", expand=True)

root.mainloop()
