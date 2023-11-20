import utils

#### BOUNDARY SPECIFICATIONS
u_in = 1  # Lid velocity
v_wall = 0  # Velocity of fluid at the walls
p_out = 0  # Gauge pressure at the boundaries

#### SIMULATION PARAMETERS
sim_params = {
    "time": 150,  # Simulation time
    "CFL_number": 0.8,  # Reduce this if solution diverges
    "file_flag": 1,  # Keep 1 to print results to file
    "interval": 100,  # Record values in file per interval number of iterations
    "length": 4,  # Length of computational domain in the x-direction
    "breadth": 4,  # Breadth of computational domain in the y-direction
    "colpts": 257,  # Number of grid points in the x-direction #KEEP ODD
    "rowpts": 257,  # Number of grid points in the y-direction #KEEP ODD
    "rho": 1,  # Density of fluid
    "mu": 0.01,  # Viscosity of fluid
}

# Create objects of the class Boundary having either Dirichlet ("D") or Neumann ("N") type boundaries
boundary_params = {
    "flow": utils.Boundary("D", u_in),
    "noslip": utils.Boundary("D", v_wall),
    "zeroflux": utils.Boundary("N", 0),
    "pressureatm": utils.Boundary("D", p_out),
}
