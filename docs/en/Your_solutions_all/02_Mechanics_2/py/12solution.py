import numpy as np
import matplotlib.pyplot as plt

# We use NumPy's vectorized operations (np.linspace) instead of for-loops.
# This is an AI Engineering best practice for processing large datasets efficiently.
t = np.linspace(0, 3, 100)  # Evaluate 100 points between t=0 and t=3

# Vectorized position equations based on our derived r(t)
x = 1.5 * t**2 + t
y = 0.5 * t**2 - t

# Plotting the trajectory
plt.figure(figsize=(8, 6))
plt.plot(x, y, label="Trajectory (t=0 to t=3)", color="purple", linewidth=2)
plt.scatter([x[0]], [y[0]], color="green", zorder=5, label="Start (t=0)")
plt.scatter([x[-1]], [y[-1]], color="red", zorder=5, label="End (t=3)")

plt.title("Particle Trajectory under Constant Force")
plt.xlabel("x position (meters)")
plt.ylabel("y position (meters)")
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend()
plt.show()
