# Problem 9: Current from Charge

### 1. Problem Statement

Charge flowing through the wire is given by the function of time $Q(t) = 5t^2+5$. What is the current at $t=3\text{ s}$?

---

### 2. Solution and Explanation

**Concept Intuition:**
Current ($I$) is simply the rate at which electric charge ($Q$) moves past a specific point in a wire over time. You can think of charge as the total volume of water that has flowed out of a hose, and current as the *speed* or *rate* the water is actively flowing at any specific second.

Mathematically, a "rate of change" is defined by the **derivative**. Therefore, to find the instantaneous current at any given moment, we take the derivative of the charge function with respect to time.

#### Step 1: Find the Current Function
The definition of current is the time-derivative of charge:
$$I(t) = \frac{dQ(t)}{dt}$$

We are given the charge function:
$$Q(t) = 5t^2 + 5$$

Using the power rule for derivatives ($\frac{d}{dt}(at^n) = n \cdot at^{n-1}$), we find the current function:
$$I(t) = \frac{d}{dt}(5t^2 + 5)$$
$$I(t) = (2 \cdot 5t^{2-1}) + 0$$
$$I(t) = 10t$$

#### Step 2: Evaluate at the Specific Time
Now that we have a formula for the current at any time $t$, we simply plug in the requested time of $t = 3\text{ s}$:
$$I(3) = 10(3)$$
$$I(3) = 30\text{ A}$$

---

### 3. Final Answer

*   **Current at $t=3\text{ s}$:** $30\text{ A}$ (Amperes)
