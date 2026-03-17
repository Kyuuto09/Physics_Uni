# Problem 3: Path Intersection and Minimum Distance

### 1. Problem Statement

Alice is moving along a path $A(t) = (2+t, 8-3t)$ and Bob is moving along a path $B(t) = (2t-1, 2t+2)$. Determine if they will collide. If not, determine the minimum distance between them and when it occurs.

---

### 2. Solution and Explanation

**Concept Intuition:**
For Alice and Bob to physically collide, they must be at the exact same $x$-coordinate AND the exact same $y$-coordinate at the exact same time ($t$). If they miss each other, we can figure out how close they got by calculating the distance between them at any given second, and finding the lowest point (minimum) of that distance.

#### Part A: Do they collide?

To collide, their $x$-coordinates must match at the same time $t$:
$$x_A = x_B \implies 2 + t = 2t - 1$$
Solve for $t$:
$$3 = t$$

If they collide, their $y$-coordinates must also match at exactly $t = 3$. Let's plug $t = 3$ into both $y$-equations:

- Alice's $y$ at $t=3$: $8 - 3(3) = 8 - 9 = -1$
- Bob's $y$ at $t=3$: $2(3) + 2 = 6 + 2 = 8$

Because $-1 \neq 8$, they are at completely different vertical positions at $t=3$. **They do not collide.**

#### Part B: When does the minimum distance occur?

Since they don't collide, we need to find the distance between them. First, we find the horizontal gap and the vertical gap at any time $t$:

- **Horizontal gap ($x$):** $(2t - 1) - (2 + t) = t - 3$
- **Vertical gap ($y$):** $(2t + 2) - (8 - 3t) = 5t - 6$

Using the Pythagorean theorem ($a^2 + b^2 = c^2$), the square of the distance ($d^2$) between them is:
$$d^2 = (t - 3)^2 + (5t - 6)^2$$

Expand the brackets:
$$d^2 = (t^2 - 6t + 9) + (25t^2 - 60t + 36)$$
$$d^2 = 26t^2 - 66t + 45$$

This forms a standard parabola ($at^2 + bt + c$). Just like finding the minimum of any parabola, we use the vertex formula $t = \frac{-b}{2a}$:
$$t = \frac{-(-66)}{2(26)}$$
$$t = \frac{66}{52} = \frac{33}{26} \approx 1.27 \text{ seconds}$$
The minimum distance occurs at exactly $t = 33/26$ seconds.

#### Part C: What is the minimum distance?

We plug this time back into our distance squared ($d^2$) formula:
$$d^2 = 26\left(\frac{33}{26}\right)^2 - 66\left(\frac{33}{26}\right) + 45$$
$$d^2 = \frac{1089}{26} - \frac{2178}{26} + \frac{1170}{26}$$
$$d^2 = \frac{81}{26}$$

To find the actual distance $d$, take the square root:
$$d = \frac{9}{\sqrt{26}} \approx 1.77\text{ units}$$

---

### 3. Final Answers

- **Collision:** No.
- **Time of minimum distance:** $t = \frac{33}{26} \approx 1.27 \text{ seconds}$
- **Minimum distance:** $d = \frac{9}{\sqrt{26}} \approx 1.77 \text{ units}$
