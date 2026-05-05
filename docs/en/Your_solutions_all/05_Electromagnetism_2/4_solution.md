# Problem 4: Magnetic Torque

### 1. Problem Statement

A rectangular loop of wire with dimensions $10 \text{ cm}$ by $5 \text{ cm}$ carries a current of $2 \text{ A}$. A uniform magnetic field of $B = 0.3 \text{ T}$ is applied parallel to the plane of the loop. What is the magnitude of the magnetic torque on the loop?

---

### 2. Solution and Explanation

**Concept Intuition:**
When a current-carrying loop is placed in a magnetic field, it experiences a twisting force called **torque** ($\tau$). This torque acts to align the loop's magnetic dipole moment (which points straight out perpendicular to the face of the loop) with the external magnetic field.

The formula for the magnitude of magnetic torque is:
$$\tau = N \cdot I \cdot A \cdot B \cdot \sin(\theta)$$

Let's break down the most critical part of this problem: the angle $\theta$. 
$\theta$ is defined as the angle between the magnetic field vector ($\vec{B}$) and the **normal vector** (a line pointing $90^\circ$ straight out of the surface of the loop). 
The problem states the magnetic field is applied *parallel to the plane of the loop*. Because the field lies flat along the plane of the loop, it must be exactly perpendicular ($90^\circ$) to the normal vector sticking out of the loop.
Therefore, $\theta = 90^\circ$. Since $\sin(90^\circ) = 1$, the torque is at its absolute maximum.

#### Step 1: Identify Known Variables and Convert Units
As always, we convert centimeters to meters to ensure our final unit is in standard Newton-meters ($\text{N}\cdot\text{m}$).
- Dimensions: $0.10 \text{ m}$ by $0.05 \text{ m}$
- Area ($A$): $0.10 \text{ m} \times 0.05 \text{ m} = 0.005 \text{ m}^2$
- Current ($I$): $2 \text{ A}$
- Magnetic Field ($B$): $0.3 \text{ T}$
- Number of turns ($N$): $1$ (since it just says "a loop")
- Angle ($\theta$): $90^\circ$

#### Step 2: Set Up the Equation
$$\tau = I \cdot A \cdot B \cdot \sin(\theta)$$

#### Step 3: Calculation
Substitute the identified values into the equation:
$$\tau = (2 \text{ A}) \cdot (0.005 \text{ m}^2) \cdot (0.3 \text{ T}) \cdot \sin(90^\circ)$$

Since $\sin(90^\circ) = 1$:
$$\tau = 2 \cdot 0.005 \cdot 0.3 \cdot 1$$

First, multiply the current by the area (this calculates the magnetic dipole moment, $\mu = 0.01 \text{ A}\cdot\text{m}^2$):
$$\tau = (0.01) \cdot (0.3)$$
$$\tau = 0.003 \text{ N}\cdot\text{m}$$

---

### 3. Final Answer

- **Magnitude of Magnetic Torque ($\tau$):** $0.003 \text{ N}\cdot\text{m}$ (or $3.0 \times 10^{-3} \text{ N}\cdot\text{m}$)
