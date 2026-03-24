# Problem 10: Force Field and Power

### 1. Problem Statement

In a certain force field, the equations of motion of a particle with mass $m=0.5$ kg are as follows:
$$x = 5t^2 - t, \quad y = 2t^3, \quad z = -3t + 2$$

Find the time dependence of: the particle's velocity, the particle's momentum, the particle's acceleration, the force acting on the particle, and the power transferred by the field to the particle.

---

### 2. Solution and Explanation

**Concept Intuition:**
This problem is a complete tour of kinematics and dynamics using calculus.
When we are given position equations for $x$, $y$, and $z$, we treat them as independent 1D problems. We take the derivative with respect to time ($t$) to step down from Position $\rightarrow$ Velocity $\rightarrow$ Acceleration.

Once we have the motion (kinematics), we multiply by the mass ($m$) to find the physical impact (dynamics) like Momentum and Force. Finally, Power is calculated by finding the "dot product" of Force and Velocity, which simply means multiplying their matching directional pieces together and adding them up.

#### Step 1: Find Velocity ($\vec{v}$)

Velocity is the first derivative of position with respect to time: $\vec{v} = \frac{d\vec{r}}{dt}$.
We apply the Power Rule to each coordinate separately:

- $v_x = \frac{d}{dt}(5t^2 - t) = 10t - 1$
- $v_y = \frac{d}{dt}(2t^3) = 6t^2$
- $v_z = \frac{d}{dt}(-3t + 2) = -3$

$$\vec{v}(t) = (10t - 1)\hat{i} + (6t^2)\hat{j} - 3\hat{k}$$

#### Step 2: Find Momentum ($\vec{p}$)

Momentum is simply mass times velocity: $\vec{p} = m\vec{v}$.
We multiply our velocity vector by the mass ($m = 0.5$ kg):

- $p_x = 0.5 \cdot (10t - 1) = 5t - 0.5$
- $p_y = 0.5 \cdot (6t^2) = 3t^2$
- $p_z = 0.5 \cdot (-3) = -1.5$

$$\vec{p}(t) = (5t - 0.5)\hat{i} + (3t^2)\hat{j} - 1.5\hat{k}$$

#### Step 3: Find Acceleration ($\vec{a}$)

Acceleration is the derivative of velocity with respect to time: $\vec{a} = \frac{d\vec{v}}{dt}$.
We take the derivative of the velocity components we found in Step 1:

- $a_x = \frac{d}{dt}(10t - 1) = 10$
- $a_y = \frac{d}{dt}(6t^2) = 12t$
- $a_z = \frac{d}{dt}(-3) = 0$

$$\vec{a}(t) = 10\hat{i} + 12t\hat{j}$$

#### Step 4: Find the Force ($\vec{F}$)

According to Newton's Second Law, Force is mass times acceleration: $\vec{F} = m\vec{a}$.
We multiply our acceleration vector by the mass ($m = 0.5$ kg):

- $F_x = 0.5 \cdot 10 = 5$
- $F_y = 0.5 \cdot 12t = 6t$
- $F_z = 0.5 \cdot 0 = 0$

$$\vec{F}(t) = 5\hat{i} + 6t\hat{j}$$

#### Step 5: Find the Power ($P$)

Power transferred by a force to a moving particle is the dot product of the Force vector and the Velocity vector: $P = \vec{F} \cdot \vec{v}$.
To calculate a dot product, we multiply the $x$'s together, the $y$'s together, and the $z$'s together, then add them all up into a single scalar number.

- $P_x = F_x \cdot v_x = 5 \cdot (10t - 1) = 50t - 5$
- $P_y = F_y \cdot v_y = 6t \cdot (6t^2) = 36t^3$
- $P_z = F_z \cdot v_z = 0 \cdot (-3) = 0$

Add them together for the total power:
$$P(t) = 36t^3 + 50t - 5$$

---

### 3. Final Answers

- **Velocity:** $\vec{v}(t) = (10t - 1)\hat{i} + 6t^2\hat{j} - 3\hat{k}$
- **Momentum:** $\vec{p}(t) = (5t - 0.5)\hat{i} + 3t^2\hat{j} - 1.5\hat{k}$
- **Acceleration:** $\vec{a}(t) = 10\hat{i} + 12t\hat{j}$
- **Force:** $\vec{F}(t) = 5\hat{i} + 6t\hat{j}$
- **Power:** $P(t) = 36t^3 + 50t - 5$
