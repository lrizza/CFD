import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import utils

#### SPATIAL AND TEMPORAL INPUTS
length = 8  # Length of computational domain in the x-direction
breadth = 4  # Breadth of computational domain in the y-direction
colpts = 257  # Number of grid points in the x-direction #KEEP ODD
rowpts = 257  # Number of grid points in the y-direction #KEEP ODD
# Create an object of the class Space called cavity
cavity = utils.Space()
cavity.CreateMesh(rowpts, colpts)
cavity.SetDeltas(breadth, length)

#### FLUID PROPERTIES
rho = 1  # Density of fluid
mu = 0.01  # Viscosity of fluid
# Create an object of the class Fluid called water
water = utils.Fluid(rho, mu)

#### BOUNDARY SPECIFICATIONS
u_in = 1  # Lid velocity
v_wall = 0  # Velocity of fluid at the walls
p_out = 0  # Gauge pressure at the boundaries
# Create objects of the class Boundary having either Dirichlet ("D") or Neumann ("N") type boundaries
flow = utils.Boundary("D", u_in)
noslip = utils.Boundary("D", v_wall)
zeroflux = utils.Boundary("N", 0)
pressureatm = utils.Boundary("D", p_out)

#### SIMULATION PARAMETERS
time = 150  # Simulation time
CFL_number = 0.8  # Reduce this if solution diverges
file_flag = 1  # Keep 1 to print results to file
interval = 100  # Record values in file per interval number of iterations

#### RUN SIMULATION
# Print general simulation information
print("######## Beginning FlowPy Simulation ########")
print("#############################################")
print("# Simulation time: {0:.2f}".format(time))
print("# Mesh: {0} x {1}".format(colpts, rowpts))
print("# Re/u: {0:.2f}\tRe/v:{1:.2f}".format(rho * length / mu, rho * breadth / mu))
print("# Save outputs to text file: {0}".format(bool(file_flag)))
## Initialization
# Make directory to store results
utils.MakeResultDirectory(wipe=True)
# Initialize counters
t = 0
i = 0
## Run
while t < time:
    # Print time left
    sys.stdout.write("\rSimulation time left: {0:.2f}".format(time - t))
    sys.stdout.flush()
    # Set the time-step
    utils.SetTimeStep(CFL_number, cavity, water)
    timestep = cavity.dt

    # Set boundary conditions
    utils.SetUBoundary(cavity, noslip, noslip, flow, noslip)
    utils.SetVBoundary(cavity, noslip, noslip, noslip, noslip)
    utils.SetPBoundary(cavity, zeroflux, zeroflux, pressureatm, zeroflux)

    # Calculate starred velocities
    utils.GetStarredVelocities(cavity, water)

    # Solve the pressure Poisson equation
    utils.SolvePressurePoisson(cavity, water, zeroflux, zeroflux, pressureatm, zeroflux)
    # Solve the momentum equation
    utils.SolveMomentumEquation(cavity, water)
    # Save variables and write to file
    utils.SetCentrePUV(cavity)
    if file_flag == 1:
        utils.WriteToFile(cavity, i, interval)
    # Advance time-step and counter
    t += timestep
    i += 1
