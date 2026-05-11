# Problem 11: Power & Energy

### 1. Problem Statement

What is the power dissipated by a $100\,\Omega$ resistor when a voltage of $50\text{ V}$ is applied across it? How much energy is consumed in 5 minutes?

---

### 2. Solution and Explanation

**Concept Intuition:**
*   **Power** is the *rate* at which electricity is used. In a resistor, electrical energy is "dissipated" (converted into heat) due to friction-like resistance. We can find this rate using the voltage and the resistance.
*   **Energy** is the *total amount* of electricity used over a period of time. Just like driving at a constant speed ($60\text{ mph}$) for a specific time ($2\text{ hours}$) tells you the total distance ($120\text{ miles}$), drawing a constant power over a specific time tells you the total energy consumed. We just need to make sure our time is in standard seconds to get standard Joules!

#### Step 1: Calculate the Power Dissipated
There are a few ways to calculate power ($P = I \cdot V$ or $P = I^2 \cdot R$), but since we are given Voltage ($V$) and Resistance ($R$), the most direct formula is:
$$P = \frac{V^2}{R}$$

Substitute the given values ($V = 50\text{ V}$ and $R = 100\,\Omega$):
$$P = \frac{(50)^2}{100}$$
$$P = \frac{2500}{100}$$
$$P = 25\text{ W}$$
The resistor dissipates $25\text{ Watts}$ of power. (This means it converts $25\text{ Joules}$ of electrical energy into heat every single second).

#### Step 2: Calculate the Total Energy Consumed
Energy ($E$) is simply Power multiplied by Time. First, we must convert the given time from minutes into standard seconds.
$$t = 5\text{ minutes} \times 60\frac{\text{seconds}}{\text{minute}} = 300\text{ seconds}$$

Now, multiply the power by the time:
$$E = P \cdot t$$
$$E = 25\text{ W} \cdot 300\text{ s}$$
$$E = 7,500\text{ J}$$

---

### 3. Final Answers

*   **Power Dissipated:** $25\text{ W}$ (Watts)
*   **Energy Consumed:** $7,500\text{ J}$ (Joules)
