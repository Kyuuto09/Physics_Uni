# Problem 4: Force Comparison

### 1. Problem Statement

Calculate the magnitude of the electric force and the gravitational force between an electron and a proton in a hydrogen atom (average distance $r \approx 5.3 \times 10^{-11} \text{ m}$). What is the ratio $F_e/F_g$?

---

### 2. Solution and Explanation

**Concept Intuition:**
This problem fundamentally explores why chemistry and physics on an atomic level ignore gravity entirely! Both gravity and the electric force are inverse-square laws (they both get weaker exactly based on $1/r^2$). 
However, gravity relies on mass, and subatomic particles are incredibly, unfathomably lightweight. On the other hand, the electric force relies on charge, and the electromagnetic force constant is exponentially stronger than the gravitational constant.

By evaluating the ratio $F_e / F_g$, we will clearly see just how hopelessly outmatched gravity is in the subatomic world!

#### Part A: Setting up the Constants

Here are the standard constants we will magically need for both the electron ($e$) and the proton ($p$):
- Charge magnitude: $|q| \approx 1.60 \times 10^{-19} \text{ C}$
- Electron mass ($m_e$): $\approx 9.11 \times 10^{-31} \text{ kg}$
- Proton mass ($m_p$): $\approx 1.67 \times 10^{-27} \text{ kg}$
- Coulomb's Constant ($k$): $\approx 8.99 \times 10^9 \text{ N}\cdot\text{m}^2/\text{C}^2$
- Gravitational Constant ($G$): $\approx 6.67 \times 10^{-11} \text{ N}\cdot\text{m}^2/\text{kg}^2$
- Average distance ($r$): $\approx 5.3 \times 10^{-11} \text{ m}$

#### Part B: The Electric Force ($F_e$)

Using Coulomb's Law:
$$F_e = k \frac{|q_e q_p|}{r^2}$$

Since an electron and a proton have the exact identically sized charge:
$$F_e = (8.99 \times 10^9) \frac{(1.60 \times 10^{-19})^2}{(5.3 \times 10^{-11})^2}$$
$$F_e = (8.99 \times 10^9) \frac{2.56 \times 10^{-38}}{2.809 \times 10^{-21}}$$
$$F_e \approx 8.19 \times 10^{-8} \text{ N}$$

#### Part C: The Gravitational Force ($F_g$)

Using Newton's Law of Universal Gravitation:
$$F_g = G \frac{m_e m_p}{r^2}$$
$$F_g = (6.67 \times 10^{-11}) \frac{(9.11 \times 10^{-31})(1.67 \times 10^{-27})}{(5.3 \times 10^{-11})^2}$$
$$F_g = (6.67 \times 10^{-11}) \frac{1.52 \times 10^{-57}}{2.809 \times 10^{-21}}$$
$$F_g \approx 3.61 \times 10^{-47} \text{ N}$$

#### Part D: The Ratio ($\frac{F_e}{F_g}$)

To truly prove how completely dominated gravity is, we divide the forces:
$$\text{Ratio} = \frac{8.19 \times 10^{-8} \text{ N}}{3.61 \times 10^{-47} \text{ N}}$$
$$\text{Ratio} \approx 2.27 \times 10^{39}$$

**Fun mathematical note:** If you set up the ratio purely algebraically before plugging in numbers, the distance term completely perfectly cancels out entirely!
$$\frac{F_e}{F_g} = \frac{k q^2 / r^2}{G m_e m_p / r^2} = \frac{k q^2}{G m_e m_p}$$
This elegant mathematical cancellation proves that this insane ratio of $\approx 10^{39}$ is completely **independent** of how far apart the particles are! The electric force is ALWAYS this many times stronger than gravity between these two exact particles at any distance.

---

### 3. Final Answers

- **Magnitude of electric force ($F_e$):** $\approx 8.19 \times 10^{-8} \text{ N}$
- **Magnitude of gravitational force ($F_g$):** $\approx 3.61 \times 10^{-47} \text{ N}$
- **Ratio ($F_e/F_g$):** $\approx 2.27 \times 10^{39}$
