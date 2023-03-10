import numpy as np

def calculate_trajectory(initial_position, initial_velocity, mass, time_step, duration):
    # Define constants
    G = 6.67430e-11  # Gravitational constant
    M = 5.97e24  # Mass of Earth
    R = 6.3781e6  # Radius of Earth
    Cd = 2.2  # Drag coefficient
    A = 10  # Cross-sectional area
    rho0 = 1.225  # Density at sea level
    H = 8000  # Scale height
    k = 1/(rho0*H)  # Exponential factor
    
    # Initialize arrays
    position = np.zeros((int(duration/time_step)+1,3))
    velocity = np.zeros((int(duration/time_step)+1,3))
    acceleration = np.zeros(3)
    density = np.zeros(int(duration/time_step)+1)
    
    # Set initial conditions
    position[0] = initial_position
    velocity[0] = initial_velocity
    
    # Numerical integration using Euler's method
    for i in range(1, int(duration/time_step)+1):
        # Calculate density at current altitude
        r = np.linalg.norm(position[i-1])
        if r <= R:
            density[i] = 0
        else:
            h = r - R
            density[i] = rho0*np.exp(-k*h)
        
        # Calculate acceleration
        v = np.linalg.norm(velocity[i-1])
        A_effective = A*np.cos(np.arcsin(np.dot(velocity[i-1], position[i-1])/r))
        F_drag = -0.5*Cd*density[i]*A_effective*v**2
        acceleration_gravity = -G*M*position[i-1]/r**3
        acceleration_drag = F_drag/mass
        acceleration = acceleration_gravity + acceleration_drag
        
        # Update velocity and position
        velocity[i] = velocity[i-1] + acceleration*time_step
        position[i] = position[i-1] + velocity[i]*time_step
    
    return position, velocity, density
