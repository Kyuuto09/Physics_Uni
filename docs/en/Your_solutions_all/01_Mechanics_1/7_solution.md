# Problem 7: Elimination of Time and Interpretation of Acceleration

### 1. Problem Statement

The path equation is given in parametric form:
$$x(t) = 2t^2, \qquad y(t) = 3t^3$$

- Eliminate the parameter $t$.
- Draw the trajectory.
- Calculate $\vec{v}(t)$, $|\vec{v}(t)|$, $\vec{a}(t)$, and $|\vec{a}(t)|$.
- Is the acceleration constant?

---

### 2. Solution and Explanation

**Concept Intuition:**
Right now, the $x$ and $y$ coordinates are controlled by a "hidden clock" called $t$ (time).

- "Eliminating $t$" just means rewriting the equation so $y$ connects directly to $x$ without needing the clock, just like a normal graph.
- Finding velocity and acceleration is just taking derivatives (the Power Rule), and finding their magnitudes (the $|$ symbols|) is just using the Pythagorean theorem.

#### Part A: Eliminate the parameter $t$

We will use the substitution method. First, isolate $t$ in the simpler $x$ equation:
$$x = 2t^2$$
Divide by 2:
$$\frac{x}{2} = t^2$$
Take the square root (assuming $t \ge 0$):
$$t = \sqrt{\frac{x}{2}}$$

Now, substitute this definition of $t$ into the $y$ equation:
$$y = 3t^3$$
$$y = 3\left(\sqrt{\frac{x}{2}}\right)^3$$
_(To make this look cleaner, you can write it as a fractional exponent or square both sides to get $y^2 = \frac{9}{8}x^3$. Both are correct)._

#### Part B: Draw the trajectory

_(For the drawing portion of the assignment, this graph forms a "semi-cubical parabola", which looks like a curve starting at the origin $(0,0)$ and swooping upwards and to the right, getting steeper as it goes)._

#### Part C: Calculate Vectors and Magnitudes

**1. Velocity Vector $\vec{v}(t)$:** Take the first derivative of position.

- $x(t) = 2t^2 \implies v_x = 4t$
- $y(t) = 3t^3 \implies v_y = 9t^2$
  $$\vec{v}(t) = [4t, 9t^2]$$

**2. Velocity Magnitude $|\vec{v}(t)|$:** Use the Pythagorean theorem $\sqrt{a^2 + b^2}$.
$$|\vec{v}(t)| = \sqrt{(4t)^2 + (9t^2)^2}$$
$$|\vec{v}(t)| = \sqrt{16t^2 + 81t^4}$$

**3. Acceleration Vector $\vec{a}(t)$:** Take the derivative of velocity.

- $v_x = 4t \implies a_x = 4$
- $v_y = 9t^2 \implies a_y = 18t$
  $$\vec{a}(t) = [4, 18t]$$

**4. Acceleration Magnitude $|\vec{a}(t)|$:** Use the Pythagorean theorem again.
$$|\vec{a}(t)| = \sqrt{(4)^2 + (18t)^2}$$
$$|\vec{a}(t)| = \sqrt{16 + 324t^2}$$

#### Part D: Is the acceleration constant?

Look at our acceleration vector: $\vec{a}(t) = [4, 18t]$.
Because the $y$-component still contains the variable $t$, the vertical acceleration changes every single second. Therefore, the overall acceleration is **not constant**.

---

### 3. Final Answers

- **Trajectory Equation:** $y = 3\left(\sqrt{\frac{x}{2}}\right)^3$ or $y^2 = \frac{9}{8}x^3$
- **Velocity:** $\vec{v}(t) = [4t, 9t^2]$
- **Speed (Mag):** $|\vec{v}(t)| = \sqrt{16t^2 + 81t^4}$
- **Acceleration:** $\vec{a}(t) = [4, 18t]$
- **Acc (Mag):** $|\vec{a}(t)| = \sqrt{16 + 324t^2}$
- **Constant Accel?** No.
