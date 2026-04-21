# Problem 3: Electrostatic Equilibrium

### 1. Problem Statement

Find the equilibrium position for a charge $q_3 = +1\text{C}$ placed on the line between a charge $q_1 = +4\text{C}$ and a charge $q_2 = +9\text{C}$, which are separated by a distance of 2 m.

---

### 2. Solution and Explanation

**Concept Intuition:**
"Equilibrium" means the net force acting on the object is completely zero. Because our third charge ($q_3 = +1\text{C}$) is positive, and the two outer charges ($+4\text{C}$ and $+9\text{C}$) are also positive, the outer charges will both try to push our middle charge away.

Imagine being stuck between two people constantly pushing you. The $+9\text{C}$ person is pushing with much more force than the $+4\text{C}$ person. Therefore, to perfectly balance the pushing forces, you need to stand much closer to the weaker $+4\text{C}$ charge and further away from the very strong $+9\text{C}$ charge.

Let's do the math to find exactly where that perfectly balanced sweet spot is!

#### Part A: Setting up the Forces

Let the distance between the $+4\text{C}$ charge and our test charge $+1\text{C}$ be exactly $x$.
Since the entire total distance is 2 meters, the remaining distance to the $+9\text{C}$ charge must logically be $(2 - x)$.

For the object to be in perfectly balanced equilibrium, the repelling force from the first charge ($F_1$) pushing it to the right must absolutely perfectly equal the repelling force from the second charge ($F_2$) pushing it to the left:
$$F_1 = F_2$$

Using Coulomb's force equation for both sides:
$$k \frac{|q_1 q_3|}{x^2} = k \frac{|q_2 q_3|}{(2 - x)^2}$$

#### Part B: Simplifying and Solving

Right away, we notice that the constant $k$ and the test charge $q_3$ are absolutely identical on both sides of our perfectly balanced equation. Therefore, we can completely divide them out! This mathematically proves that *any* test charge would find its balance at this exact same spot.
$$\frac{q_1}{x^2} = \frac{q_2}{(2 - x)^2}$$

Now, plug in our given charge values (ignoring the units for simplicity):
$$\frac{4}{x^2} = \frac{9}{(2 - x)^2}$$

To make solving this extremely easy, we can simply take the square root of both sides! Because physical distances are always positive, we only care about the positive roots:
$$\frac{\sqrt{4}}{\sqrt{x^2}} = \frac{\sqrt{9}}{\sqrt{(2 - x)^2}}$$
$$\frac{2}{x} = \frac{3}{2 - x}$$

Now, cross-multiply to beautifully solve the algebra:
$$2(2 - x) = 3x$$
$$4 - 2x = 3x$$
$$4 = 5x$$

Finally, highly simple division perfectly isolates our $x$:
$$x = \frac{4}{5} = 0.8 \text{ m}$$

---

### 3. Final Answers

- **Equilibrium Position:** $x = 0.8 \text{ m}$ away from the $+4\text{C}$ charge.
- **Alternative perspective:** $(2.0 - 0.8) = 1.2 \text{ m}$ away from the $+9\text{C}$ charge.
