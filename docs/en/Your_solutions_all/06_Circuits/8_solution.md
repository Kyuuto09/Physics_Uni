# Problem 8: AC Voltage Equation

### 1. Problem Statement

The current in an AC circuit is given by $I(t) = 2 \sin(120\pi t)$. If the circuit consists of a single $50\,\Omega$ resistor, what is the equation for the voltage $V(t)$ across it?

---

### 2. Solution and Explanation

**Concept Intuition:**
In an Alternating Current (AC) circuit, voltage and current are constantly swinging back and forth like a sine wave. 

When a circuit contains *only* a pure resistor, the resistor reacts instantly to the push of the electricity. This means the voltage and current are perfectly **in phase**—they peak at the same exact time, and they cross zero at the same exact time. Because there is no phase shift, Ohm's Law ($V = I \cdot R$) applies instantaneously at every single moment in time: $V(t) = I(t) \cdot R$.

#### Step 1: Apply Ohm's Law Instantaneously
We are given the time-dependent equation for the current:
$$I(t) = 2 \sin(120\pi t)$$

And the resistance:
$$R = 50\,\Omega$$

Substitute the current function into Ohm's Law:
$$V(t) = I(t) \cdot R$$
$$V(t) = \left[ 2 \sin(120\pi t) \right] \cdot 50$$

#### Step 2: Multiply the Amplitude
The resistance simply acts as a multiplier on the *amplitude* of the wave (the peak height). The oscillating part of the wave ($\sin(120\pi t)$) remains completely unchanged, preserving the $60\text{ Hz}$ frequency and ensuring there is no phase shift.
$$V(t) = (2 \cdot 50) \sin(120\pi t)$$
$$V(t) = 100 \sin(120\pi t)$$

---

### 3. Final Answer

*   **Equation for Voltage:** $V(t) = 100 \sin(120\pi t)$ (in Volts)
