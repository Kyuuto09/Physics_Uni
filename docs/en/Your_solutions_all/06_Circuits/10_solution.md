# Problem 10: Average Current of a Lightning Bolt

### 1. Problem Statement

A lightning bolt transfers a charge of $30\text{ Coulombs}$ to the ground in a time of $2\text{ milliseconds}$. What is the average current of the lightning bolt?

---

### 2. Solution and Explanation

**Concept Intuition:**
In the previous problem, we looked at *instantaneous* current using a derivative. Here, we are looking for **average current**, which is much simpler. It's exactly like calculating an average speed on a road trip (total distance divided by total time). For electricity, average current is just the total charge that moved divided by the total time it took to move.

The only trick here is ensuring our units match. To get our answer in standard Amperes (which is exactly defined as $1\text{ Coulomb}$ per $1\text{ Second}$), we must remember to convert milliseconds into seconds before dividing!

#### Step 1: Identify the Variables and Convert Units
*   **Total Charge ($Q$):** $30\text{ C}$
*   **Total Time ($\Delta t$):** $2\text{ ms}$

Convert milliseconds to seconds by multiplying by $10^{-3}$:
$$\Delta t = 2 \times 10^{-3}\text{ s} = 0.002\text{ s}$$

#### Step 2: Calculate the Average Current
The formula for average current ($I_{avg}$) is:
$$I_{avg} = \frac{Q}{\Delta t}$$

Plug in our values:
$$I_{avg} = \frac{30\text{ C}}{0.002\text{ s}}$$
$$I_{avg} = 15,000\text{ A}$$

---

### 3. Final Answer

*   **Average Current:** $15,000\text{ A}$ (or $15\text{ kA}$)
