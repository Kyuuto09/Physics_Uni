# Problem 1: Rotational Velocity

### 1. Problem Statement

Calculate the linear speed (in km/s) of a point on the Earth's equator due to its rotation. Earth's radius $R \approx 6378\text{ km}$.

---

### 2. Solution and Explanation

**Concept Intuition:**
Even when you are sitting perfectly still on a chair, you are actually hurtling through space because the Earth is spinning! To find out exactly how fast you are moving if you live on the equator, we just need to figure out how far you travel in a single day. 

Linear speed ($v$) for circular motion is just the distance traveled (the circumference of the circle) divided by the time it takes to travel that distance (the period of rotation).

#### Step 1: Calculate the Circumference (Distance)
A point on the equator travels exactly one full circle around the Earth's axis every day. The distance of this circle is the Earth's equatorial circumference.
$$C = 2\pi R$$
$$C = 2\pi (6378\text{ km})$$
$$C \approx 40,074\text{ km}$$

#### Step 2: Determine the Time (Period)
The Earth completes one rotation relative to the Sun every 24 hours. Because we want our final answer in kilometers per **second** (km/s), we need to convert those 24 hours into seconds.

We do this using a method called dimensional analysis, where we multiply by fractions that allow the old units to cancel out (top and bottom):
1.  **Hours to Minutes:** There are 60 minutes in 1 hour.
    $$24\text{ hours} \times \frac{60\text{ minutes}}{1\text{ hour}} = 1,440\text{ minutes}$$
2.  **Minutes to Seconds:** There are 60 seconds in 1 minute.
    $$1,440\text{ minutes} \times \frac{60\text{ seconds}}{1\text{ minute}} = 86,400\text{ seconds}$$

So, the total time for one rotation is $T = 86,400\text{ seconds}$.

*(Nerd Note: If you want to be incredibly precise, the Earth actually rotates a full $360^\circ$ relative to the background stars in 23 hours, 56 minutes, and 4 seconds—known as a sidereal day! But for most standard physics problems, the 24-hour solar day is the expected benchmark.)*

#### Step 3: Calculate the Linear Speed
Divide the total distance by the total time:
$$v = \frac{C}{T}$$
$$v = \frac{40,074\text{ km}}{86,400\text{ s}}$$
$$v \approx 0.4638\text{ km/s}$$

If we convert this to meters per second, it is $\approx 464\text{ m/s}$, which is faster than the speed of sound!

---

### 3. Final Answer

*   **Linear Speed at the Equator:** $v \approx 0.46\text{ km/s}$
