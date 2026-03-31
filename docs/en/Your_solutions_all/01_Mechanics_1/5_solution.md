# Problem 5: Relative Velocity

### 1. Problem Statement

A river flows east at $2 \text{ m/s}$. A boat that can travel at $5 \text{ m/s}$ in still water wants to go directly north across the river. In what direction (angle) should it head? How long will it take to cross the river if it's $200$ meters wide?

---

### 2. Solution and Explanation

**The Practical Concept:**
The boat has to use some of its $5 \text{ m/s}$ engine power just to fight the $2 \text{ m/s}$ river. The leftover power is what actually pushes it across. We use a triangle to separate these speeds.

#### Part A: Finding the Angle

We form a right triangle using the speeds:

- The longest diagonal side (the boat's total engine power) is: **$5 \text{ m/s}$**.
- The horizontal side fighting the river is: **$2 \text{ m/s}$**.

To find the angle ($\theta$) the boat needs to aim, we just divide the river's speed by the boat's speed, and use the inverse sine function ($\arcsin$ or $\sin^{-1}$) on a calculator:
$$\sin(\theta) = \frac{2}{5} = 0.4$$
$$\theta = \arcsin(0.4) \approx 23.58^\circ$$
The boat must aim **$23.58^\circ$ West of North** to perfectly cancel out the eastward river.

#### Part B: Finding the Time

Because the boat is fighting the river, it is _not_ crossing the river at its full $5 \text{ m/s}$ speed. We use the Pythagorean theorem ($a^2 + b^2 = c^2$) to find the actual forward speed.

- $a^2$ is the river ($2^2 = 4$)
- $c^2$ is the boat's engine ($5^2 = 25$)
- $b^2$ is our actual straight-forward speed.

$$4 + b^2 = 25$$
$$b^2 = 21$$
$$b = \sqrt{21} \approx 4.58 \text{ m/s}$$

Now, we just divide the total distance by this forward speed:
$$\text{Time} = \frac{200 \text{ meters}}{4.58 \text{ m/s}} \approx 43.6 \text{ seconds}$$

---

### 3. Final Answers

- **Direction:** $23.58^\circ$ West of North.
- **Time to Cross:** $43.6$ seconds.
