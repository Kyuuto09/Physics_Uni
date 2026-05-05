# Problem 9: Refraction (Snell's Law)

### 1. Problem Statement

A light ray travels from air ($n=1.00$) into glass ($n=1.50$). If the angle of incidence is $30^\circ$, what is the angle of refraction?

---

### 2. Solution and Explanation

**Concept Intuition:**
When light passes from one transparent medium into another, its speed changes. This change in speed causes the path of the light ray to bend, a phenomenon known as **refraction**. 

A critical rule of thumb for refraction is:
- When light enters a **denser** medium (higher index of refraction $n$), it slows down and bends **towards** the normal line.
- When light enters a **less dense** medium (lower $n$), it speeds up and bends **away** from the normal line.

*(Note: The "normal line" is an imaginary line perfectly perpendicular to the boundary between the two materials. All angles in optics are measured against this normal line, not against the flat surface itself!)*

In this problem, light is moving from air ($n=1.00$) into denser glass ($n=1.50$). Therefore, before we even do the math, we know our final angle of refraction *must* be smaller than our $30^\circ$ angle of incidence because it is bending towards the normal.

#### Step 1: Identify Known Variables
- Index of refraction of medium 1 (air): $n_1 = 1.00$
- Index of refraction of medium 2 (glass): $n_2 = 1.50$
- Angle of incidence: $\theta_1 = 30^\circ$

#### Step 2: Set Up Snell's Law
The mathematical relationship governing refraction is Snell's Law:
$$n_1 \cdot \sin(\theta_1) = n_2 \cdot \sin(\theta_2)$$

#### Step 3: Calculation
Substitute our known values into the equation:
$$1.00 \cdot \sin(30^\circ) = 1.50 \cdot \sin(\theta_2)$$

We know from trigonometry that $\sin(30^\circ) = 0.5$:
$$1.00 \cdot 0.5 = 1.50 \cdot \sin(\theta_2)$$
$$0.5 = 1.50 \cdot \sin(\theta_2)$$

Now, isolate $\sin(\theta_2)$ by dividing both sides by $1.50$:
$$\sin(\theta_2) = \frac{0.5}{1.50}$$
$$\sin(\theta_2) = \frac{1}{3}$$
$$\sin(\theta_2) \approx 0.3333$$

Finally, we use the inverse sine function (arcsin or $\sin^{-1}$) to find the angle itself:
$$\theta_2 = \arcsin\left(\frac{1}{3}\right)$$
$$\theta_2 \approx 19.47^\circ$$

As predicted in our concept intuition, $19.47^\circ$ is indeed smaller than the initial $30^\circ$, proving the light bent toward the normal!

---

### 3. Final Answer

- **Angle of Refraction ($\theta_2$):** $\approx 19.47^\circ$
