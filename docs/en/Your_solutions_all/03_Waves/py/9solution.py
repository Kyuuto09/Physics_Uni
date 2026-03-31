import numpy as np
import matplotlib.pyplot as plt


def derivatives(state, t, m, b, k):
    """Calculates [dx/dt, dv/dt] for the RK4 solver."""
    x, v = state
    dxdt = v
    dvdt = -(b / m) * v - (k / m) * x
    return np.array([dxdt, dvdt])


def rk4_step(state, t, dt, m, b, k):
    """Executes one standard Runge-Kutta 4th Order time step."""
    k1 = derivatives(state, t, m, b, k)
    k2 = derivatives(state + 0.5 * dt * k1, t + 0.5 * dt, m, b, k)
    k3 = derivatives(state + 0.5 * dt * k2, t + 0.5 * dt, m, b, k)
    k4 = derivatives(state + dt * k3, t + dt, m, b, k)

    return state + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)


# System Parameters
m = 1.0  # Mass (kg)
k = 10.0  # Spring constant (N/m)
dt = 0.05  # Time step (seconds)
time_steps = int(10 / dt)  # Simulate for 10 seconds

# Initial Conditions [Position, Velocity]
initial_state = np.array([1.0, 0.0])  # Pulled out 1 meter, let go from rest

# Calculate exact 'b' values for the 3 cases
b_critical = 2 * np.sqrt(m * k)
cases = {
    "Underdamped (b=1.0)": 1.0,
    "Critically Damped (b=6.32)": b_critical,
    "Overdamped (b=12.0)": 12.0,
}

# Setup Plots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

for label, b in cases.items():
    t_vals = np.linspace(0, 10, time_steps)
    states = np.zeros((time_steps, 2))
    states[0] = initial_state

    # Run the RK4 Simulation Loop
    for i in range(1, time_steps):
        states[i] = rk4_step(states[i - 1], t_vals[i - 1], dt, m, b, k)

    x_vals = states[:, 0]
    v_vals = states[:, 1]

    # Plot x(t) - Time Domain
    ax1.plot(t_vals, x_vals, label=label, linewidth=2)

    # Plot v vs x - Phase Portrait
    ax2.plot(x_vals, v_vals, label=label, linewidth=2)

# Formatting Graph 1: Position vs Time
ax1.set_title("Time Domain: Position x(t)")
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Position (m)")
ax1.axhline(0, color="black", linewidth=1)
ax1.grid(True, linestyle="--", alpha=0.7)
ax1.legend()

# Formatting Graph 2: Phase Portrait (Velocity vs Position)
ax2.set_title("Phase Portrait: Velocity vs Position")
ax2.set_xlabel("Position (m)")
ax2.set_ylabel("Velocity (m/s)")
ax2.axhline(0, color="black", linewidth=1)
ax2.axvline(0, color="black", linewidth=1)
ax2.grid(True, linestyle="--", alpha=0.7)
ax2.legend()

plt.tight_layout()
plt.show()
