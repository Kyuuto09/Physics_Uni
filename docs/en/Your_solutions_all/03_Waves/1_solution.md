# Problem 1: Wave Properties

### 1. Problem Statement

A sound wave in air has a frequency of $440\text{ Hz}$. If the speed of sound in air is $343\text{ m/s}$, what is its wavelength? What is its wavelength in water, where the speed of sound is $1482\text{ m/s}$?

---

### 2. Solution and Explanation

**Concept Intuition:**
Think of a wave like a data stream crossing a network.

- **Frequency ($f$):** This is the "clock rate" or refresh rate of the signal ($440$ ticks per second). It is hardcoded by the original source (the speaker) and _never changes_, even when the signal moves from one medium (air) to another (water).
- **Speed ($v$):** This is the physical transmission speed of the medium. Water is much denser and stiffer than air, so the mechanical sound data travels through it much faster.
- **Wavelength ($\lambda$):** This is the physical footprint of one full cycle of data. Because the signal travels much faster in water but "ticks" at the exact same rate, the physical space between each tick gets stretched out significantly.

#### Step 1: The Fundamental Wave Equation

The relationship between speed, frequency, and wavelength is defined by the fundamental wave equation:
$$v = f \cdot \lambda$$

To find the wavelength, we just rearrange the formula by dividing both sides by the frequency:
$$\lambda = \frac{v}{f}$$

#### Step 2: Calculate Wavelength in Air

We plug in the speed of sound in air ($343\text{ m/s}$) and the constant frequency ($440\text{ Hz}$):
$$\lambda_{air} = \frac{343}{440}$$
$$\lambda_{air} \approx 0.78\text{ meters}$$

_In air, the physical distance between the peaks of the sound wave is about $78\text{ cm}$._

#### Step 3: Calculate Wavelength in Water

Now we plug in the much faster speed of sound in water ($1482\text{ m/s}$), keeping the frequency exactly the same:
$$\lambda_{water} = \frac{1482}{440}$$
$$\lambda_{water} \approx 3.37\text{ meters}$$

_Because the sound is moving more than four times faster through the water, the wave gets stretched out to nearly $3.4\text{ meters}$ long._

---

### 3. Final Answers

- **Wavelength in Air:** $\approx 0.78\text{ m}$
- **Wavelength in Water:** $\approx 3.37\text{ m}$
