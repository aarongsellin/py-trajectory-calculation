# Projectile Trajectory Calculation

This project is a Python program that calculates the trajectory of a projectile based on its initial velocity and launch angle.

## Calculation

The program uses the following equations to calculate the trajectory:

- `x = v * cos(theta) * t` : horizontal distance traveled
- `y = v * sin(theta) * t - 0.5 * g * t^2` : vertical distance traveled
- `t = 2 * v * sin(theta) / g` : time of flight
- `ymax = (v * sin(theta))^2 / (2 * g)` : maximum height
- `xmax = v^2 * sin(2 * theta) / g` : maximum distance

where:
- `x` is the horizontal distance traveled by the projectile
- `y` is the vertical distance traveled by the projectile
- `v` is the initial velocity of the projectile
- `theta` is the launch angle of the projectile
- `t` is the time of flight of the projectile
- `g` is the acceleration due to gravity (9.81 m/s^2)
- `ymax` is the maximum height reached by the projectile
- `xmax` is the maximum distance reached by the projectile

## Usage

To use the program, simply run the `trajectory_calculation.py` file in a Python environment:

```python
python trajectory_calculation.py