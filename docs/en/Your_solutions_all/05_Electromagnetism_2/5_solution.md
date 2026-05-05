# Problem 5: Energy Stored by Charge in a Capacitor

### 1. Problem Statement

We have a parallel-plate capacitor with the following parameters:
* Area of the plates ($S$): $0.02\,\mathrm{m^2}$
* Distance between plates ($d$): $5\,\mathrm{mm}$
* Voltage across plates ($V$): $500\,\mathrm{V}$ *(Note: The problem text uses $U$ for voltage, but standard physics notation uses $V$ for voltage and $U$ for energy. We will use $V=500\,\mathrm{V}$ to prevent confusion with the energy calculation)*

Calculate:
1. The capacitance $C$ of the capacitor.
2. The energy $U$ stored in the capacitor.
3. The electric field intensity $E$ between the plates.
4. The force of attraction $F$ between the plates.

---

### 2. Solution and Explanation

Before beginning, we must convert all given values into standard SI units.
- $S = 0.02 \text{ m}^2$
- $d = 5 \text{ mm} = 0.005 \text{ m}$
- $V = 500 \text{ V}$
- Permittivity of free space ($\varepsilon_0$) $\approx 8.854 \times 10^{-12} \text{ F/m}$

---

#### Part 1: Capacitance ($C$)

**Concept:** The capacitance of a parallel-plate capacitor relies entirely on its physical geometry (area and distance) and the material between them (in this case, air/vacuum, represented by $\varepsilon_0$).

**Formula:** 
$$C = \frac{\varepsilon_0 \cdot S}{d}$$

**Calculation:**
$$C = \frac{(8.854 \times 10^{-12} \text{ F/m}) \cdot (0.02 \text{ m}^2)}{0.005 \text{ m}}$$
$$C = \frac{1.7708 \times 10^{-13}}{0.005}$$
$$C = 3.5416 \times 10^{-11} \text{ F}$$

*(This can also be written as $35.4 \text{ pF}$)*

---

#### Part 2: Energy Stored ($U$)

**Concept:** The energy stored in a capacitor represents the work done by the battery to separate the positive and negative charges onto the two plates.

**Formula:** 
$$U = \frac{1}{2} C V^2$$

**Calculation:**
$$U = \frac{1}{2} \cdot (3.5416 \times 10^{-11} \text{ F}) \cdot (500 \text{ V})^2$$
$$U = \frac{1}{2} \cdot (3.5416 \times 10^{-11}) \cdot (250,000)$$
$$U = 4.427 \times 10^{-6} \text{ J}$$

*(This can also be written as $4.43 \, \mu\text{J}$)*

---

#### Part 3: Electric Field Intensity ($E$)

**Concept:** The electric field between two infinite parallel plates is uniform. It is simply the "slope" of the voltage over the distance.

**Formula:** 
$$E = \frac{V}{d}$$

**Calculation:**
$$E = \frac{500 \text{ V}}{0.005 \text{ m}}$$
$$E = 100,000 \text{ V/m}$$

*(This can also be written as $1.0 \times 10^5 \text{ V/m}$)*

---

#### Part 4: Force of Attraction ($F$)

**Concept:** The two plates have opposite charges ($+Q$ and $-Q$), meaning they attract each other. You might be tempted to use $F = Q \cdot E$, but remember that $E$ is the *total* electric field created by both plates. A plate cannot exert a force on itself. The field created by just one plate is exactly half of the total field ($\frac{E}{2}$). Therefore, the force one plate exerts on the other is $F = Q \cdot (\frac{E}{2})$.

**Formula:**
$$F = \frac{1}{2} Q E$$
*(Note: To find $Q$, we use $Q = C \cdot V$)*

**Calculation:**
First, find the total charge $Q$ on one plate:
$$Q = (3.5416 \times 10^{-11} \text{ F}) \cdot (500 \text{ V}) = 1.7708 \times 10^{-8} \text{ C}$$

Now, find the force:
$$F = \frac{1}{2} \cdot (1.7708 \times 10^{-8} \text{ C}) \cdot (100,000 \text{ V/m})$$
$$F = 0.5 \cdot 0.0017708$$
$$F = 8.854 \times 10^{-4} \text{ N}$$

---

### 3. Final Answers

1. **Capacitance ($C$):** $3.54 \times 10^{-11} \text{ F}$ (or $35.4 \text{ pF}$)
2. **Energy ($U$):** $4.43 \times 10^{-6} \text{ J}$ (or $4.43 \, \mu\text{J}$)
3. **Electric Field ($E$):** $1.0 \times 10^5 \text{ V/m}$
4. **Attraction Force ($F$):** $8.85 \times 10^{-4} \text{ N}$
