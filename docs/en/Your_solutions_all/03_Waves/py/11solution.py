import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. Setup the 2D Spatial Grid
grid_size = 10.0
resolution = 200
x = np.linspace(0, grid_size, resolution)  # Slits are at x=0, screen is at x=10
y = np.linspace(-grid_size / 2, grid_size / 2, resolution)
X, Y = np.meshgrid(x, y)

# 2. Physics Parameters (Initial State)
A = 1.0  # Amplitude
wavelength = 1.0  # Wavelength (lambda)
omega = 5.0  # Angular frequency
d = 2.0  # Distance between slits


def calculate_interference(X, Y, t, wavelength, d, A, omega):
    """Calculates the two-slit superposition map."""
    k = (2 * np.pi) / wavelength

    # Slit Coordinates (placed on the left wall at x=0)
    r1 = np.array([0.0, d / 2])
    r2 = np.array([0.0, -d / 2])

    # Distance from each slit to every pixel on the grid
    R1 = np.sqrt((X - r1[0]) ** 2 + (Y - r1[1]) ** 2)
    R2 = np.sqrt((X - r2[0]) ** 2 + (Y - r2[1]) ** 2)

    # Prevent division by zero at the exact slit coordinates
    R1 = np.where(R1 < 0.1, 0.1, R1)
    R2 = np.where(R2 < 0.1, 0.1, R2)

    # Superposition Equation
    wave1 = (A / R1) * np.sin(k * R1 - omega * t)
    wave2 = (A / R2) * np.sin(k * R2 - omega * t)

    return wave1 + wave2


# 3. Setup the Animation Plot
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_title(f"Two-Slit Interference (d={d}, $\lambda$={wavelength})")
ax.set_xlabel("Distance from Slits (X)")
ax.set_ylabel("Position along Screen (Y)")

# Initial render
Z_initial = calculate_interference(X, Y, 0, wavelength, d, A, omega)
img = ax.imshow(
    Z_initial,
    extent=[0, grid_size, -grid_size / 2, grid_size / 2],
    origin="lower",
    cmap="inferno",
    vmin=-1.5,
    vmax=1.5,
)
fig.colorbar(img, ax=ax, label="Wave Amplitude")


def update(frame):
    """Animation loop."""
    t = frame * 0.1
    Z_new = calculate_interference(X, Y, t, wavelength, d, A, omega)
    img.set_data(Z_new)
    return [img]


ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.show()
