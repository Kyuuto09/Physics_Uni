# Problem 1: Projectile Motion

### 1. Problem Statement

A projectile is fired from the ground with an initial velocity of 100 m/s at an angle of 37° above the horizontal. Assume no air resistance.
Find the differential equations of motion, time of flight, maximum height, and range. (Assuming gravity $g = 9.8 \text{ m/s}^2$).

---

### 2. Solution and Explanation

**Concept Intuition:**
Projectile motion is just two independent motions happening at the exact same time:

1. Moving forward at a constant speed (Horizontal).
2. Going up and falling back down due to gravity (Vertical).

First, we break the initial velocity (100 m/s) into these two pieces.
Using the standard 37° triangle approximations ($\sin(37^\circ) \approx 0.6$ and $\cos(37^\circ) \approx 0.8$):

- **Horizontal initial velocity ($v_{0x}$):** $100 \cdot \cos(37^\circ) = 100 \cdot 0.8 = 80 \text{ m/s}$
- **Vertical initial velocity ($v_{0y}$):** $100 \cdot \sin(37^\circ) = 100 \cdot 0.6 = 60 \text{ m/s}$

#### Part A: Differential Equations of Motion

Newton's Second Law states Force equals mass times acceleration ($F = ma$). Acceleration is the second derivative of position with respect to time ($\frac{d^2}{dt^2}$).

- **Horizontal ($x$-direction):** There is no air resistance, so there are zero forces pushing it left or right.
  $$m \frac{d^2x}{dt^2} = 0 \implies \frac{d^2x}{dt^2} = 0$$

- **Vertical ($y$-direction):** The only force is gravity pulling perfectly downward.
  $$m \frac{d^2y}{dt^2} = -mg \implies \frac{d^2y}{dt^2} = -g$$

#### Part B: Time of Flight

To find how long it stays in the air, we only look at the vertical motion. The projectile hits the ground when its vertical position is zero. Using the standard kinematic formula:
$$y(t) = v_{0y}t - \frac{1}{2}gt^2$$
Set $y = 0$ and solve for $t$:
$$0 = t(v_{0y} - \frac{1}{2}gt)$$
Since $t = 0$ is the launch, the landing time is:
$$t = \frac{2v_{0y}}{g}$$
$$t = \frac{2(60)}{9.8} \approx 12.24 \text{ seconds}$$

#### Part C: Maximum Height

The highest point occurs exactly halfway through the flight, when the vertical upward velocity hits zero before it starts falling.
We use the kinematic formula for peak height:
$$H = \frac{v_{0y}^2}{2g}$$
$$H = \frac{60^2}{2(9.8)} = \frac{3600}{19.6} \approx 183.67 \text{ meters}$$

#### Part D: Range (Total Horizontal Distance)

The range is simply the horizontal speed multiplied by the total time it was in the air.
$$\text{Range} = v_{0x} \cdot t$$
$$\text{Range} = 80 \cdot 12.24 \approx 979.2 \text{ meters}$$

---

### 3. Final Answers

- **Differential Equations:** $\frac{d^2x}{dt^2} = 0$ and $\frac{d^2y}{dt^2} = -g$
- **Time of Flight:** 12.24 s
- **Maximum Height:** 183.67 m
- **Range:** 979.2 m
