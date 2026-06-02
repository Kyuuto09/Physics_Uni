# Problem 2: Orbital Mechanics

### 1. Problem Statement

Calculate the orbital speed of the International Space Station (ISS), which orbits at an altitude of approximately 400 km above the Earth's surface. (Earth's mass $M_E \approx 5.97 \times 10^{24}\text{ kg}$). Compare this speed to Earth's orbital speed around the Sun (Earth-Sun distance $\approx 150 \times 10^6\text{ km}$, Earth's orbital period $\approx 365.25\text{ days}$). Which is faster, the ISS around the Earth or Earth in its orbit around the Sun?

---

### 2. Solution and Explanation

**Concept Intuition:**
There are two completely different ways to calculate orbital speed depending on the information you have. 
1. If you know the **mass** of the object you are orbiting, you use Newton's law of gravity: $v = \sqrt{\frac{GM}{r}}$.
2. If you know the **time** it takes to complete an orbit (the period), you can just use simple circular motion (distance / time): $v = \frac{2\pi r}{T}$.

We will use the gravity method for the ISS, and the circular motion method for the Earth!

#### Part 1: Orbital Speed of the ISS
To use Newton's equation $v = \sqrt{\frac{GM}{r}}$, we first need to find the *true* orbital radius ($r$). The ISS is 400 km above the surface, but gravity pulls from the *center* of the Earth. 
*   Earth's Radius ($R_E$): $6,378\text{ km}$ (from Problem 1)
*   ISS Altitude ($h$): $400\text{ km}$
*   Total Radius ($r = R_E + h$): $6,378 + 400 = 6,778\text{ km}$

We must convert this to meters for standard physics equations: $r = 6,778,000\text{ m}$.
We also know the Gravitational Constant $G \approx 6.674 \times 10^{-11}\text{ m}^3\text{/(kg}\cdot\text{s}^2)$.

Now, plug it into the orbital velocity formula. 
*(In words: Velocity is equal to the square root of the entire result of: the Gravitational constant multiplied by the Mass of the Earth, divided by the orbital radius).*
$$v_{iss} = \sqrt{\frac{G \cdot M_E}{r}}$$
$$v_{iss} = \sqrt{\frac{(6.674 \times 10^{-11}) \cdot (5.97 \times 10^{24})}{6,778,000}}$$
$$v_{iss} = \sqrt{\frac{3.984 \times 10^{14}}{6.778 \times 10^6}}$$
$$v_{iss} = \sqrt{5.878 \times 10^7}$$
$$v_{iss} \approx 7,667\text{ m/s}$$

To convert to kilometers per second, divide by 1,000:
**$v_{iss} \approx 7.67\text{ km/s}$**

#### Part 2: Orbital Speed of the Earth
We know the Earth completes one massive circle around the Sun in $365.25$ days. Let's use simple circular motion. 
*(In words: Velocity is equal to the total distance traveled—the circumference of the orbit—divided by the total time it takes).*
$$v = \frac{\text{distance}}{\text{time}} = \frac{2\pi r}{T}$$

1.  **Distance (Circumference):**
    The radius is $150 \times 10^6\text{ km}$.
    $$C = 2\pi (150,000,000\text{ km}) \approx 942,477,796\text{ km}$$
2.  **Time (in seconds):**
    Just like the last problem, we use fraction multiplication to convert days to seconds:
    $$365.25\text{ days} \times \frac{24\text{ hours}}{1\text{ day}} \times \frac{60\text{ minutes}}{1\text{ hour}} \times \frac{60\text{ seconds}}{1\text{ minute}} = 31,557,600\text{ seconds}$$
3.  **Speed:**
    $$v_{earth} = \frac{942,477,796\text{ km}}{31,557,600\text{ s}}$$
    **$v_{earth} \approx 29.87\text{ km/s}$**

---

### 3. Final Answer

*   **Speed of ISS:** $\approx 7.67\text{ km/s}$
*   **Speed of Earth:** $\approx 29.87\text{ km/s}$
*   **Comparison:** The **Earth orbiting the Sun is much faster** (nearly 4 times faster) than the ISS orbiting the Earth!
