# Problem 14: The RLC Circuit and Harmonic Oscillator

### 1. Problem Statement

Write down the differential equation for a series RLC circuit with a voltage source $V$, a resistor $R$, an inductor $L$, and a capacitor $C$. Assume the current is $I(t)$ and the voltage across the capacitor is $V_C(t)$. Compare this to the equation of a damped harmonic oscillator. What are the analogies between the terms in the two equations?

---

### 2. Solution and Explanation

**Concept Intuition:**
One of the most beautiful connections in all of physics is the exact mathematical equivalence between a mechanical spring-mass system and an electrical RLC circuit. Because they are governed by the exact same differential equation, we can understand the "sloshing" of electrical charge back and forth in a circuit by visualizing a mass bouncing on a spring!

#### Step 1: The Circuit Differential Equation
Using Kirchhoff's Voltage Law (KVL) around a series loop, the sum of voltage drops across the components must equal the supplied voltage:
$$V_L(t) + V_R(t) + V_C(t) = V(t)$$

We can express each voltage drop using the component definitions:
*   **Inductor:** $V_L = L \frac{dI}{dt}$
*   **Resistor:** $V_R = I \cdot R$

Substituting these into the KVL equation gives us our first form:
$$L \frac{dI}{dt} + R \cdot I(t) + V_C(t) = V(t)$$

To see the classic second-order differential equation, we write everything in terms of the electrical charge, $Q(t)$. 
We know that current is the rate of charge flow ($I = \frac{dQ}{dt}$), which means $\frac{dI}{dt} = \frac{d^2Q}{dt^2}$. 
We also know the voltage across a capacitor is $V_C = \frac{Q}{C}$. 
Substituting these gives the standard differential equation:
$$L \frac{d^2Q}{dt^2} + R \frac{dQ}{dt} + \frac{1}{C} Q = V(t)$$

#### Step 2: The Mechanical Damped Harmonic Oscillator
Now, recall Newton's Second Law for a mass $m$ attached to a spring (with spring constant $k$) sliding on a surface with friction (damping coefficient $b$), being pushed by an external force $F(t)$:
$$\Sigma F = m \cdot a$$
$$F_{external} - F_{friction} - F_{spring} = m \cdot a$$
$$F(t) - b \cdot v - k \cdot x = m \cdot a$$

Writing velocity as $\frac{dx}{dt}$ and acceleration as $\frac{d^2x}{dt^2}$, we rearrange to get the standard mechanical differential equation:
$$m \frac{d^2x}{dt^2} + b \frac{dx}{dt} + k \cdot x = F(t)$$

#### Step 3: The Analogies
By lining up the two equations side-by-side, the physical analogies become immediately apparent:

$$L \frac{d^2Q}{dt^2} + R \frac{dQ}{dt} + \frac{1}{C} Q = V(t)$$
$$m \frac{d^2x}{dt^2} + b \frac{dx}{dt} + k \cdot x = F(t)$$

*   **Inductance ($L$) $\leftrightarrow$ Mass ($m$):** Both represent *inertia*. Mass resists changes in velocity, while an inductor resists changes in current.
*   **Resistance ($R$) $\leftrightarrow$ Damping/Friction ($b$):** Both represent *energy loss*. Friction turns kinetic energy into heat; a resistor turns electrical energy into heat.
*   **Inverse Capacitance ($1/C$) $\leftrightarrow$ Spring Constant ($k$):** Both provide a *restoring force*. A stiff spring ($large\ k$) wants to violently push the mass back to zero. A small capacitor ($large\ 1/C$) quickly builds up a large reverse voltage, wanting to violently push the charge back.
*   **Charge ($Q$) $\leftrightarrow$ Position ($x$):** The fundamental variables oscillating back and forth.
*   **Current ($I$) $\leftrightarrow$ Velocity ($v$):** The rate at which the fundamental variable is moving.
*   **Voltage Source ($V(t)$) $\leftrightarrow$ External Force ($F(t)$):** The outside driving influence pushing the system.

---

### 3. Final Summary

**Electrical DE:** 
$$L \frac{d^2Q}{dt^2} + R \frac{dQ}{dt} + \frac{1}{C} Q = V(t)$$

**Mechanical DE:** 
$$m \frac{d^2x}{dt^2} + b \frac{dx}{dt} + kx = F(t)$$

| Electrical Term | Mechanical Analogy | Conceptual Role |
| :--- | :--- | :--- |
| Charge ($Q$) | Position ($x$) | The oscillating quantity |
| Current ($I = dQ/dt$) | Velocity ($v = dx/dt$) | Rate of movement |
| Inductance ($L$) | Mass ($m$) | Inertia (resists change) |
| Resistance ($R$) | Damping/Friction ($b$) | Energy dissipation |
| Capacitance ($1/C$) | Spring Stiffness ($k$) | Restoring push-back |
| Voltage Source ($V$) | External Force ($F$) | Driving influence |
