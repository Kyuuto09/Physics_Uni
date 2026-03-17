# Problem 8: Circular Motion

### 1. Problem Statement

Calculate the centripetal acceleration of a person standing on the Earth's equator. The Earth's radius is approximately 6378 km.

---

### 2. Solution and Explanation

**Concept Intuition:**
Even though you feel like you are standing perfectly still, the Earth is spinning. Because you are traveling in a massive circle, you are constantly experiencing a tiny inward acceleration keeping you on that circular path. This is called centripetal acceleration.

To find it, we need two things: the radius of the circle, and how fast you are moving along the edge of it.

#### Step 1: Convert to Standard Units

Physics formulas require standard SI units (meters and seconds).

- **Radius ($R$):** $6378 \text{ km} = 6,378,000 \text{ meters}$.
- **Time ($T$):** The Earth makes one full rotation every 24 hours.
  $$T = 24 \text{ hours} \cdot 60 \text{ minutes} \cdot 60 \text{ seconds} = 86,400 \text{ seconds}$$

#### Step 2: Calculate Tangential Velocity ($v$)

Velocity is just distance divided by time. For a circle, the distance is the circumference ($2\pi R$).
$$v = \frac{2\pi R}{T}$$
$$v = \frac{2\pi (6,378,000)}{86,400}$$
$$v \approx \frac{40,074,155.89}{86,400} \approx 463.82 \text{ m/s}$$
_(This means you are currently moving at over 460 meters per second just by sitting in your chair!)_
 
#### Step 3: Calculate Centripetal Acceleration ($a_c$)

The formula for centripetal acceleration is velocity squared divided by the radius:
$$a_c = \frac{v^2}{R}$$
$$a_c = \frac{(463.82)^2}{6,378,000}$$
$$a_c = \frac{215,129}{6,378,000} \approx 0.0337 \text{ m/s}^2$$

---

### 3. Final Answer

The centripetal acceleration of a person on the equator is approximately **$0.0337 \text{ m/s}^2$**.
