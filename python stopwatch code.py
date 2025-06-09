#TEAM MEMBER 1 Name: Keshika Pillai 23104A0038

#Team member 2 Name:Pravin Bhangare 23104A0051
import tkinter as tk 
import time

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        self.running = False
        self.counter = 0

        # Timer label
        self.time_label = tk.Label(root, text="00:00:00", font=("Helvetica", 40))
        self.time_label.pack(pady=20)

        # Buttons
        self.start_button = tk.Button(root, text="Start", font=("Helvetica", 15), command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=20)

        self.stop_button = tk.Button(root, text="Stop", font=("Helvetica", 15), command=self.stop)
        self.stop_button.pack(side=tk.LEFT, padx=20)

        self.reset_button = tk.Button(root, text="Reset", font=("Helvetica", 15), command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=20)

    def update_timer(self):
        if self.running:
            self.counter += 1
            formatted_time = self.format_time(self.counter)
            self.time_label.config(text=formatted_time)
            self.root.after(1000, self.update_timer)

    def format_time(self, seconds):
        hrs = seconds // 3600
        mins = (seconds % 3600) // 60
        secs = seconds % 60
        return f"{hrs:02}:{mins:02}:{secs:02}"

    def start(self):
        if not self.running:
            self.running = True
            self.update_timer()

    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.counter = 0
        self.time_label.config(text="00:00:00")


if __name__ == "__main__":
    root = tk.Tk()
    app = Stopwatch(root)
    root.mainloop()

