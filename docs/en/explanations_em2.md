# Problem 1: Gauss's Law

### 1. Solution and Explanation

**Physical Meaning:**
* **Concept:** Gauss's Law dictates that the total electric flux leaving any completely closed 3D surface is determined *only* by the total amount of charge trapped inside.
* **Result:** The provided radius of $1 \text{ m}$ is a deliberate distractor. Whether the sphere's radius is $1 \text{ m}$ or $100 \text{ m}$, the total flux remains mathematically identical because the enclosed $+2 \text{ C}$ charge has not changed.

**The Calculation:**
* We determine the flux using the core equation: 
$$\Phi_E = \frac{q_{enc}}{\varepsilon_0}$$
*(where the total electric flux $\Phi_E$ is calculated by taking the total enclosed charge $q_{enc}$ and dividing it by the vacuum permittivity constant $\varepsilon_0$).*

* We identify our given variables: the enclosed charge is $2 \text{ C}$, and the standard constant $\varepsilon_0 \approx 8.854 \times 10^{-12} \text{ C}^2 / (\text{N}\cdot\text{m}^2)$.

* We substitute these values directly into the equation: 
$$\Phi_E = \frac{2}{8.854 \times 10^{-12}}$$

* Evaluating the division yields the final result: 
$$\Phi_E \approx 2.259 \times 10^{11} \text{ N}\cdot\text{m}^2 / \text{C}$$

---

### 2. Final Answer

* **Electric Flux ($\Phi_E$):** $\approx 2.259 \times 10^{11} \text{ N}\cdot\text{m}^2 / \text{C}$
* **Key Takeaway:** The physical dimensions of the bounding surface ($1 \text{ m}$ radius) are entirely irrelevant to the total electric flux.


# Problem 2: Ampere's Law

### 1. Solution and Explanation

**Physical Meaning:**
* **Concept:** Magnetic fields are vectors. To find their direction, use the **Right-Hand Grip Rule** (thumb = current direction, curled fingers = field direction). 
* **Result:** Assume two vertical wires. The left wire goes UP, creating a field pointing **INTO the page** at the midpoint. The right wire goes DOWN, *also* creating a field pointing **INTO the page** at the midpoint. Because they point the exact same way, we simply add their magnitudes.

#### Step 1: Identify Variables
* Distance between wires: $d = 0.10 \text{ m}$
* Distance to midpoint: $r_1 = r_2 = 0.05 \text{ m}$
* Currents: $I_1 = I_2 = 5 \text{ A}$
* Vacuum permeability: $\mu_0 = 4\pi \times 10^{-7} \text{ T}\cdot\text{m/A}$

#### Step 2: Calculate Field for Wire 1 ($B_1$)
Apply Ampere's Law for a straight wire:
$$B = \frac{\mu_0 I}{2\pi r}$$
*(where magnetic field $B$ is the vacuum permeability $\mu_0$ multiplied by current $I$, divided by the circular boundary $2\pi r$).*

Substitute the values:
$$B_1 = \frac{(4\pi \times 10^{-7})(5)}{2\pi (0.05)}$$
$$B_1 = \frac{2 \times 10^{-7} \times 5}{0.05}$$
$$B_1 = 2.0 \times 10^{-5} \text{ T}$$

#### Step 3: Calculate Field for Wire 2 ($B_2$)
Wire 2 has identical current ($5 \text{ A}$) and distance ($0.05 \text{ m}$), so the result is mathematically identical:
$$B_2 = 2.0 \times 10^{-5} \text{ T}$$

#### Step 4: Calculate Net Magnetic Field ($B_{net}$)
Both fields point INTO the page. Add them together:
$$B_{net} = B_1 + B_2$$
$$B_{net} = (2.0 \times 10^{-5}) + (2.0 \times 10^{-5})$$
$$B_{net} = 4.0 \times 10^{-5} \text{ T}$$

---

### 2. Final Answer

* **Magnitude:** $4.0 \times 10^{-5} \text{ T}$ (or $40 \, \mu\text{T}$)
* **Direction:** **Directly INTO the page** (assuming left wire is UP and right wire is DOWN).


# Problem 3: Biot-Savart Law

### 1. Solution and Explanation

**Physical Meaning:**
The **Biot-Savart Law** calculates the magnetic field from a single, tiny piece of wire. Because the problem specifies a "small segment" that is perfectly perpendicular to our target, we can skip complex calculus and use the direct approximation formula.

#### Step 1: The Formula and Variables
Apply the Biot-Savart approximation for a small segment:
$$\Delta B = \frac{\mu_0}{4\pi} \frac{I \cdot \Delta l \cdot \sin(\theta)}{r^2}$$
*(where the magnetic field $\Delta B$ is the magnetic constant $\frac{\mu_0}{4\pi}$ multiplied by current $I$, length $\Delta l$, and angle $\sin(\theta)$, divided by distance squared $r^2$).*

**Our Givens:**
* Segment length ($\Delta l$) = $0.1 \text{ m}$
* Current ($I$) = $3 \text{ A}$
* Distance ($r$) = $0.2 \text{ m}$
* Angle ($\theta$) = $90^\circ$ (so $\sin(90^\circ) = 1$)
* Magnetic constant ($\frac{\mu_0}{4\pi}$) = $10^{-7} \text{ T}\cdot\text{m/A}$

#### Step 2: Calculation
Substitute the values directly into the equation:
$$\Delta B = (10^{-7}) \frac{3 \cdot 0.1 \cdot 1}{(0.2)^2}$$
$$\Delta B = (10^{-7}) \frac{0.3}{0.04}$$
$$\Delta B = 7.5 \times 10^{-7} \text{ T}$$

---

### 2. Final Answer
* **Magnetic Field ($\Delta B$):** $7.5 \times 10^{-7} \text{ T}$ (or $0.75 \, \mu\text{T}$)


# Problem 4: Magnetic Torque

### 1. Solution and Explanation

**Physical Meaning:**
Magnetic **torque** twists a current-carrying loop in order to align its normal vector (a line pointing straight out of the loop's face) with the external magnetic field. Because the problem states the field is *parallel* to the surface of the loop, the angle between the field and the loop's normal vector is exactly $90^\circ$, producing the absolute maximum twisting force.

#### Step 1: The Formula and Variables
Apply the magnetic torque formula for a current loop:
$$\tau = N \cdot I \cdot A \cdot B \cdot \sin(\theta)$$
*(where the magnetic torque $\tau$ is calculated by multiplying the number of turns $N$, current $I$, area $A$, magnetic field $B$, and the sine of the angle $\sin(\theta)$).*

**Our Givens:**
* Dimensions = $0.10 \text{ m}$ by $0.05 \text{ m}$
* Area ($A$) = $0.005 \text{ m}^2$
* Current ($I$) = $2 \text{ A}$
* Magnetic Field ($B$) = $0.3 \text{ T}$
* Number of turns ($N$) = $1$
* Angle ($\theta$) = $90^\circ$ (so $\sin(90^\circ) = 1$)

#### Step 2: Calculation
Substitute the values directly into the equation:
$$\tau = 1 \cdot 2 \cdot 0.005 \cdot 0.3 \cdot \sin(90^\circ)$$
$$\tau = (0.01) \cdot 0.3 \cdot 1$$
$$\tau = 0.003 \text{ N}\cdot\text{m}$$

---

### 2. Final Answer
* **Magnitude of Magnetic Torque ($\tau$):** $0.003 \text{ N}\cdot\text{m}$ (or $3.0 \times 10^{-3} \text{ N}\cdot\text{m}$)


# Problem 5: Energy Stored by Charge in a Capacitor

### 1. Solution and Explanation

**Physical Meaning:**
A parallel-plate capacitor stores energy by separating opposite charges. Its **capacitance** depends strictly on its physical geometry (area and gap). The **electric field** between the plates is uniform, acting as a direct gradient of the voltage. Because the plates hold opposite charges, they attract each other; however, the attractive force is calculated using only *half* the total electric field, as a plate cannot mathematically exert a force on itself.

#### Step 1: Identify Variables and Convert Units
* Area ($S$) = $0.02 \text{ m}^2$
* Distance ($d$) = $5 \text{ mm} = 0.005 \text{ m}$
* Voltage ($V$) = $500 \text{ V}$
* Permittivity ($\varepsilon_0$) $\approx 8.854 \times 10^{-12} \text{ F/m}$

#### Step 2: Calculate Capacitance ($C$)
$$C = \frac{\varepsilon_0 \cdot S}{d}$$
*(where capacitance $C$ is the permittivity constant $\varepsilon_0$ multiplied by plate area $S$, divided by the gap distance $d$).*

$$C = \frac{(8.854 \times 10^{-12})(0.02)}{0.005}$$
$$C = 3.54 \times 10^{-11} \text{ F}$$

#### Step 3: Calculate Stored Energy ($U$)
$$U = \frac{1}{2} C V^2$$
*(where stored energy $U$ is half the capacitance $C$ multiplied by the squared voltage $V^2$).*

$$U = 0.5 \cdot (3.54 \times 10^{-11}) \cdot (500)^2$$
$$U = 4.43 \times 10^{-6} \text{ J}$$

#### Step 4: Calculate Electric Field ($E$)
$$E = \frac{V}{d}$$
*(where the uniform electric field $E$ is the voltage $V$ divided by the gap distance $d$).*

$$E = \frac{500}{0.005}$$
$$E = 1.0 \times 10^5 \text{ V/m}$$

#### Step 5: Calculate Attraction Force ($F$)
First, find the total stored charge ($Q = C \cdot V$). Then evaluate the force:
$$F = \frac{1}{2} Q E$$
*(where force $F$ is half the total charge $Q$ multiplied by the total electric field $E$, accounting for the fact that a plate only feels the field generated by the opposite plate).*

$$Q = (3.54 \times 10^{-11}) \cdot 500 = 1.77 \times 10^{-8} \text{ C}$$
$$F = 0.5 \cdot (1.77 \times 10^{-8}) \cdot (1.0 \times 10^5)$$
$$F = 8.85 \times 10^{-4} \text{ N}$$

---

### 2. Final Answers

1. **Capacitance ($C$):** $3.54 \times 10^{-11} \text{ F}$ (or $35.4 \text{ pF}$)
2. **Energy ($U$):** $4.43 \times 10^{-6} \text{ J}$ (or $4.43 \, \mu\text{J}$)
3. **Electric Field ($E$):** $1.0 \times 10^5 \text{ V/m}$
4. **Attraction Force ($F$):** $8.85 \times 10^{-4} \text{ N}$


# Problem 6: EM Wave Analysis

### 1. Solution and Explanation

**Physical Meaning:**
An electromagnetic wave consists of perfectly synchronized electric ($E$) and magnetic ($B$) fields. By comparing a specific wave equation to the standard blueprint $E(x,t) = E_0 \sin(kx \pm \omega t)$, we can instantly extract its physical traits. The $B$ field is inextricably linked to the $E$ field via the speed of light ($c$) and must be strictly orthogonal (perpendicular) to both the $E$ field and the direction of travel.

#### Step 1: Extract Constants and Direction
Compare the given equation $E_y(x,t) = 100 \sin(10^7 x - \omega t)$ to the standard blueprint:
* **Amplitude ($E_0$):** $100 \text{ V/m}$
* **Wavenumber ($k$):** $10^7 \text{ rad/m}$
* **Direction:** The spatial variable $x$ combined with the minus sign indicates propagation strictly in the **$+x$ direction**.

#### Step 2: Calculate Wavelength ($\lambda$)
$$k = \frac{2\pi}{\lambda} \implies \lambda = \frac{2\pi}{k}$$
*(where wavelength $\lambda$ is exactly $2\pi$ divided by the wavenumber $k$).*

$$\lambda = \frac{2\pi}{10^7}$$
$$\lambda = 2\pi \times 10^{-7} \text{ m} \approx 628 \text{ nm}$$

#### Step 3: Calculate Angular Frequency ($\omega$)
$$\omega = c \cdot k$$
*(where the angular frequency $\omega$ is the speed of light $c$ multiplied by the wavenumber $k$).*

$$\omega = (3 \times 10^8) \cdot (10^7)$$
$$\omega = 3 \times 10^{15} \text{ rad/s}$$

#### Step 4: Formulate the Magnetic Field ($B$)
First, find the magnetic amplitude ($B_0$):
$$B_0 = \frac{E_0}{c}$$
*(where the magnetic amplitude $B_0$ is the electric amplitude $E_0$ divided by the constant speed of light $c$).*

$$B_0 = \frac{100}{3 \times 10^8} \approx 3.33 \times 10^{-7} \text{ T}$$

Next, determine the direction using the cross product $\vec{S} \propto \vec{E} \times \vec{B}$:
* Propagation ($\vec{S}$) is $+x$ ($\hat{i}$)
* Electric Field ($\vec{E}$) is $+y$ ($\hat{j}$)
* We need: $\hat{j} \times \vec{B} = \hat{i}$. By the Right-Hand Rule, the magnetic field must oscillate in the **$+z$ direction** ($\hat{k}$).

Combine the amplitude, identical phase, and $z$-direction:
$$B_z(x,t) = 3.33 \times 10^{-7} \sin(10^7 x - 3 \times 10^{15} t) \text{ T}$$

---

### 2. Final Answers

* **Direction of Propagation:** The $+x$ direction
* **Wavelength ($\lambda$):** $2\pi \times 10^{-7} \text{ m}$ (or $\approx 628 \text{ nm}$)
* **Angular Frequency ($\omega$):** $3 \times 10^{15} \text{ rad/s}$
* **Magnetic Field Equation:** $B_z(x,t) = 3.33 \times 10^{-7} \sin(10^7 x - 3 \times 10^{15} t) \text{ T}$


# Problem 7: Wavelength and Frequency

### 1. Solution and Explanation

**Physical Meaning:**
Because all light travels at a constant speed in a vacuum ($c$), wavelength and frequency are strictly inversely proportional: as one goes up, the other must go down. The human eye evolved to be most sensitive to the exact middle of the visible spectrum ($550 \text{ nm}$), which corresponds to bright yellow-green light.

#### Step 1: Identify the Color
* The visible spectrum spans roughly $400 \text{ nm}$ (violet) to $700 \text{ nm}$ (red).
* $550 \text{ nm}$ falls squarely in the middle, corresponding to **Yellow-Green**.

#### Step 2: Extract Variables and Formula
Convert nanometers to standard SI meters before calculating.
* Wavelength ($\lambda$) = $550 \text{ nm} = 550 \times 10^{-9} \text{ m}$
* Speed of light ($c$) = $3.0 \times 10^8 \text{ m/s}$

Rearrange the wave equation ($c = \lambda \cdot f$) to solve for frequency:
$$f = \frac{c}{\lambda}$$
*(where the frequency $f$ is exactly the constant speed of light $c$ divided by the wavelength $\lambda$).*

#### Step 3: Calculate Frequency ($f$)
Substitute the values directly into the equation:
$$f = \frac{3.0 \times 10^8}{550 \times 10^{-9}}$$
$$f \approx 0.00545 \times 10^{17}$$
$$f = 5.45 \times 10^{14} \text{ Hz}$$

---

### 2. Final Answers

* **Color:** Yellow-Green
* **Frequency ($f$):** $5.45 \times 10^{14} \text{ Hz}$ (or $545 \text{ THz}$)


# Problem 8: EM Spectrum

### 1. Solution and Explanation

**Physical Meaning:**
* **Concept:** All electromagnetic waves travel at the constant speed of light ($c$), but they carry different levels of energy. 
* **Result:** Wavelength ($\lambda$) is strictly inversely proportional to energy. High-energy waves (like Gamma rays) have the shortest wavelengths, while low-energy waves (like Radio waves) have the longest.

#### Step 1: The Wavelength-Energy Link
We visualize the relationship using the fundamental wave equation:
$$c = \lambda \cdot f$$
*(where the constant speed of light $c$ is the product of the wavelength $\lambda$ and the frequency $f$).*

* **High Energy/Frequency** = Short Wavelength (e.g., Gamma rays).
* **Low Energy/Frequency** = Long Wavelength (e.g., Radio waves).

#### Step 2: Ordering the Categories (Shortest to Longest)
1. **Gamma rays:** Most energetic; wavelengths are smaller than an atom.
2. **X-rays:** High energy; wavelengths are roughly the size of an atom.
3. **Ultraviolet:** Higher energy than visible light; causes sunburns.
4. **Infrared:** Lower energy than visible light; felt as heat.
5. **Microwaves:** Low energy; used for cooking and wireless signals.
6. **Radio waves:** Lowest energy; wavelengths can be longer than a football field.

---

### 2. Final Answer

In order of **increasing wavelength** (shortest to longest):

1. **Gamma rays**
2. **X-rays**
3. **Ultraviolet**
4. **Infrared**
5. **Microwaves**
6. **Radio waves**


# Problem 9: Refraction (Snell's Law)

### 1. Solution and Explanation

**Physical Meaning:**
* **Concept:** Refraction occurs because light changes speed when passing between different materials. This speed change causes the ray to bend at the boundary.
* **Result:** When light enters a denser medium like glass ($n=1.50$) from air ($n=1.00$), it slows down. Because it slows, the path must bend **toward the normal line** (the line perpendicular to the surface). This means our resulting angle must be smaller than $30^\circ$.

#### Step 1: Identify Known Variables
* Index of refraction (Air): $n_1 = 1.00$
* Index of refraction (Glass): $n_2 = 1.50$
* Angle of incidence: $\theta_1 = 30^\circ$

#### Step 2: Snell's Law Formula
To find the exact bend, we use the governing equation for refraction:
$$n_1 \cdot \sin(\theta_1) = n_2 \cdot \sin(\theta_2)$$
*(where the index of refraction $n_1$ multiplied by the sine of the incident angle $\theta_1$ is exactly equal to index $n_2$ multiplied by the sine of the refractive angle $\theta_2$).*

#### Step 3: Calculation
Substitute the variables and isolate the unknown angle:
$$1.00 \cdot \sin(30^\circ) = 1.50 \cdot \sin(\theta_2)$$
$$0.5 = 1.50 \cdot \sin(\theta_2)$$
$$\sin(\theta_2) = \frac{0.5}{1.50} = \frac{1}{3}$$
$$\theta_2 = \arcsin(0.3333) \approx 19.47^\circ$$

---

### 2. Final Answer

* **Angle of Refraction ($\theta_2$):** $\approx 19.47^\circ$
* **Key Takeaway:** The angle decreased from $30^\circ$ to $\approx 19.5^\circ$, confirming the light bent toward the normal as it entered the denser glass.

# Problem 10: Speed of Light in Media

### 1. Solution and Explanation

**Physical Meaning:**
* **Concept:** While the speed of light ($c$) is a universal constant in a vacuum, it slows down significantly when passing through physical matter. 
* **Result:** The **Index of Refraction ($n$)** is a ratio that tells you exactly how much a material resists the flow of light. A high index like diamond’s ($2.42$) means the light is being "braked" heavily, traveling at less than half its maximum speed. This extreme slowing is what causes the intense bending of light that gives diamonds their sparkle.

#### Step 1: Identify Variables
* Speed of light in a vacuum: $c \approx 3.0 \times 10^8 \text{ m/s}$
* Index of refraction (Diamond): $n = 2.42$

#### Step 2: The Formula
To find the velocity within the material, we rearrange the standard refractive index definition:
$$v = \frac{c}{n}$$
*(where the speed of light in the medium $v$ is calculated by taking the vacuum speed of light $c$ and dividing it by the index of refraction $n$).*

#### Step 3: Calculation
Substitute the known values into the equation:
$$v = \frac{3.0 \times 10^8 \text{ m/s}}{2.42}$$
$$v \approx 1.23966 \times 10^8 \text{ m/s}$$
$$v \approx 1.24 \times 10^8 \text{ m/s}$$

---

### 2. Final Answer

* **Speed of light in diamond ($v$):** $\approx 1.24 \times 10^8 \text{ m/s}$
* **Comparison:** This is roughly $41\%$ of the speed of light in a vacuum, illustrating how optically dense a diamond truly is.