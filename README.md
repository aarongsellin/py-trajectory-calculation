# Python Trajectory Calculation

This is a Python script that calculates the trajectory of an object in space using numerical integration. The script takes into account the gravitational forces between the object and the Earth, as well as the effects of atmospheric drag on the object's trajectory. The script uses the Euler's method for numerical integration and returns the position and velocity of the object at each time step, as well as the atmospheric density at different altitudes.

## Usage
To use the script, you will need to have Python 3 installed on your computer. You can then run the script from the command line using the following command:


The script includes several parameters that you can modify to simulate different scenarios. These parameters include:

- `initial_position`: The initial position of the object in space, specified as a 3-element numpy array.
- `initial_velocity`: The initial velocity of the object in space, specified as a 3-element numpy array.
- `mass`: The mass of the object, in kilograms.
- `time_step`: The time step for numerical integration, in seconds.
- `duration`: The duration of the simulation, in seconds.

You can modify these parameters to simulate different initial conditions and scenarios.

## Mathematical Formulation

The script calculates the trajectory of the object using the following equations:

### Gravitational Force

The gravitational force between the object and the Earth is given by the equation:

$$F_{gravity} = -\frac{GMm}{r^3} \vec{r}$$

where $G$ is the gravitational constant, $M$ is the mass of the Earth, $m$ is the mass of the object, $r$ is the distance between the object and the Earth, and $\vec{r}$ is the unit vector in the direction of the object.

### Drag Force

The drag force on the object due to atmospheric drag is given by the equation:

$$F_{drag} = -\frac{1}{2} \rho v^2 C_d A_{effective} \vec{v}$$

where $\rho$ is the atmospheric density, $v$ is the velocity of the object, $C_d$ is the drag coefficient, $A_{effective}$ is the effective cross-sectional area of the object, and $\vec{v}$ is the velocity vector of the object.

The effective cross-sectional area of the object is given by:

$$A_{effective} = A \cos\theta$$

where $A$ is the actual cross-sectional area of the object and $\theta$ is the angle between the velocity vector of the object and the vector normal to the object's surface.

## Example

Here is an example of how to use the script:

```python
import numpy as np
from trajectory_calculation import calculate_trajectory

# Set initial conditions
initial_position = np.array([0, 5000000, 0])
initial_velocity = np.array([5000, 0, 0])
mass = 1000
time_step = 10
duration = 86400

# Calculate trajectory
position, velocity, density = calculate_trajectory(initial_position, initial_velocity, mass, time_step, duration)

# Print results
print("Position at t=0:", position[0])
print("Velocity at t=0:", velocity[0])
print("Position at t=86400:", position[-1])
print("Velocity at t=86400:", velocity[-1])
