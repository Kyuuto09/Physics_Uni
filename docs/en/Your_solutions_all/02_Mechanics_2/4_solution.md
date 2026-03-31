# Problem 4: Energy & Momentum

### 1. Problem Statement

A 0.5 kg block slides down a frictionless track from a height of 3.0 m. At the bottom, it collides and sticks to a 1.5 kg block, which is initially at rest. What is the speed of the combined mass just after the collision?

---

### 2. Solution and Explanation

**Concept Intuition:**
This is a classic two-part physics problem. You have to treat the slide and the crash as two completely separate events with different rules.

1.  **The Slide (Conservation of Energy):** As the first block falls, it perfectly converts its Gravitational Potential Energy into Kinetic Energy (speed).
2.  **The Crash (Conservation of Momentum):** When things crash and stick together, it is called a _perfectly inelastic collision_. During this crash, some energy is lost to sound and heat, so we can no longer use energy equations. However, **momentum is always conserved** in a collision, so we use the momentum formula ($p = mv$) to find the final speed.

#### Step 1: Find the speed of the first block at the bottom of the track

We use the Law of Conservation of Energy to find out how fast the 0.5 kg block is moving right before it hits the second block.
$$PE_{top} = KE_{bottom}$$
$$m_1gh = \frac{1}{2}m_1v_1^2$$

Since the mass of the first block ($m_1$) is on both sides, we can divide it out. The speed at the bottom only depends on the height!
$$gh = \frac{1}{2}v_1^2$$

Multiply both sides by 2, and take the square root to isolate $v_1$:
$$v_1 = \sqrt{2gh}$$

Plug in Earth's gravity ($g = 9.81 \text{ m/s}^2$) and the height ($h = 3.0 \text{ m}$):
$$v_1 = \sqrt{2 \cdot 9.81 \cdot 3.0}$$
$$v_1 = \sqrt{58.86}$$
$$v_1 \approx 7.67 \text{ m/s}$$

_The first block is moving at 7.67 m/s right before the crash._

#### Step 2: Find the speed of the combined blocks after the crash

Now we switch to the Law of Conservation of Momentum. The total momentum before the crash must equal the total momentum after the crash.
$$P_{before} = P_{after}$$
$$m_1v_1 + m_2v_2 = (m_1 + m_2)v_{final}$$

We know the second block is initially at rest, so its starting velocity ($v_2$) is 0. This makes its initial momentum zero. Let's plug in the masses and the $v_1$ we just found:
$$(0.5 \text{ kg} \cdot 7.67 \text{ m/s}) + 0 = (0.5 \text{ kg} + 1.5 \text{ kg}) \cdot v_{final}$$
$$3.835 = 2.0 \cdot v_{final}$$

Divide both sides by the total combined mass (2.0 kg) to find the final velocity:
$$v_{final} = \frac{3.835}{2.0}$$
$$v_{final} \approx 1.92 \text{ m/s}$$

---

### 3. Final Answer

- **Speed of the combined mass after collision:** $\approx 1.92 \text{ m/s}$
