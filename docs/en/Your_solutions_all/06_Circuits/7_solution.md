# Problem 7: Capacitors in Parallel

### 1. Problem Statement

Two capacitors, $C_1=4\,\mu\text{F}$ and $C_2=6\,\mu\text{F}$, are connected in parallel to a $10\text{ V}$ battery. What is the total charge stored on the capacitors? What is the total energy stored?

---

### 2. Solution and Explanation

**Concept Intuition:**
Unlike resistors, which *impede* flow, capacitors *store* charge based on their plate surface area. When you connect capacitors in **parallel**, you are effectively attaching their plates together side-by-side, creating one giant capacitor with a larger total surface area. Therefore, their capacitances simply add up directly!

Because they are in parallel, both capacitors are directly connected to the battery terminals. This means they both experience the exact same voltage ($10\text{ V}$).

#### Step 1: Calculate Equivalent Capacitance
For capacitors in parallel, we simply add their individual capacitances together:
$$C_{eq} = C_1 + C_2$$
$$C_{eq} = 4\,\mu\text{F} + 6\,\mu\text{F} = 10\,\mu\text{F}$$
*(Note: $10\,\mu\text{F} = 10 \times 10^{-6}\text{ F}$)*

#### Step 2: Calculate Total Charge Stored
The fundamental equation for a capacitor relates Charge ($Q$), Capacitance ($C$), and Voltage ($V$):
$$Q = C \cdot V$$

We can use the equivalent capacitance to find the total charge drawn from the battery:
$$Q_{total} = C_{eq} \cdot V$$
$$Q_{total} = (10 \times 10^{-6}\text{ F}) \cdot (10\text{ V})$$
$$Q_{total} = 100 \times 10^{-6}\text{ C} = 100\,\mu\text{C}$$

*(Self-check: $Q_1 = 4\,\mu\text{F} \cdot 10\text{V} = 40\,\mu\text{C}$ and $Q_2 = 6\,\mu\text{F} \cdot 10\text{V} = 60\,\mu\text{C}$. $40 + 60 = 100\,\mu\text{C}$. Matches perfectly!)*

#### Step 3: Calculate Total Energy Stored
The energy ($U$) stored in a capacitor is half the product of its capacitance and the square of the voltage across it:
$$U_{total} = \frac{1}{2} C_{eq} V^2$$
$$U_{total} = \frac{1}{2} (10 \times 10^{-6}\text{ F}) \cdot (10\text{ V})^2$$
$$U_{total} = (5 \times 10^{-6}) \cdot (100)$$
$$U_{total} = 500 \times 10^{-6}\text{ J} = 500\,\mu\text{J}$$

---

### 3. Final Answers

*   **Total Charge Stored ($Q_{total}$):** $100\,\mu\text{C}$
*   **Total Energy Stored ($U_{total}$):** $500\,\mu\text{J}$
