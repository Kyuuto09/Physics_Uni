# Problem 3: Superposition Principle

### 1. Problem Statement

Two waves are described by the equations $y_1(x, t) = A \sin(kx - \omega t)$ and $y_2(x, t) = A \sin(kx + \omega t)$. What is the equation of the resulting standing wave? Identify the positions of the nodes.

---

### 2. Solution and Explanation

**Concept Intuition:**
Think of the "Superposition Principle" as element-wise array addition. If you have two separate audio signals (waves) running through the same medium (like a string or air), their physical displacements simply add together at every exact coordinate ($x$) and every exact millisecond ($t$).

When a wave moving right ($y_1$) perfectly overlaps with an identical wave moving left ($y_2$), they create a "Standing Wave." Instead of looking like a pulse traveling across the screen, the resulting data simply vibrates up and down in place.

**Nodes** are the "null pointers" of this physical system—exact coordinates where the right-moving wave and the left-moving wave _always_ perfectly cancel each other out, resulting in a permanent zero value.

#### Step 1: Add the Wave Equations (Superposition)

To find the resulting wave $y(x,t)$, we sum the two equations:
$$y(x, t) = y_1(x, t) + y_2(x, t)$$
$$y(x, t) = A \sin(kx - \omega t) + A \sin(kx + \omega t)$$

#### Step 2: Apply the Trigonometric Identity

To simplify the addition of two sine functions, we use the standard sum-to-product trigonometric identity:
$$\sin(\alpha) + \sin(\beta) = 2 \sin\left(\frac{\alpha + \beta}{2}\right) \cos\left(\frac{\alpha - \beta}{2}\right)$$

Let $\alpha = kx - \omega t$ and $\beta = kx + \omega t$.
First, find the sum and difference for the numerators:

- $\alpha + \beta = (kx - \omega t) + (kx + \omega t) = 2kx$
- $\alpha - \beta = (kx - \omega t) - (kx + \omega t) = -2\omega t$

Now plug them into the identity:
$$y(x, t) = A \left[ 2 \sin\left(\frac{2kx}{2}\right) \cos\left(\frac{-2\omega t}{2}\right) \right]$$
$$y(x, t) = 2A \sin(kx) \cos(-\omega t)$$

Since the cosine function is even ($\cos(-\theta) = \cos(\theta)$), the negative sign disappears:
**Standing Wave Equation:**
$$y(x, t) = [2A \sin(kx)] \cos(\omega t)$$

_Note how the equation is now split. The $[2A \sin(kx)]$ part acts as a fixed "Amplitude Map" based purely on position, while the $\cos(\omega t)$ handles the ticking "clock" making it vibrate over time._

#### Step 3: Identify the Positions of the Nodes

Nodes occur exactly where the string never moves. This means the amplitude portion of our new equation must be perfectly equal to zero.
$$2A \sin(kx) = 0$$
$$\sin(kx) = 0$$

The sine function outputs zero at integer multiples of $\pi$ ($0, \pi, 2\pi, 3\pi...$).
Therefore, we set the inside of the sine function equal to $n\pi$:
$$kx = n\pi \quad \text{where } n = 0, 1, 2, 3, \dots$$

Since the wave number $k = \frac{2\pi}{\lambda}$, we substitute that in:
$$\left(\frac{2\pi}{\lambda}\right) x = n\pi$$

Solve for $x$:
$$x = \frac{n\pi \lambda}{2\pi}$$
$$x = \frac{n\lambda}{2}$$

---

### 3. Final Answers

- **Standing Wave Equation:** $y(x, t) = 2A \sin(kx) \cos(\omega t)$
- **Positions of Nodes:** $x = 0, \frac{\lambda}{2}, \lambda, \frac{3\lambda}{2}, \dots$ (Every half-wavelength).
