# Problem 4: Geostationary Orbit

### 1. Problem Statement

Satellites in geostationary orbit remain above the same point on Earth. What must their orbital period be? Calculate the altitude of a geostationary orbit above the Earth's surface.

---

### 2. Solution and Explanation

**Concept Intuition:**
A geostationary satellite is basically a satellite that plays "follow the leader" perfectly with a specific spot on the Earth's equator. As the Earth spins, the satellite orbits at the exact same angular speed, making it appear to hover motionless in the sky. This is incredibly useful for things like satellite TV or weather monitoring!

#### Step 1: Determine the Orbital Period
In order to hover over the same spot, the satellite must complete one full orbit in the exact same amount of time it takes the Earth to complete one full rotation. 
Therefore, the **orbital period ($T$) is 24 hours**.

*(Just like we calculated in previous problems, $24\text{ hours} \times 60 \times 60 = 86,400\text{ seconds}$.)*

#### Step 2: Set Up the Equations
To find the altitude, we first need to find the total distance from the *center* of the Earth to the satellite (the orbital radius, $r$). We do this by combining Newton's law of gravity with the formula for circular motion, which simplifies down to Kepler's Third Law. 

The formula for the orbital radius is:
$$r^3 = \frac{G \cdot M_E \cdot T^2}{4\pi^2}$$
*(In words: The orbital radius cubed is equal to the top half—which is the Gravitational constant multiplied by the Mass of the Earth multiplied by the Period squared—all divided by the bottom half, which is $4 \pi^2$.)*

#### Step 3: Calculate the Total Orbital Radius ($r$)
Let's plug in our known values (using the same $G$ and $M_E$ from previous problems):
*   $G = 6.674 \times 10^{-11}\text{ m}^3\text{/(kg}\cdot\text{s}^2)$
*   $M_E = 5.97 \times 10^{24}\text{ kg}$
*   $T = 86,400\text{ s}$

First, square the time: 
$T^2 = 86,400 \times 86,400 = 7,464,960,000\text{ s}^2$.

Now plug it all in:
$$r^3 = \frac{(6.674 \times 10^{-11}) \cdot (5.97 \times 10^{24}) \cdot (7,464,960,000)}{4 \cdot \pi^2}$$
$$r^3 = \frac{2.974 \times 10^{24}}{39.478}$$
$$r^3 \approx 7.533 \times 10^{22}\text{ m}^3$$

To find $r$, we take the **cube root** of both sides:
$$r = \sqrt[3]{7.533 \times 10^{22}}$$
$$r \approx 42,230,000\text{ meters}$$
Convert to kilometers by dividing by 1,000:
$$r \approx 42,230\text{ km}$$

#### Step 4: Calculate the Altitude ($h$)
The radius $r$ we just calculated is the distance from the satellite to the *center* of the Earth. To find the altitude (the height above the *surface*), we must subtract the Earth's radius ($R_E = 6,378\text{ km}$).

$$\text{Altitude } (h) = r - R_E$$
$$h = 42,230\text{ km} - 6,378\text{ km}$$
$$h = 35,852\text{ km}$$

*(Nerd Note: If you use the highly precise sidereal day of 23 hours 56 minutes instead of 24 hours, the math comes out to exactly $\approx 35,786\text{ km}$, which is the true engineering altitude used by NASA!)*

---

### 3. Final Answer

*   **Orbital Period:** $24\text{ hours}$ (or $86,400\text{ seconds}$)
*   **Altitude:** $h \approx 35,852\text{ km}$
