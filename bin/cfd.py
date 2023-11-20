import sys
import utils


def run(sim_params):
    #### BOUNDARY SPECIFICATIONS
    u_in = 1  # Lid velocity
    v_wall = 0  # Velocity of fluid at the walls
    p_out = 0  # Gauge pressure at the boundaries

    # Create objects of the class Boundary having either Dirichlet ("D") or Neumann ("N") type boundaries
    boundary_params = {
        "flow": utils.Boundary("D", u_in),
        "noslip": utils.Boundary("D", v_wall),
        "zeroflux": utils.Boundary("N", 0),
        "pressureatm": utils.Boundary("D", p_out),
    }

    ####  Unpack simulation parameter dictionary
    time = sim_params["time"]
    CFL_number = sim_params["CFL_number"]
    file_flag = sim_params["file_flag"]
    interval = sim_params["interval"]
    length = sim_params["length"]
    breadth = sim_params["breadth"]
    colpts = sim_params["colpts"]
    rowpts = sim_params["rowpts"]
    rho = sim_params["rho"]
    mu = sim_params["mu"]

    #### Unpack boundary condition dictionary
    noslip = boundary_params["noslip"]
    flow = boundary_params["flow"]
    zeroflux = boundary_params["zeroflux"]
    pressureatm = boundary_params["pressureatm"]

    # Create an object of the class Fluid called water
    water = utils.Fluid(rho, mu)

    # Create an object of the class Space called cavity
    cavity = utils.Space()
    cavity.CreateMesh(rowpts, colpts)
    cavity.SetDeltas(breadth, length)

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
        utils.SolvePressurePoisson(
            cavity, water, zeroflux, zeroflux, pressureatm, zeroflux
        )
        # Solve the momentum equation
        utils.SolveMomentumEquation(cavity, water)
        # Save variables and write to file
        utils.SetCentrePUV(cavity)
        if file_flag == 1:
            utils.WriteToFile(cavity, i, interval)
        # Advance time-step and counter
        t += timestep
        i += 1
