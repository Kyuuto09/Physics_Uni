# Problem 5: Escape Velocity

### 1. Problem Statement

What is the escape velocity from the surface of the Moon? (Moon's mass $M_M \approx 7.35 \times 10^{22}\text{ kg}$; whereas Moon's radius $R_M \approx 1,737\text{ km}$). Express the result in km/s and as a fraction of Earth's escape velocity (Earth's escape velocity $\approx 11.2\text{ km/s}$).

---

### 2. Solution and Explanation

**Concept Intuition:**
Escape velocity is the exact speed you need to travel to completely escape a planet's gravity forever without needing to use your engines anymore. If you jump off the ground at this speed, gravity will continuously slow you down, but it will never be strong enough to pull you back down to the surface!

#### Step 1: Calculate the Escape Velocity of the Moon
The formula for escape velocity comes from setting kinetic energy equal to gravitational potential energy. 
$$v_{esc} = \sqrt{\frac{2 \cdot G \cdot M_M}{R_M}}$$

*(In words: The escape velocity is equal to the square root of the entire result of: 2 multiplied by the Gravitational constant multiplied by the Mass of the celestial body, all divided by the radius of that celestial body).*

First, let's list our known values (and convert the Moon's radius to meters!):
*   $G = 6.674 \times 10^{-11}\text{ m}^3\text{/(kg}\cdot\text{s}^2)$
*   $M_M = 7.35 \times 10^{22}\text{ kg}$
*   $R_M = 1,737,000\text{ m}$

Now, plug them into the equation:
$$v_{esc} = \sqrt{\frac{2 \cdot (6.674 \times 10^{-11}) \cdot (7.35 \times 10^{22})}{1,737,000}}$$
$$v_{esc} = \sqrt{\frac{9.811 \times 10^{12}}{1.737 \times 10^6}}$$
$$v_{esc} = \sqrt{5,648,244}$$
$$v_{esc} \approx 2,376\text{ m/s}$$

To convert this to kilometers per second, we divide by 1,000:
**$v_{esc} \approx 2.38\text{ km/s}$**

#### Step 2: Compare to Earth
The problem asks us to express this as a fraction of Earth's escape velocity ($11.2\text{ km/s}$).
$$\text{Fraction} = \frac{v_{\text{moon}}}{v_{\text{earth}}}$$
$$\text{Fraction} = \frac{2.38\text{ km/s}}{11.2\text{ km/s}}$$
$$\text{Fraction} \approx 0.21$$

This means it takes roughly **21%** (or about **$\frac{1}{5}$th**) of the speed to escape the Moon as it does to escape the Earth. This is exactly why the Apollo lunar modules were able to blast off the Moon's surface using relatively small ascent engines, rather than needing the massive Saturn V rockets they used to leave Earth!

---

### 3. Final Answer

*   **Moon's Escape Velocity:** $\approx 2.38\text{ km/s}$
*   **Fraction of Earth's:** $\approx 0.21$ (or roughly $\frac{1}{5}$th the speed required to escape Earth)
