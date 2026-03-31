# Problem 4: Phase Difference

### 1. Problem Statement

What is the phase difference in radians between two points on a wave that are separated by a distance of $\lambda/3$?

---

### 2. Solution and Explanation

**Concept Intuition:**
Think of a wave as a repeating loop, like a continuous background animation cycle. In physics, we measure this repeating cycle in radians, where one complete loop is exactly $2\pi$ radians (or $360^\circ$).

The physical length of that complete loop is one wavelength ($\lambda$). Because the wave geometry is uniform, physical distance maps perfectly to the phase angle. If you look at two points separated by exactly half a wavelength, they are exactly halfway out of sync ($\pi$ radians). If they are separated by a third of a wavelength, they are a third of the cycle out of sync.

#### Step 1: The Phase-Distance Relationship

The formula connecting physical distance ($\Delta x$) to the phase angle difference ($\Delta \phi$) is a direct proportion. The wave number $k = \frac{2\pi}{\lambda}$ acts as our conversion factor:
$$\Delta \phi = k \cdot \Delta x$$
$$\Delta \phi = \left(\frac{2\pi}{\lambda}\right) \Delta x$$

#### Step 2: Calculate the Phase Difference

We are given that the physical distance between the two points is exactly one-third of a wavelength:
$$\Delta x = \frac{\lambda}{3}$$

Substitute this distance into our conversion formula:
$$\Delta \phi = \left(\frac{2\pi}{\lambda}\right) \left(\frac{\lambda}{3}\right)$$

The $\lambda$ variables in the numerator and denominator completely cancel each other out, leaving only the radian phase value:
$$\Delta \phi = \frac{2\pi}{3}$$

_In degrees, this would be $120^\circ$, meaning the second point is exactly one-third of a cycle ahead of or behind the first point._

---

### 3. Final Answer

- **Phase Difference:** $\frac{2\pi}{3} \text{ radians}$
