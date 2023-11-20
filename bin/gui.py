import tkinter as tk
from tkinter import messagebox
import cfd


#### SIMULATION RUN BUTTON COMMAND ----------------------------------------------------------------
def run_simulation():
    # Retrieve values from the entry widgets
    sim_params = {
        "time": int(time_entry.get()),
        "CFL_number": float(cfl_entry.get()),
        "file_flag": int(file_flag_entry.get()),
        "interval": int(interval_entry.get()),
        "length": float(length_entry.get()),
        "breadth": float(breadth_entry.get()),
        "colpts": int(colpts_entry.get()),
        "rowpts": int(rowpts_entry.get()),
        "rho": float(rho_entry.get()),
        "mu": float(mu_entry.get()),
    }

    # You can now pass sim_params and boundary_params to your simulation function
    # For now, just showing a message box
    messagebox.showinfo("Simulation", "Simulation started with the given parameters.")
    cfd.run(sim_params)


#### Create GUI ----------------------------
app = tk.Tk()
app.title("Fluid Dynamics Simulation")

#### Widgets--------------------------------
# Simulation time
tk.Label(app, text="Time").pack()
time_entry = tk.Entry(app)
time_entry.insert(0, 150)
time_entry.pack()

# Reduce this if solution diverges
tk.Label(app, text="CFL Number").pack()
cfl_entry = tk.Entry(app)
cfl_entry.insert(0, 0.8)
cfl_entry.pack()

# Keep 1 to print results to file
tk.Label(app, text="File flag").pack()
file_flag_entry = tk.Entry(app)
file_flag_entry.insert(0, 1)
file_flag_entry.pack()

# Record values in file per interval number of iterations
tk.Label(app, text="Interval").pack()
interval_entry = tk.Entry(app)
interval_entry.insert(0, 100)
interval_entry.pack()

# Length of computational domain in the x-direction
tk.Label(app, text="Length").pack()
length_entry = tk.Entry(app)
length_entry.insert(0, 4)
length_entry.pack()

# Breadth of computational domain in the y-direction
tk.Label(app, text="Breadth").pack()
breadth_entry = tk.Entry(app)
breadth_entry.insert(0, 4)
breadth_entry.pack()

# Number of grid points in the x-direction #KEEP ODD
tk.Label(app, text="Points along y").pack()
colpts_entry = tk.Entry(app)
colpts_entry.insert(0, 257)
colpts_entry.pack()

# Number of grid points in the y-direction #KEEP ODD
tk.Label(app, text="Points along x").pack()
rowpts_entry = tk.Entry(app)
rowpts_entry.insert(0, 257)
rowpts_entry.pack()

# Density of fluid
tk.Label(app, text="Fluid density").pack()
rho_entry = tk.Entry(app)
rho_entry.insert(0, 1)
rho_entry.pack()

# Dynamic viscosity of fluid
tk.Label(app, text="Fluid dynamic viscosity").pack()
mu_entry = tk.Entry(app)
mu_entry.insert(0, 0.01)
mu_entry.pack()

#### Start Simulation button
start_button = tk.Button(app, text="Start Simulation", command=run_simulation)
start_button.pack()

app.mainloop()
