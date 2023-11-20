import tkinter as tk
from tkinter import messagebox


def run_simulation():
    # You can add code here to get values from entry widgets and run the simulation
    messagebox.showinfo("Simulation", "Simulation started with the given parameters.")


app = tk.Tk()
app.title("Fluid Dynamics Simulation")

# Create and place widgets
start_button = tk.Button(app, text="Start Simulation", command=run_simulation)
start_button.pack()

# Add more widgets like entry fields, labels, etc.

app.mainloop()
