import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from playsound import playsound
import time

class Pomodoro:

    def __init__(self): 
        self.gui = tk.Tk()

        icon = tk.PhotoImage(file="./favicon1.png") 
        self.gui.iconphoto(True, icon)

        self.time = 0
        self.type = ""
        self.minutes = tk.StringVar(self.gui)
        self.seconds = tk.StringVar(self.gui)
        self.timers = {
            "pomodoro": {"duration": "25", "message": "Good job!"},
            "short_break": {"duration": "05", "message": "Time for a break."},
            "long_break": {"duration": "10", "message": "Get a good rest. Drink water."}
        }
        self.bg_image = None


    def select(self, type):
        self.type = type
        self.minutes.set(self.timers[type]["duration"])
        self.seconds.set("00")
        self.time = -1 

    def timer(self, timer):
        minutes, seconds = divmod(timer, 60)
        self.minutes.set(f"{minutes:02d}")
        self.seconds.set(f"{seconds:02d}")
        self.gui.update()
        time.sleep(1) 

    def start(self):
        self.time = int(self.minutes.get()) * 60 + int(self.seconds.get())

        while self.time >= 0: 
            self.timer(self.time) 
            
            if self.time == 0:
                playsound("./alarm_pixabay.mp3")
                messagebox.showinfo("Time's up!", self.timers[self.type]["message"])

            self.time -= 1

    def stop(self):
        self.time = -1

    def reset(self):
        self.stop()
        self.select(self.type) 

    def create_widgets(self):

        for i in range(5):
            self.gui.grid_columnconfigure(i, weight=1)

        tk.Label(self.gui, textvariable=self.minutes,
            font=("arial", 22, "bold"), bg="red", fg="black",
            width=5, justify="center").grid(row=0, column=2, padx=5, pady=10)

        tk.Label(self.gui, textvariable=self.seconds,
            font=("arial", 22, "bold"), bg="black", fg="white",
            width=5, justify="center").grid(row=0, column=3, padx=5, pady=10)
        
        tk.Button(self.gui, text="pomodoro", command=lambda: self.select("pomodoro"),
                  bd=5).grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        tk.Button(self.gui, text="short break", command=lambda: self.select("short_break"),
                  bd=5).grid(row=1, column=2, columnspan=2, padx=10, pady=5)

        tk.Button(self.gui, text="long break", command=lambda: self.select("long_break"),
                  bd=5).grid(row=1, column=4, columnspan=4, padx=10, pady=5)

        canvas = tk.Canvas(self.gui, width=250, height=250)
        canvas.grid(row=2, column=0, columnspan=5, pady=(5, 10))

        img = Image.open("./cute_tomato.png").resize((250, 250))
        self.bg_image = ImageTk.PhotoImage(img)
        canvas.create_image(125, 125, image=self.bg_image)  
        
        tk.Button(self.gui, text="start", command=lambda: self.start(),
                    bd=5, bg="white", fg="green", font=("arial", 13, "bold")
                    ).grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        tk.Button(self.gui, text="stop", command=lambda: self.stop(),
                    bd=5, bg="white", fg="green", font=("arial", 13, "bold")
                    ).grid(row=3, column=2, columnspan=2, padx=10, pady=10)
    
        tk.Button(self.gui, text="reset", command=lambda: self.reset(),
                    bd=5, bg="white", fg="green", font=("arial", 13, "bold")
                    ).grid(row=3, column=4, columnspan=4, padx=10, pady=10)

    def run(self):
        self.gui.geometry("390x440")
        self.gui.resizable(False, False)
        self.gui.title("Pomodoro Timer")   
        self.create_widgets()
        self.gui.mainloop()

if __name__ == "__main__":
    pomodoro = Pomodoro()
    pomodoro.run()