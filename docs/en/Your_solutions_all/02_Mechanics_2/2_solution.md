# Problem 2: Harmonic Motion

### 1. Problem Statement

A 10 kg mass is attached to a spring and oscillates according to the equation $x(t) = 0.2 \cos(10\pi t)$ (in meters). What is the spring constant $k$? What is the total mechanical energy of the system?

---

### 2. Solution and Explanation

**Concept Intuition:**
Instead of trying to do heavy math right away, treat this problem like parsing data from an API. In physics, the standard "blueprint" formula for a bouncing spring (Simple Harmonic Motion) is:
$$x(t) = A \cos(\omega t)$$

If we line our specific equation up directly beneath the blueprint, we can instantly extract two hidden variables without doing any math at all:

1.  **Amplitude ($A$):** The number in the very front is the maximum stretch. So, $A = 0.2$ meters.
2.  **Angular Frequency ($\omega$):** The number sitting right next to the $t$ is the "speed of the wiggle". So, $\omega = 10\pi$ rad/s.

#### Part 1: Finding the Spring Constant ($k$)

The spring constant ($k$) just tells us how stiff the spring is. A higher $k$ means a stiffer spring. The physics formula that links the speed of the wiggle ($\omega$), the mass ($m$), and the stiffness ($k$) is:
$$\omega = \sqrt{\frac{k}{m}}$$

Let's use algebra to get $k$ by itself.

1. Square both sides to eliminate the square root:
   $$\omega^2 = \frac{k}{m}$$
2. Multiply both sides by $m$:
   $$k = m \cdot \omega^2$$

Now, we just plug in our 10 kg mass and the $\omega$ we extracted earlier:
$$k = 10 \cdot (10\pi)^2$$
$$k = 10 \cdot 100\pi^2$$
$$k = 1000\pi^2$$

$1000 \cdot \pi^2 \approx 9869.6$ N/m.

#### Part 2: Finding the Total Mechanical Energy ($E$)

The total energy of a bouncing spring system is locked entirely into its maximum stretch. The formula for the total energy is:
$$E = \frac{1}{2} k A^2$$

We just found $k$, and we parsed $A$ from the original equation ($A = 0.2$). We just plug them in:
$$E = \frac{1}{2} (1000\pi^2) (0.2)^2$$
$$E = 500\pi^2 \cdot 0.04$$
$$E = 20\pi^2$$

($20 \cdot \pi^2 \approx 197.4$ Joules)

---

### 3. Final Answers

- **Spring Constant ($k$):** $1000\pi^2$ N/m (approx. 9869.6 N/m)
- **Total Mechanical Energy ($E$):** $20\pi^2$ Joules (approx. 197.4 Joules)
