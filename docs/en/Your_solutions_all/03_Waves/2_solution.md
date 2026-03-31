# Problem 2: String Harmonics

### 1. Problem Statement

A guitar string is $64\text{ cm}$ long and has a fundamental frequency (one antinode) of $330\text{ Hz}$. What is the speed of the wave on this string?

---

### 2. Solution and Explanation

**Concept Intuition:**
Think of a vibrating guitar string like a fixed-size data buffer. Because the string is clamped down at both ends (the bridge and the nut), any wave on it must have zero amplitude at the ends.

When a string vibrates at its "fundamental frequency" (the lowest possible note), it forms exactly one "antinode" (one big bulge in the middle). Mathematically, this single bulge represents exactly _half_ of a full sine wave. Therefore, the physical length of one complete wave data cycle (the wavelength) is exactly twice the length of the string. Once we know the wavelength and the "clock speed" (frequency), finding the transmission speed is just basic multiplication.

#### Step 1: Convert to Standard Units

Physics formulas strictly expect SI units (meters).
$$L = 64\text{ cm} = 0.64\text{ meters}$$

#### Step 2: Determine the Wavelength ($\lambda$)

For a string vibrating at its fundamental frequency, the length of the string ($L$) holds exactly half of a wavelength ($\frac{\lambda}{2}$).
$$L = \frac{\lambda}{2}$$

To find the full wavelength, we multiply the string's length by 2:
$$\lambda = 2L$$
$$\lambda = 2 \cdot 0.64$$
$$\lambda = 1.28\text{ meters}$$

_The physical size of one full wave is $1.28\text{ meters}$._

#### Step 3: Calculate the Wave Speed ($v$)

Now we use the fundamental wave equation, which states that speed is frequency multiplied by wavelength:
$$v = f \cdot \lambda$$

Plug in our given frequency ($330\text{ Hz}$) and our calculated wavelength ($1.28\text{ m}$):
$$v = 330 \cdot 1.28$$
$$v = 422.4\text{ m/s}$$

_The physical vibration is traveling back and forth across the guitar string at over $422\text{ meters per second}$._

---

### 3. Final Answer

- **Wave Speed:** $422.4\text{ m/s}$
