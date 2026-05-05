# Problem 6: EM Wave Analysis

### 1. Problem Statement

An electromagnetic wave has its electric field component described by $E_y(x,t) = 100 \sin(10^7 x - \omega t) \text{ V/m}$. What is the direction of propagation? What is the wavelength $\lambda$? What is the angular frequency $\omega$? What is the equation for the magnetic field component?

---

### 2. Solution and Explanation

**Concept Intuition:**
The equation for a traveling wave takes the general standard form:
$$E(x,t) = E_0 \sin(kx \pm \omega t)$$

By simply lining up our given equation beneath the standard blueprint, we can immediately extract the vital parameters of the wave without doing any complex math:
$$E_y(x,t) = 100 \sin(10^7 x - \omega t)$$

- **Amplitude ($E_0$):** $100 \text{ V/m}$
- **Wavenumber ($k$):** $10^7 \text{ rad/m}$

Let's address the specific questions one by one.

#### Part 1: Direction of Propagation
To determine which way the wave is moving, we look at the variables inside the sine function: $(10^7 x - \omega t)$.
1. The spatial variable is $x$, which tells us the wave travels along the **x-axis**.
2. There is a **minus sign** between the spatial term ($x$) and the temporal term ($t$). In wave physics, a minus sign indicates propagation in the positive direction, while a plus sign indicates the negative direction.
Therefore, the wave propagates in the **$+x$ direction**.

#### Part 2: Wavelength ($\lambda$)
The wavenumber $k$ is related to the physical wavelength $\lambda$ by the formula:
$$k = \frac{2\pi}{\lambda}$$

We rearrange to solve for $\lambda$:
$$\lambda = \frac{2\pi}{k}$$
$$\lambda = \frac{2\pi}{10^7 \text{ m}^{-1}}$$
$$\lambda = 2\pi \times 10^{-7} \text{ m} \approx 6.28 \times 10^{-7} \text{ m}$$

*(Note: $628 \text{ nm}$ falls squarely in the visible light spectrum, corresponding to red/orange light!)*

#### Part 3: Angular Frequency ($\omega$)
For electromagnetic waves traveling through a vacuum, the wave always travels at the speed of light ($c = 3 \times 10^8 \text{ m/s}$). The relationship between angular frequency, wavenumber, and wave speed is:
$$\omega = c \cdot k$$

$$\omega = (3 \times 10^8 \text{ m/s}) \cdot (10^7 \text{ rad/m})$$
$$\omega = 3 \times 10^{15} \text{ rad/s}$$

#### Part 4: Equation for the Magnetic Field Component
An electromagnetic wave consists of an electric field ($\vec{E}$) and a magnetic field ($\vec{B}$) traveling perfectly in sync. To write the equation for $\vec{B}$, we need its amplitude, phase, and direction.

**1. Magnitude ($B_0$):**
The magnitudes of the $\vec{E}$ and $\vec{B}$ fields are permanently linked by the speed of light:
$$B_0 = \frac{E_0}{c}$$
$$B_0 = \frac{100}{3 \times 10^8} \approx 3.33 \times 10^{-7} \text{ T}$$

**2. Phase:**
The magnetic field oscillates perfectly in phase with the electric field, so the sine term is completely identical:
$$\sin(10^7 x - 3 \times 10^{15} t)$$

**3. Direction:**
Electromagnetic waves are transverse. The direction of propagation ($\vec{S}$) is given by the cross product of the fields: $\vec{S} \propto \vec{E} \times \vec{B}$.
- We know propagation is in the **$+x$** direction ($\hat{i}$).
- The equation was given as $E_y$, meaning the electric field oscillates in the **$+y$** direction ($\hat{j}$).
- Setting up the cross product: $\hat{j} \times (\text{direction of } \vec{B}) = \hat{i}$
According to the Right-Hand Rule (or vector math $\hat{j} \times \hat{k} = \hat{i}$), the magnetic field must oscillate in the **$+z$** direction ($\hat{k}$).

Putting it all together gives us $B_z(x,t)$.

---

### 3. Final Answers

1. **Direction of Propagation:** The $+x$ direction.
2. **Wavelength ($\lambda$):** $2\pi \times 10^{-7} \text{ m}$ (or $\approx 628 \text{ nm}$)
3. **Angular frequency ($\omega$):** $3 \times 10^{15} \text{ rad/s}$
4. **Magnetic field equation:** $B_z(x,t) = 3.33 \times 10^{-7} \sin(10^7 x - 3 \times 10^{15} t) \text{ T}$
