# Problem 8: Waves (The Wave Equation)

### 1. Problem Statement

Which of the following functions can describe a traveling wave? Hint: check if it satisfies the wave equation:
$$\frac{\partial^2 y}{\partial x^2} = \frac{1}{v^2} \frac{\partial^2 y}{\partial t^2}$$

a) $y(x,t) = A \cos(kx^2 - \omega t)$
b) $y(x,t) = A(x-vt)^2$
c) $y(x,t) = A \log(x+vt)$

---

### 2. Solution and Explanation

**Concept Intuition:**
Think of the wave equation as a strict **Unit Test** that every mathematical function must pass to be classified as a valid "Traveling Wave."

Physically, a traveling wave must move its exact shape smoothly through space without stretching, warping, or distorting. To achieve this, the position variable ($x$) and the time variable ($t$) must be locked together in a linear package, usually looking like $(x - vt)$ or $(x + vt)$. If a function squares $x$ but doesn't square $t$, the shape will accelerate and distort over time, failing the test.

To run the test, we take the second derivative with respect to space ($x$) and see if it perfectly equals the second derivative with respect to time ($t$) divided by $v^2$.

#### Part a) Testing $y(x,t) = A \cos(kx^2 - \omega t)$

Let's find the second partial derivative with respect to $x$ (using the Chain Rule and Product Rule):

1. $\frac{\partial y}{\partial x} = -A \sin(kx^2 - \omega t) \cdot (2kx)$
2. $\frac{\partial^2 y}{\partial x^2} = -2Ak \sin(kx^2 - \omega t) - 4Ak^2x^2 \cos(kx^2 - \omega t)$

Now, let's find the second partial derivative with respect to $t$:

1. $\frac{\partial y}{\partial t} = -A \sin(kx^2 - \omega t) \cdot (-\omega) = A\omega \sin(kx^2 - \omega t)$
2. $\frac{\partial^2 y}{\partial t^2} = -A\omega^2 \cos(kx^2 - \omega t)$

**The Test:** Does $\frac{\partial^2 y}{\partial x^2} = \frac{1}{v^2} \frac{\partial^2 y}{\partial t^2}$?
No. The $x$-derivative generated a massive $-4Ak^2x^2$ term and a stray sine term. There is no constant $v$ that can make these two sides equal. The nonlinear $x^2$ inside the function causes the wave to distort.
_Result: Fails. Not a traveling wave._

#### Part b) Testing $y(x,t) = A(x-vt)^2$

Find the second partial derivative with respect to $x$:

1. $\frac{\partial y}{\partial x} = 2A(x - vt) \cdot (1) = 2A(x - vt)$
2. $\frac{\partial^2 y}{\partial x^2} = 2A$

Find the second partial derivative with respect to $t$:

1. $\frac{\partial y}{\partial t} = 2A(x - vt) \cdot (-v) = -2Av(x - vt)$
2. $\frac{\partial^2 y}{\partial t^2} = -2Av(-v) = 2Av^2$

**The Test:** Does $\frac{\partial^2 y}{\partial x^2} = \frac{1}{v^2} \frac{\partial^2 y}{\partial t^2}$?
Substitute our results in:
$$2A = \frac{1}{v^2} (2Av^2)$$
$$2A = 2A$$
_Result: Passes. This perfectly satisfies the wave equation._ (Note: While mathematically valid, a shape that grows infinitely large like a parabola isn't a realistic physical wave on a string, but it is a valid traveling mathematical pulse).

#### Part c) Testing $y(x,t) = A \log(x+vt)$

Find the second partial derivative with respect to $x$:

1. $\frac{\partial y}{\partial x} = A \cdot \frac{1}{x+vt} \cdot (1) = \frac{A}{x+vt}$
2. $\frac{\partial^2 y}{\partial x^2} = -\frac{A}{(x+vt)^2}$

Find the second partial derivative with respect to $t$:

1. $\frac{\partial y}{\partial t} = A \cdot \frac{1}{x+vt} \cdot (v) = \frac{Av}{x+vt}$
2. $\frac{\partial^2 y}{\partial t^2} = -\frac{Av^2}{(x+vt)^2}$

**The Test:** Does $\frac{\partial^2 y}{\partial x^2} = \frac{1}{v^2} \frac{\partial^2 y}{\partial t^2}$?
Substitute our results in:
$$-\frac{A}{(x+vt)^2} = \frac{1}{v^2} \left(-\frac{Av^2}{(x+vt)^2}\right)$$
$$-\frac{A}{(x+vt)^2} = -\frac{A}{(x+vt)^2}$$
_Result: Passes. This perfectly satisfies the wave equation._

---

### 3. Final Answers

- **a)** No, it does not satisfy the wave equation.
- **b)** Yes, it describes a traveling wave.
- **c)** Yes, it describes a traveling wave.
