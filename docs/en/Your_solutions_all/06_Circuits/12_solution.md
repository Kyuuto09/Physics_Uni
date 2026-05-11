# Problem 12: Transformer Currents

### 1. Problem Statement

A transformer has a primary coil with 1000 turns and a secondary coil with 200 turns. If the primary voltage is $120\text{ V}$ (AC), what is the secondary voltage? If the current in the secondary is $3\text{ A}$, what is the current in the primary?

---

### 2. Solution and Explanation

**Concept Intuition:**
A transformer uses magnetic fields to transfer AC power from one coil of wire to another without them ever physically touching. 
*   **Voltage:** The voltage scales perfectly proportionally to the number of wire loops (turns). If the secondary coil has fewer loops than the primary coil, it will "step down" the voltage.
*   **Current:** A transformer cannot magically create free energy. To obey the law of conservation of energy, the total Power ($P = I \cdot V$) must remain perfectly balanced on both sides. Therefore, if a transformer steps *down* the voltage, it must step *up* the current by that exact same ratio to keep the power equal!

#### Step 1: Calculate the Secondary Voltage
The transformer equation relates voltages to the number of turns ($N$):
$$\frac{V_s}{V_p} = \frac{N_s}{N_p}$$

We can rearrange this to solve for the secondary voltage ($V_s$):
$$V_s = V_p \cdot \left( \frac{N_s}{N_p} \right)$$
$$V_s = 120\text{ V} \cdot \left( \frac{200}{1000} \right)$$
$$V_s = 120 \cdot 0.2$$
$$V_s = 24\text{ V}$$
*(The voltage successfully stepped down because there were fewer turns!)*

#### Step 2: Calculate the Primary Current
Because power is conserved in an ideal transformer, the power entering the primary coil must equal the power leaving the secondary coil:
$$P_{primary} = P_{secondary}$$
$$V_p \cdot I_p = V_s \cdot I_s$$

We can rearrange this to solve for the primary current ($I_p$):
$$I_p = I_s \cdot \left( \frac{V_s}{V_p} \right)$$

Notice that $\frac{V_s}{V_p}$ is just the turns ratio ($\frac{200}{1000} = 0.2$) we already found!
$$I_p = 3\text{ A} \cdot \left( \frac{24\text{ V}}{120\text{ V}} \right)$$
$$I_p = 3 \cdot 0.2$$
$$I_p = 0.6\text{ A}$$

*(Alternatively: The secondary side is drawing $P = 24\text{V} \cdot 3\text{A} = 72\text{W}$ of power. To supply $72\text{W}$ from a $120\text{V}$ source on the primary side, you need $I = P/V = 72/120 = 0.6\text{ A}$.)*

---

### 3. Final Answers

*   **Secondary Voltage:** $24\text{ V}$
*   **Primary Current:** $0.6\text{ A}$
