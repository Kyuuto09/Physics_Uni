# Problem 2: Range Optimization

### 1. Problem Statement

For projectile motion, show analytically that the maximum range:
$$R(\theta) = \frac{v_0^2 \sin(2\theta)}{g}$$
for a given initial velocity is achieved at a launch angle of $45^\circ$.

---

### 2. Solution and Explanation

**Concept Intuition:**
To throw something as far as possible, you need a perfect balance. Throw it too high (like $80^\circ$), and it stays in the air a long time but doesn't travel forward. Throw it too low (like $10^\circ$), and it moves forward extremely fast but hits the ground almost immediately. The angle of $45^\circ$ is the exact mathematical middle ground between vertical hang-time and horizontal speed.

#### The Simplest Analytical Method (Trigonometry)

**Step 1: Identify the constants**
In the formula $R(\theta) = \frac{v_0^2 \sin(2\theta)}{g}$, the initial velocity ($v_0$) and gravity ($g$) are fixed constants. The only variable that changes the range is the trigonometric piece: $\sin(2\theta)$.

**Step 2: Maximize the Sine function**
In trigonometry, the highest possible value that any sine function can ever output is exactly $1$. To maximize the range $R$, we simply set that part of the formula to its maximum value:
$$\sin(2\theta) = 1$$

**Step 3: Solve for the angle**
On the mathematical unit circle, the angle that produces a sine of $1$ is $90^\circ$.
$$2\theta = 90^\circ$$

Divide both sides by $2$:
$$\theta = 45^\circ$$

#### The Calculus Backup Method (Derivatives)

_(If required to use calculus for optimization)_
To find the maximum of any function, we take the derivative and set it to zero.

1. Take the derivative of $R$ with respect to $\theta$:
   $$R'(\theta) = \frac{v_0^2}{g} \cdot \cos(2\theta) \cdot 2$$
2. Set it to zero to find the peak:
   $$0 = \cos(2\theta)$$
3. Cosine is zero at $90^\circ$, so:
   $$2\theta = 90^\circ \implies \theta = 45^\circ$$

---

### 3. Final Answer

By maximizing the $\sin(2\theta)$ term to its peak value of $1$, we analytically prove the launch angle must be exactly **$45^\circ$**.
