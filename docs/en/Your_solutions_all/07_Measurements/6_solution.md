# Problem 6: Instrument Precision

### 1. Problem Statement

A digital thermometer reads $25.4^\circ\text{C}$. Assuming the uncertainty is half the value of the last digit, what is the absolute uncertainty of this measurement?

---

### 2. Solution and Explanation

**Concept Intuition:**
Whenever we take a measurement with a digital instrument, there is always a built-in "rounding" uncertainty. Because the digital screen can't show infinite decimal places, the instrument rounds the true physical value to fit the screen.

If the thermometer reads exactly $25.4^\circ\text{C}$, the true temperature could be slightly higher (e.g., $25.44^\circ\text{C}$) or slightly lower (e.g., $25.36^\circ\text{C}$). The standard rule of thumb for digital instruments is that the maximum rounding error—and therefore the absolute uncertainty—is **half the value of the smallest displayed decimal place** (the least significant digit).

#### Step 1: Identify the Value of the Last Digit
Look at the given reading: $25.4^\circ\text{C}$.
The last digit is the "4", which is in the **tenths** place.
Therefore, the value of the smallest possible step this thermometer can display is $0.1^\circ\text{C}$.

#### Step 2: Calculate the Absolute Uncertainty
The problem states that the uncertainty is half the value of this last digit.
$$\text{Absolute Uncertainty} = \frac{0.1^\circ\text{C}}{2}$$
$$\text{Absolute Uncertainty} = 0.05^\circ\text{C}$$

This tells us that the thermometer will read $25.4^\circ\text{C}$ for any true temperature between $25.35^\circ\text{C}$ and $25.45^\circ\text{C}$.

---

### 3. Final Answer

*   **Absolute Uncertainty:** $\pm 0.05^\circ\text{C}$
