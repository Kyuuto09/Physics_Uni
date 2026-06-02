# Problem 10: Measuring the Height of the Atmosphere

### 1. Problem Statement

A medieval astronomer in Al-Andalus, Al-Zarqali, estimated the height of the Earth’s atmosphere using sunset timing. The interval between sunset and the first appearance of faint stars was $t = 40\text{ minutes}$.

Given:
*   Earth radius $R_E = 6,370\text{ km}$
*   Earth’s rotation rate: $360^\circ$ in 24 hours
*   Sharp-edge atmosphere model: $\cos\phi = \frac{R_E}{R_E+h}$

Find the solar depression angle ($\phi$) and the atmospheric height ($h$).

---

### 2. Solution and Explanation

**Concept Intuition:**
When the sun "sets" below the horizon, it doesn't immediately get pitch black outside. The sky stays lit for a while (twilight) because the sun's rays are still hitting the upper atmosphere high above our heads and bouncing down to us. When it finally gets dark enough to see faint stars, it means the sun has dipped so low that its rays can no longer even graze the very top of the atmosphere. 

By measuring exactly how long twilight lasts, we can calculate what angle the sun moved during that time, and use basic trigonometry to find the height of that "atmospheric ceiling"!

#### Part 1: The Solar Depression Angle ($\phi$)
First, we need to figure out how many degrees the Earth rotates every single minute. We know it does a full $360^\circ$ rotation in 24 hours.

**Degrees per hour:**
$$\frac{360^\circ}{24\text{ hours}} = 15^\circ\text{ per hour}$$

**Degrees per minute:**
$$\frac{15^\circ}{60\text{ minutes}} = 0.25^\circ\text{ per minute}$$

Now we simply multiply that rate by the $40\text{ minutes}$ of twilight.
$$\phi = \text{Rate} \times \text{Time}$$
*(In words: The solar depression angle is equal to the rotation rate of the Earth in degrees per minute multiplied by the twilight time in minutes).*

$$\phi = 0.25^\circ\text{/min} \times 40\text{ minutes}$$
$$\phi = 10^\circ$$

The sun was exactly **$10^\circ$** below the horizon when the first stars appeared.

#### Part 2: The Atmospheric Height ($h$)
We are given the geometric formula for the sharp-edge model:
$$\cos\phi = \frac{R_E}{R_E+h}$$

Let's rearrange this formula to solve for the height ($h$):
1.  Multiply both sides by $(R_E + h)$:
    $$(R_E + h) \cdot \cos\phi = R_E$$
2.  Divide both sides by $\cos\phi$:
    $$R_E + h = \frac{R_E}{\cos\phi}$$
3.  Subtract $R_E$ from both sides:
    $$h = \frac{R_E}{\cos\phi} - R_E$$

*(In words: The atmospheric height is equal to the Earth's radius divided by the cosine of the depression angle, minus the Earth's radius).*

Let's plug in our known values ($R_E = 6,370\text{ km}$ and $\phi = 10^\circ$):
$$h = \frac{6,370}{\cos(10^\circ)} - 6,370$$
$$h = \frac{6,370}{0.9848} - 6,370$$
$$h \approx 6,468.3 - 6,370$$
$$h \approx 98.3\text{ km}$$

*(Nerd Note: Today, modern science defines the edge of space at the Kármán line, which sits at exactly 100 km above sea level. This medieval method, despite being nearly a thousand years old, was stunningly accurate!)*

---

### 3. Final Answer

1.  **Solar Depression Angle:** $\phi = 10^\circ$
2.  **Atmospheric Height:** $h \approx 98.3\text{ km}$
