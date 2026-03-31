# Problem 3: Conservation of Energy

### 1. Problem Statement

A pendulum with a length of 1.0 meter is released from an initial angle of $15^\circ$. What is the speed of the pendulum bob at the bottom of its swing?

---

### 2. Solution and Explanation

**Concept Intuition:**
This problem is a classic example of the Law of Conservation of Energy. When you pull the pendulum back, you are storing **Gravitational Potential Energy (PE)** because you are lifting it slightly off its resting position. When you let go, it falls, and all of that stored energy is perfectly converted into **Kinetic Energy (KE)** (speed) at the very bottom of the swing.

The mass of the bob doesn't matter because a heavy bob has more stored energy, but also requires more energy to get moving. The mass simply cancels out of the equation.

#### Step 1: Find the Initial Height ($h$)

Before we can calculate energy, we need to know exactly how high the pendulum was lifted.
When the pendulum is pulled back at an angle $\theta$, it forms a right triangle with the vertical axis.

The vertical piece of that triangle (adjacent to the angle) is $L \cos(\theta)$.
Therefore, the actual height $h$ the bob was lifted from the bottom is the total length $L$ minus that vertical piece:
$$h = L - L \cos(\theta)$$
$$h = L(1 - \cos(\theta))$$

Plug in our known values ($L = 1.0$ m, $\theta = 15^\circ$):
$$h = 1.0 \cdot (1 - \cos(15^\circ))$$
$$h = 1.0 \cdot (1 - 0.9659)$$
$$h \approx 0.0341 \text{ meters}$$

#### Step 2: Apply Conservation of Energy

The total energy at the top (purely Potential) equals the total energy at the bottom (purely Kinetic).
$$PE_{top} = KE_{bottom}$$
$$mgh = \frac{1}{2}mv^2$$

Because mass ($m$) is on both sides, we can divide it out completely:
$$gh = \frac{1}{2}v^2$$

#### Step 3: Solve for Velocity ($v$)

Now we just use algebra to get the velocity ($v$) by itself.
Multiply both sides by 2:
$$2gh = v^2$$

Take the square root of both sides:
$$v = \sqrt{2gh}$$

Plug in Earth's gravity ($g = 9.81 \text{ m/s}^2$) and the height ($h = 0.0341$ m) we found in Step 1:
$$v = \sqrt{2 \cdot 9.81 \cdot 0.0341}$$
$$v = \sqrt{0.669}$$
$$v \approx 0.818 \text{ m/s}$$

---

### 3. Final Answer

- **Speed at the bottom of the swing:** $\approx 0.818 \text{ m/s}$
