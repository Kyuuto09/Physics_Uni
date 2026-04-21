# Problem 1: Coulomb's Law

### 1. Problem Statement

Four point charges of +1.0 C each are placed at the corners of a square with sides of 1.0 m. Calculate the magnitude and direction of the electric force on a charge of -2.0 C placed at the center of the square.

---

### 2. Solution and Explanation

**Concept Intuition:**
Coulomb's Law states that electric charges exert forces on each other. Since the charge in the center is negative (-2.0 C) and the charges on the corners are all positive (+1.0 C), they will attract each other. 

However, because this is a perfectly symmetrical square with identical charges on all corners, all four corners are pulling the center charge with exactly the same amount of force. 

Imagine four incredibly strong, equally matched people pulling you from four perfectly opposite corners of a square room using ropes. You wouldn't move anywhere! The pull from the top-left completely cancels out the pull from the bottom-right, and the pull from the top-right completely cancels out the pull from the bottom-left.

#### Part A: Mathematical Symmetry

By symmetry, the distance from the center of a square to any of its corners is exactly the same. We can call this distance $r$. 
Using Coulomb's force equation, the magnitude of the force from any single corner charge $q_c$ on the center charge $q_0$ is:
$$F = k \frac{|q_c q_0|}{r^2}$$

Since $q_c = +1.0 \text{ C}$ for all four corners and the distance $r$ is identical for all four corners, the absolute magnitude of the force from each corner is precisely the same.

Let's pair up the opposite diagonal corners:
- Let $\vec{F}_{TL}$ be the attractive force pulling towards the top-left corner.
- Let $\vec{F}_{BR}$ be the attractive force pulling towards the bottom-right corner.

Because these two corners lie perfectly opposite each other on a straight diagonal line passing through the center, their force vectors point in exact opposite directions:
$$\vec{F}_{TL} = -\vec{F}_{BR}$$
$$\vec{F}_{TL} + \vec{F}_{BR} = 0$$

The exact same cancellation happens with the other two opposite corners (top-right and bottom-left):
$$\vec{F}_{TR} + \vec{F}_{BL} = 0$$

#### Part B: Finding the Net Force

To find the total electric force on the center charge, we sum up all the individual force vectors (Superposition Principle):
$$\vec{F}_{net} = \vec{F}_{TL} + \vec{F}_{BR} + \vec{F}_{TR} + \vec{F}_{BL}$$
$$\vec{F}_{net} = (\vec{F}_{TL} + \vec{F}_{BR}) + (\vec{F}_{TR} + \vec{F}_{BL})$$
$$\vec{F}_{net} = 0 + 0 = 0 \text{ N}$$

---

### 3. Final Answers

- **Magnitude of force:** $0 \text{ N}$
- **Direction:** None (Undefined, as there is zero net force).
