# Problem 2: Electric Potential

### 1. Problem Statement

Point charges of +1C, -2C, +3C, and -4C are placed at the corners of a square with sides of 1.0 m (in order). Calculate the electric potential at the center of the square.

---

### 2. Solution and Explanation

**Concept Intuition:**
Unlike electric force (which is a vector, meaning direction entirely dictates how forces cancel out), electric potential (voltage) is a **scalar** quantity. It behaves more like temperature or money. If you have four heaters in the corners of a room, the temperature in the center is just the simple sum of the heat from all four. You don't have to worry about arrows or vectors canceling each other out based on geometry; you just add their values up!

Since electric potential equals $V = k \frac{q}{r}$, any positive charge creates a positive potential ("heating up" the space), and any negative charge creates a negative potential ("cooling down" the space).

#### Part A: Distance to the Center

First, we need the precise distance $r$ from any perfectly square corner to the exact center. 
The side length of the square is $a = 1.0 \text{ m}$. 
Using the Pythagorean theorem on the full diagonal ($d$):
$$d = \sqrt{a^2 + a^2} = \sqrt{1^2 + 1^2} = \sqrt{2} \text{ m}$$

The distance to the center $r$ is exactly half of the full diagonal:
$$r = \frac{\sqrt{2}}{2} \approx 0.707 \text{ m}$$
Because it is a perfect square, this distance $r$ is absolutely identical for all four corner charges.

#### Part B: The Principle of Superposition

Now, we calculate the total electric potential $V_{net}$ at the center by simply summing up the individual potentials from all four charges ($V_1, V_2, V_3, V_4$):
$$V_{net} = V_1 + V_2 + V_3 + V_4$$

Using the formula for the potential of a point charge $\left(V = k \frac{q}{r}\right)$:
$$V_{net} = k\frac{q_1}{r} + k\frac{q_2}{r} + k\frac{q_3}{r} + k\frac{q_4}{r}$$

Notice that the constant $k$ and the distance $r$ are exactly the same for every single term. We can easily factor them out to make the math incredibly simple!
$$V_{net} = \frac{k}{r} (q_1 + q_2 + q_3 + q_4)$$

#### Part C: Calculating the Final Value

Now, we just logically plug in our given charge values:
$$q_1 = +1 \text{ C}$$
$$q_2 = -2 \text{ C}$$
$$q_3 = +3 \text{ C}$$
$$q_4 = -4 \text{ C}$$

$$q_{total} = (+1) + (-2) + (+3) + (-4) = -2 \text{ C}$$

Plugging everything back into our factored potential equation (and using Coulomb's constant $k \approx 8.99 \times 10^9 \text{ N}\cdot\text{m}^2/\text{C}^2$):
$$V_{net} = \frac{8.99 \times 10^9}{\frac{\sqrt{2}}{2}} \cdot (-2)$$

Multiplying the denominator flip:
$$V_{net} = (-2 \cdot \sqrt{2}) \cdot 8.99 \times 10^9$$
$$V_{net} \approx -2.828 \cdot 8.99 \times 10^9$$
$$V_{net} \approx -25.43 \times 10^9 \text{ V}$$
$$V_{net} \approx -2.54 \times 10^{10} \text{ V}$$

Because the total sum of the charges is heavily negative overall, the resulting electrical potential in the exact center is also highly negative.

---

### 3. Final Answers

- **Electric Potential at the center ($V_{net}$):** $-2.54 \times 10^{10} \text{ V}$ (or exactly $-2\sqrt{2}k \text{ V}$)
