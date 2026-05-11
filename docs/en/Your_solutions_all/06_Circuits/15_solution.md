# Problem 15: The Resistor Cube

### 1. Problem Statement

A cube is constructed from 12 identical resistors on its edges, each with resistance $R$. What is the equivalent resistance between two opposite corners of the cube?

---

### 2. Solution and Explanation

**Concept Intuition:**
This is one of the most famous classic physics problems! Attempting to solve this using standard series and parallel formulas or Kirchhoff's loop equations will result in a massive, tangled mess of math. 

Instead, the elegant way to solve it is by using **Symmetry**. Because a cube is perfectly symmetrical, we can easily track how the current splits at each junction from the entrance corner to the exit corner.

#### Step 1: Track the Current Splitting
Imagine a total current $I$ enters the cube at one corner (let's call it Corner A) and exits at the diametrically opposite corner (Corner B). We will trace the path of the current along the edges.

1.  **Leaving Corner A:**
    When the total current $I$ enters Corner A, it has exactly 3 identical edges it can travel down. Because the cube is perfectly symmetric, the current splits evenly into 3 equal parts.
    *   Current on each of the 3 starting edges: **$\frac{I}{3}$**

2.  **The Middle Edges:**
    Follow one of those $\frac{I}{3}$ currents to the next corner. At this new corner, the current cannot go backward, and it has 2 symmetric forward paths that lead toward the exit. So, it splits evenly in half again.
    *   Current on each of the 6 middle edges: $\frac{I/3}{2} =$ **$\frac{I}{6}$**

3.  **Entering Corner B:**
    Now look at the 3 corners immediately adjacent to the final exit (Corner B). At each of these 3 corners, two of those $\frac{I}{6}$ middle currents converge. They combine to form a larger current that travels down the final edge into the exit.
    *   Current on each of the 3 final edges: $\frac{I}{6} + \frac{I}{6} =$ **$\frac{I}{3}$**
    *(Self-check: The three $\frac{I}{3}$ currents meet at the final exit Corner B, combining perfectly back into the total current $I$.)*

#### Step 2: Calculate the Total Voltage Drop
Now we can find the total equivalent resistance by finding the total voltage drop ($V_{total}$) across the cube. To do this, we just apply Ohm's Law ($V = I \cdot R$) along *any single path* from Corner A to Corner B. 

Every possible path from Corner A to Corner B consists of exactly 3 edges: a starting edge, a middle edge, and a final edge.

*   Voltage drop on the 1st edge: $V_1 = \left(\frac{I}{3}\right) \cdot R$
*   Voltage drop on the 2nd edge: $V_2 = \left(\frac{I}{6}\right) \cdot R$
*   Voltage drop on the 3rd edge: $V_3 = \left(\frac{I}{3}\right) \cdot R$

Sum them up to get the total voltage drop across the entire cube:
$$V_{total} = V_1 + V_2 + V_3$$
$$V_{total} = \frac{IR}{3} + \frac{IR}{6} + \frac{IR}{3}$$

To add the fractions, find a common denominator (which is 6):
$$V_{total} = \frac{2IR}{6} + \frac{1IR}{6} + \frac{2IR}{6}$$
$$V_{total} = \frac{5IR}{6}$$

#### Step 3: Find Equivalent Resistance
By definition, the equivalent resistance ($R_{eq}$) of the entire cube is the total voltage drop divided by the total current:
$$R_{eq} = \frac{V_{total}}{I}$$
$$R_{eq} = \frac{\frac{5}{6} I \cdot R}{I}$$
$$R_{eq} = \frac{5}{6} R$$

---

### 3. Final Answer

*   **Equivalent Resistance:** $\frac{5}{6} R$
