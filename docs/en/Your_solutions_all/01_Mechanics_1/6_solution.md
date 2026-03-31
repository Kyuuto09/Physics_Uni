# Problem 6: Variable Velocity

### 1. Problem Statement

An object's velocity is given by $v(t) = t^2 + 2t - 5$. If the object was at $x=4$ at $t=0$, what is its position and acceleration at time $t=3$?

---

### 2. Solution and Explanation

**Concept Intuition:**
Velocity is the middle step between position and acceleration.

- To find acceleration, we go one step "forward" by taking the **derivative** of velocity.
- To find position, we go one step "backward" by taking the **integral** (antiderivative) of velocity.

#### Part A: Find Acceleration at $t=3$

Acceleration is the first derivative of velocity:
$$a(t) = \frac{dv}{dt}$$

Using the power rule on $v(t) = t^2 + 2t - 5$:

- The derivative of $t^2$ is $2t$.
- The derivative of $2t$ is $2$.
- The constant $-5$ becomes $0$.

$$a(t) = 2t + 2$$

Now, plug in $t=3$:
$$a(3) = 2(3) + 2$$
$$a(3) = 6 + 2 = 8$$

#### Part B: Find Position at $t=3$

Position is the integral of velocity:
$$x(t) = \int v(t) \, dt$$
$$x(t) = \int (t^2 + 2t - 5) \, dt$$

Using the reverse power rule (add 1 to the exponent, then divide by the new exponent):
$$x(t) = \frac{t^3}{3} + \frac{2t^2}{2} - 5t + C$$
$$x(t) = \frac{t^3}{3} + t^2 - 5t + C$$

We must find the constant $C$. The problem states that at $t=0$, the position $x=4$. Plug these in:
$$4 = \frac{0^3}{3} + 0^2 - 5(0) + C$$
$$4 = C$$

So, our exact position formula is:
$$x(t) = \frac{t^3}{3} + t^2 - 5t + 4$$

Now, plug in $t=3$ to find the final position:
$$x(3) = \frac{3^3}{3} + 3^2 - 5(3) + 4$$
$$x(3) = \frac{27}{3} + 9 - 15 + 4$$
$$x(3) = 9 + 9 - 15 + 4$$
$$x(3) = 18 - 15 + 4 = 7$$

---

### 3. Final Answers

- **Acceleration at $t=3$:** $8$
- **Position at $t=3$:** $7$
