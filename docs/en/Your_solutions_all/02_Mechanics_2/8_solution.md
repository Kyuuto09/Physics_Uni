# Problem 8: Work of a Variable Force

### 1. Problem Statement

Given a one-dimensional force:
$$F(x) = -kx$$

- Write down the equation of motion and solve it.
- Calculate the work done during the displacement from $0$ to $x_0$.
- Interpret the result as potential energy.
- Verify the relationship $F = -\frac{dU}{dx}$.
- Draw the graph of $F(x)$ and $U(x)$.

---

### 2. Solution and Explanation

**Concept Intuition:**
The equation $F(x) = -kx$ is known as **Hooke's Law**. It describes a "restoring force," exactly like a spring. The negative sign means that if you pull the spring to the right (positive $x$), it pulls back to the left (negative force). The further you pull it, the harder it fights back, which is why the force is "variable" (it changes based on distance).

#### Part 1: Equation of Motion and its Solution

To find the equation of motion, we use Newton's Second Law ($F = ma$).
In calculus terms, acceleration ($a$) is the second derivative of position ($x$) with respect to time ($t$).
$$m \frac{d^2x}{dt^2} = -kx$$

If we divide by $m$, we get the standard differential equation for Simple Harmonic Motion (like the bouncing spring from Problem 2):
$$\frac{d^2x}{dt^2} + \frac{k}{m}x = 0$$

**The Solution:**
The solution to this specific equation is a wave function (sine or cosine), because the object will bounce back and forth forever.
$$x(t) = A \cos(\omega t + \phi)$$
_(Where $A$ is the maximum stretch, $\phi$ is the starting phase, and the angular frequency is $\omega = \sqrt{\frac{k}{m}}$)._

#### Part 2: Calculate the Work Done (from $0$ to $x_0$)

Because the force is constantly changing as you pull the spring, we cannot use simple multiplication. We must use an integral to add up all the tiny fractions of work done over the distance.
$$W = \int_{0}^{x_0} F(x) \, dx$$
$$W = \int_{0}^{x_0} (-kx) \, dx$$

Using the reverse Power Rule (add 1 to the invisible exponent of $x$, then divide by the new exponent):
$$W = \left[ -\frac{1}{2}kx^2 \right]_0^{x_0}$$
$$W = \left(-\frac{1}{2}kx_0^2\right) - \left(-\frac{1}{2}k(0)^2\right)$$
$$W = -\frac{1}{2}kx_0^2$$

#### Part 3: Interpret as Potential Energy

In physics, the work done _by_ a conservative force (like a spring) is equal to the _negative_ change in Potential Energy ($\Delta U$).
$$W = -\Delta U$$
$$W = -(U_{final} - U_{initial})$$

If we assume the potential energy is zero at the resting point ($U(0) = 0$), then:
$$-\frac{1}{2}kx_0^2 = -U(x_0)$$
$$U(x_0) = \frac{1}{2}kx_0^2$$
**Interpretation:** The negative work done by the spring as it is stretched translates perfectly into the positive **Elastic Potential Energy** stored inside it, ready to be released.

#### Part 4: Verify the Relationship $F = -\frac{dU}{dx}$

This rule states that Force is the negative derivative of Potential Energy. Let's test it using our $U(x)$ from Part 3.
$$U(x) = \frac{1}{2}kx^2$$

Take the derivative with respect to $x$ using the basic Power Rule:
$$\frac{dU}{dx} = 2 \cdot \frac{1}{2}kx^{2-1}$$
$$\frac{dU}{dx} = kx$$

Now apply the negative sign from the formula:
$$-\frac{dU}{dx} = -kx$$
This perfectly matches our original force equation, $F(x) = -kx$. The relationship is verified.

#### Part 5: Drawing the Graphs

- **The Force Graph $F(x) = -kx$:**
  This is a straight linear line passing directly through the origin $(0,0)$. Because of the negative sign, it has a downward slope. As $x$ goes positive (moving right), the $F$ line goes negative (pointing down).

- **The Potential Energy Graph $U(x) = \frac{1}{2}kx^2$:**
  Because the $x$ is squared, this graph is a perfect parabola (a "U" shape) opening upwards, with its very bottom tip resting at the origin $(0,0)$. This shows that stretching the spring in _either_ direction (positive or negative) increases the stored energy.

---

### 3. Final Summary

- **Equation of Motion:** $\frac{d^2x}{dt^2} + \frac{k}{m}x = 0 \implies x(t) = A \cos(\omega t + \phi)$
- **Work Done:** $W = -\frac{1}{2}kx_0^2$
- **Potential Energy ($U$):** $U(x) = \frac{1}{2}kx^2$
- **Verification:** $-\frac{d}{dx}(\frac{1}{2}kx^2) = -kx = F(x)$
