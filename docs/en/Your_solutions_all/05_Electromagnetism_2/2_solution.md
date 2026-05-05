# Problem 2: Ampere's Law

### 1. Problem Statement

Two long, parallel wires are $10 \text{ cm}$ apart and carry currents of $5 \text{ A}$ in opposite directions. Calculate the magnitude and direction of the magnetic field at a point midway between the wires.

---

### 2. Solution and Explanation

**Concept Intuition:**
When dealing with multiple magnetic fields, it is critical to determine the *direction* of each field before doing any math. Magnetic fields are vectors, meaning they can add together or cancel each other out depending on where they point. 

We determine the direction of the magnetic field around a straight wire using the **Right-Hand Grip Rule**: if you point your right thumb in the direction of the current, your fingers curl in the direction of the circular magnetic field lines.

Let's visualize the setup:
- Assume the two wires are vertical. 
- Wire 1 is on the left, with current flowing **UP**.
- Wire 2 is on the right, with current flowing **DOWN**.
- We are looking at the exact midpoint between them.

**Applying the Right-Hand Rule:**
1. **For Wire 1 (Left wire, current UP):** Your fingers curl such that on the right side of Wire 1 (where the midpoint is), the magnetic field $\vec{B}_1$ points **INTO the page**.
2. **For Wire 2 (Right wire, current DOWN):** Your fingers curl such that on the left side of Wire 2 (where the midpoint is), the magnetic field $\vec{B}_2$ *also* points **INTO the page**.

Because both $\vec{B}_1$ and $\vec{B}_2$ point in the exact same direction at the midpoint, they constructively interfere. We can simply calculate their individual magnitudes and add them together: $B_{net} = B_1 + B_2$.

#### Step 1: Identify Known Variables and Convert Units
It is important to convert all distances to standard SI units (meters) before calculating.
- Distance between wires: $d = 10 \text{ cm} = 0.10 \text{ m}$
- Distance from Wire 1 to midpoint: $r_1 = \frac{d}{2} = 0.05 \text{ m}$
- Distance from Wire 2 to midpoint: $r_2 = \frac{d}{2} = 0.05 \text{ m}$
- Current in Wire 1: $I_1 = 5 \text{ A}$
- Current in Wire 2: $I_2 = 5 \text{ A}$
- Permeability of free space: $\mu_0 = 4\pi \times 10^{-7} \text{ T}\cdot\text{m/A}$

#### Step 2: Calculate the Magnitude of $B_1$
The magnitude of a magnetic field produced by a long, straight wire is derived from Ampere's Law:
$$B = \frac{\mu_0 I}{2\pi r}$$

Substitute the values for Wire 1:
$$B_1 = \frac{(4\pi \times 10^{-7} \text{ T}\cdot\text{m/A})(5 \text{ A})}{2\pi (0.05 \text{ m})}$$

We can simplify $\frac{4\pi}{2\pi}$ to exactly $2$:
$$B_1 = \frac{2 \times 10^{-7} \times 5}{0.05}$$
$$B_1 = \frac{10 \times 10^{-7}}{0.05}$$
$$B_1 = \frac{1.0 \times 10^{-6}}{0.05}$$
$$B_1 = 20 \times 10^{-6} \text{ T} = 2.0 \times 10^{-5} \text{ T}$$

#### Step 3: Calculate the Magnitude of $B_2$
Since Wire 2 has the exact same current ($5 \text{ A}$) and is at the exact same distance ($0.05 \text{ m}$) from the midpoint, the magnitude of its magnetic field is identical:
$$B_2 = 2.0 \times 10^{-5} \text{ T}$$

#### Step 4: Calculate the Total Net Magnetic Field ($B_{net}$)
As determined in our concept intuition, both fields point in the same direction, so we add them:
$$B_{net} = B_1 + B_2$$
$$B_{net} = (2.0 \times 10^{-5} \text{ T}) + (2.0 \times 10^{-5} \text{ T})$$
$$B_{net} = 4.0 \times 10^{-5} \text{ T}$$

*(This can also be written as $40 \, \mu\text{T}$).*

---

### 3. Final Answer

- **Magnitude:** $4.0 \times 10^{-5} \text{ T}$ (or $40 \, \mu\text{T}$)
- **Direction:** Perpendicular to the plane containing the wires. If we assume the wires are vertical and side-by-side (left/right) with the left wire going UP and the right wire going DOWN, the field points **directly INTO the page**.
