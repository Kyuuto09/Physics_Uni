# Problem 10: Kinematics and Trajectory

### 1. Problem Statement

Point $M$ moves according to the equation:
$$\vec{r}(t) = (a \cos(\omega t), b \sin(\omega t), bt)$$
where $a, b, \omega$ are positive constants.
a) Find the equation of the point's trajectory.
b) Compute the path length of the point from time $t=0$ to $t=t_0$.
c) Discuss the trajectory shape and special cases.

---

### 2. Solution and Explanation

#### Part A: Equation of the Trajectory

To find the shape of the path on the flat xy-plane, we eliminate the time variable $t$:
$$x = a \cos(\omega t) \implies \cos(\omega t) = \frac{x}{a}$$
$$y = b \sin(\omega t) \implies \sin(\omega t) = \frac{y}{b}$$

Using the trigonometric identity $\cos^2(\theta) + \sin^2(\theta) = 1$:
$$\left(\frac{x}{a}\right)^2 + \left(\frac{y}{b}\right)^2 = 1$$

This is the equation of an **ellipse**. Because the z-coordinate ($z = bt$) grows steadily with time, the point constantly rises. The full 3D shape is an **elliptical helix** (like a stretched spiral staircase).

#### Part B: Path Length

Path length $L$ is the integral of the velocity magnitude (speed).
First, find the velocity vector by taking the derivative of position $\vec{r}(t)$:
$$\vec{v}(t) = (-a\omega \sin(\omega t), b\omega \cos(\omega t), b)$$

Find the magnitude (speed) using the 3D Pythagorean theorem:
$$|\vec{v}(t)| = \sqrt{(-a\omega \sin(\omega t))^2 + (b\omega \cos(\omega t))^2 + b^2}$$
$$|\vec{v}(t)| = \sqrt{a^2\omega^2 \sin^2(\omega t) + b^2\omega^2 \cos^2(\omega t) + b^2}$$

The path length is the integral of this speed from $0$ to $t_0$:
$$L = \int_0^{t_0} \sqrt{a^2\omega^2 \sin^2(\omega t) + b^2\omega^2 \cos^2(\omega t) + b^2} \, dt$$
_(This is an elliptic integral and cannot be simplified further without specific numbers)._

#### Part C: Special Cases

If $a = b$, the base of the shape becomes a perfect circle ($x^2 + y^2 = a^2$).
The speed formula simplifies beautifully because $\sin^2 + \cos^2 = 1$:
$$|\vec{v}(t)| = \sqrt{a^2\omega^2(1) + b^2}$$
Since the speed is now a constant, the integral is just speed multiplied by time:
$$L = t_0 \sqrt{a^2\omega^2 + b^2}$$
This special case forms a perfect **circular helix**.

---

### 3. Final Answers

- **Trajectory Equation:** $\left(\frac{x}{a}\right)^2 + \left(\frac{y}{b}\right)^2 = 1$ (Elliptical helix)
- **Path Length Integral:** $L = \int_0^{t_0} \sqrt{a^2\omega^2 \sin^2(\omega t) + b^2\omega^2 \cos^2(\omega t) + b^2} \, dt$
- **Special Case ($a=b$):** Circular helix, length is $L = t_0 \sqrt{a^2\omega^2 + b^2}$
