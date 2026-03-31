import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. Setup the 2D Spatial Grid (Resolution: 200x200 pixels)
grid_size = 10.0
resolution = 200
x = np.linspace(-grid_size, grid_size, resolution)
y = np.linspace(-grid_size, grid_size, resolution)
X, Y = np.meshgrid(x, y)

# 2. Physics Parameters
A = 1.0  # Initial Amplitude
k = 2.0  # Wave number (controls wavelength)
omega = 5.0  # Angular frequency (controls speed)
alpha = 0.5  # Decay parameter (0 = no decay, 2 = fast decay)

# Define the coordinates of our wave emitters (r0)
sources = [np.array([-3.0, 0.0]), np.array([3.0, 0.0])]  # Emitter 1  # Emitter 2


def calculate_superposition(X, Y, t, sources, A, k, omega, alpha):
    """Calculates the combined wave height for every pixel on the grid."""
    Z_total = np.zeros_like(X)

    for src in sources:
        # Calculate Euclidean distance from this source to all pixels
        R = np.sqrt((X - src[0]) ** 2 + (Y - src[1]) ** 2)

        # Prevent division by zero directly at the source coordinate
        R = np.where(R < 0.1, 0.1, R)

        # Calculate the wave equation and add it to the total (Superposition)
        Z_source = (A / (R**alpha)) * np.sin(k * R - omega * t)
        Z_total += Z_source

    return Z_total


# 3. Setup the Plot for Animation
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_title(f"Wave Interference Pattern (alpha = {alpha})")
ax.set_xlabel("X Position")
ax.set_ylabel("Y Position")

# Initialize an empty image plot
Z_initial = calculate_superposition(X, Y, 0, sources, A, k, omega, alpha)
img = ax.imshow(
    Z_initial,
    extent=[-grid_size, grid_size, -grid_size, grid_size],
    origin="lower",
    cmap="RdBu",
    vmin=-2,
    vmax=2,
)
fig.colorbar(img, ax=ax, label="Wave Amplitude")


def update(frame):
    """Animation loop: increments time and updates the grid."""
    t = frame * 0.1  # Advance time
    Z_new = calculate_superposition(X, Y, t, sources, A, k, omega, alpha)
    img.set_data(Z_new)
    return [img]


# Create the animation object
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# To view this in a local IDE, use plt.show()
plt.show()

# (Optional: save as a GIF)
# ani.save('wave_interference.gif', writer='pillow', fps=20)
