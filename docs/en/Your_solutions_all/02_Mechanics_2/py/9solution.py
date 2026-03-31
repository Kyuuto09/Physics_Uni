import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def equations_of_motion(t, state, m, g, k):
    """Calculates the derivatives for position and velocity."""
    x, v = state
    dxdt = v
    dvdt = -g - (k / m) * v
    return [dxdt, dvdt]


# Physical Parameters
m = 1.0  # Mass (kg)
g = 9.81  # Gravity (m/s^2)
k = 0.5  # Drag coefficient (kg/s)
v0 = 20.0  # Initial velocity (m/s)
x0 = 10.0  # Initial height (m)

initial_state = [x0, v0]
t_span = (0, 5)  # Simulate from 0 to 5 seconds
t_eval = np.linspace(t_span[0], t_span[1], 500)

# 1. Simulate WITH drag
sol_drag = solve_ivp(
    equations_of_motion, t_span, initial_state, args=(m, g, k), t_eval=t_eval
)

# 2. Simulate WITHOUT drag (k=0)
sol_nodrag = solve_ivp(
    equations_of_motion, t_span, initial_state, args=(m, g, 0), t_eval=t_eval
)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(
    sol_drag.t, sol_drag.y[0], label=f"With Drag (k={k})", color="blue", linewidth=2
)
plt.plot(
    sol_nodrag.t,
    sol_nodrag.y[0],
    label="No Drag (k=0)",
    color="red",
    linestyle="--",
    linewidth=2,
)

plt.title("Numerical Simulation: Vertical Throw Position vs Time")
plt.xlabel("Time (seconds)")
plt.ylabel("Height (meters)")
plt.axhline(0, color="black", linewidth=1)  # Ground line
plt.ylim(bottom=0)
plt.legend()
plt.grid(True)
plt.show()
