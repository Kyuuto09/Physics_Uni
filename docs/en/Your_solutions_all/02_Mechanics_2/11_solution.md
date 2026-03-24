# Problem 11: Dynamics with a Time-Dependent Force

### 1. Problem Statement

A particle of mass $m=3$ kg moves in a force field $F$ dependent on time in the following way:
$$F = (15t, 3t-12, -6t^2) \text{ N}$$

Assuming initial conditions $r_0=(5,2,-3)$ m, $v_0=(2,0,1)$ m/s, find the dependence of the particle's position and velocity on time.

---

### 2. Solution and Explanation

**Concept Intuition:**
Because the force is constantly changing with time, the acceleration is also changing. We cannot use simple algebra formulas here. Instead, we must use Newton's Second Law ($F = ma$) to find the acceleration, and then use integral calculus to step "up" the ladder:

1. Integrate Acceleration to find Velocity.
2. Integrate Velocity to find Position.

The initial conditions ($v_0$ and $r_0$) are the "constants of integration" (the $+ C$) that we add at the end of each step to anchor the math to the particle's actual starting state.

#### Step 1: Find Acceleration ($\vec{a}$)

From Newton's Second Law, $\vec{F} = m\vec{a}$, which means $\vec{a} = \frac{\vec{F}}{m}$.
We simply divide each component of the force vector by the mass ($m = 3$ kg):

- $a_x(t) = \frac{15t}{3} = 5t$
- $a_y(t) = \frac{3t - 12}{3} = t - 4$
- $a_z(t) = \frac{-6t^2}{3} = -2t^2$

$$\vec{a}(t) = (5t)\hat{i} + (t - 4)\hat{j} - (2t^2)\hat{k}$$

#### Step 2: Find Velocity ($\vec{v}$)

Velocity is the integral of acceleration with respect to time: $\vec{v}(t) = \int \vec{a}(t) \, dt + \vec{v}_0$.
We integrate each component using the reverse Power Rule (add 1 to the exponent, divide by the new exponent), and then add the corresponding initial velocity piece from $v_0 = (2, 0, 1)$:

- **X-component:** $v_x(t) = \int 5t \, dt = \frac{5}{2}t^2 + C_x$
  Since $v_{0x} = 2$, we get: $v_x(t) = 2.5t^2 + 2$

- **Y-component:**
  $v_y(t) = \int (t - 4) \, dt = \frac{1}{2}t^2 - 4t + C_y$
  Since $v_{0y} = 0$, we get: $v_y(t) = 0.5t^2 - 4t$

- **Z-component:**
  $v_z(t) = \int (-2t^2) \, dt = -\frac{2}{3}t^3 + C_z$
  Since $v_{0z} = 1$, we get: $v_z(t) = -\frac{2}{3}t^3 + 1$

$$\vec{v}(t) = (2.5t^2 + 2)\hat{i} + (0.5t^2 - 4t)\hat{j} + \left(-\frac{2}{3}t^3 + 1\right)\hat{k}$$

#### Step 3: Find Position ($\vec{r}$)

Position is the integral of velocity with respect to time: $\vec{r}(t) = \int \vec{v}(t) \, dt + \vec{r}_0$.
We integrate our new velocity components and add the initial position pieces from $r_0 = (5, 2, -3)$:

- **X-component:**
  $x(t) = \int (2.5t^2 + 2) \, dt = \frac{2.5}{3}t^3 + 2t + C_x = \frac{5}{6}t^3 + 2t + C_x$
  Since $r_{0x} = 5$, we get: $x(t) = \frac{5}{6}t^3 + 2t + 5$

- **Y-component:**
  $y(t) = \int (0.5t^2 - 4t) \, dt = \frac{0.5}{3}t^3 - \frac{4}{2}t^2 + C_y = \frac{1}{6}t^3 - 2t^2 + C_y$
  Since $r_{0y} = 2$, we get: $y(t) = \frac{1}{6}t^3 - 2t^2 + 2$

- **Z-component:**
  $z(t) = \int \left(-\frac{2}{3}t^3 + 1\right) \, dt = -\frac{2}{12}t^4 + t + C_z = -\frac{1}{6}t^4 + t + C_z$
  Since $r_{0z} = -3$, we get: $z(t) = -\frac{1}{6}t^4 + t - 3$

$$\vec{r}(t) = \left(\frac{5}{6}t^3 + 2t + 5\right)\hat{i} + \left(\frac{1}{6}t^3 - 2t^2 + 2\right)\hat{j} + \left(-\frac{1}{6}t^4 + t - 3\right)\hat{k}$$

---

### 3. Final Answers

- **Velocity Time Dependence:** $$\vec{v}(t) = \left(2.5t^2 + 2, \quad 0.5t^2 - 4t, \quad -\frac{2}{3}t^3 + 1\right) \text{ m/s}$$

- **Position Time Dependence:** $$\vec{r}(t) = \left(\frac{5}{6}t^3 + 2t + 5, \quad \frac{1}{6}t^3 - 2t^2 + 2, \quad -\frac{1}{6}t^4 + t - 3\right) \text{ m}$$
