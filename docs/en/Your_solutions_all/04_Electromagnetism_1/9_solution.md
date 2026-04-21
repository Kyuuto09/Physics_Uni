# Problem 9: Vector Lorentz Force

### 1. Problem Statement

A proton moves with a velocity $\vec{v} = (2\hat{i} - 4\hat{j} + \hat{k}) \text{ m/s}$ in a region where the magnetic field is $\vec{B} = (\hat{i} + 2\hat{j} - \hat{k}) \text{ T}$. What is the magnitude of the magnetic force this charge experiences?

---

### 2. Solution and Explanation

**Concept Intuition:**
In the previous Lorentz problem, the velocity and magnetic field were completely, cleanly perpendicular. Simple multiplication $F = qvB$ was enough. However, here they are messy 3D vectors! Because the magnetic force only mathematically "cares" about exactly the part of the velocity that is perpendicular to the completely uniform magnetic field, we MUST use the **vector cross product** ($\vec{v} \times \vec{B}$).

The cross product beautifully and automatically filters out any perfectly parallel movement (which makes 0 force) and calculates not only the physical perpendicular force magnitude but also exactly which 3D direction it is pointing!

#### Part A: The Cross Product Setup

For a heavily rigid 3D system, we calculate the vector Lorentz force equation:
$$\vec{F} = q (\vec{v} \times \vec{B})$$
$$\vec{v} = 2\hat{i} - 4\hat{j} + 1\hat{k}$$
$$\vec{B} = 1\hat{i} + 2\hat{j} - 1\hat{k}$$

We flawlessly calculate the mathematical cross product using a standard matrix determinant:
$$\vec{v} \times \vec{B} = \det \begin{vmatrix} 
\hat{i} & \hat{j} & \hat{k} \\ 
2 & -4 & 1 \\ 
1 & 2 & -1 
\end{vmatrix}$$

Expanding carefully by the absolutely exact top row:
$$= \hat{i} \begin{vmatrix} -4 & 1 \\ 2 & -1 \end{vmatrix} - \hat{j} \begin{vmatrix} 2 & 1 \\ 1 & -1 \end{vmatrix} + \hat{k} \begin{vmatrix} 2 & -4 \\ 1 & 2 \end{vmatrix}$$
$$= \hat{i}\left[(-4)(-1) - (1)(2)\right] \quad - \hat{j}\left[(2)(-1) - (1)(1)\right] \quad + \hat{k}\left[(2)(2) - (-4)(1)\right]$$
$$= \hat{i}\left[4 - 2\right] \quad - \hat{j}\left[-2 - 1\right] \quad + \hat{k}\left[4 - (-4)\right]$$
$$= 2\hat{i} \quad - \hat{j}(-3) \quad + \hat{k}(8)$$
$$\vec{v} \times \vec{B} = 2\hat{i} + 3\hat{j} + 8\hat{k}$$

#### Part B: The Full Force Vector

A proton possesses exactly the fundamental positive charge $q \approx 1.6 \times 10^{-19} \text{ C}$.
Therefore, the absolutely precise Force Vector is:
$$\vec{F} = (1.6 \times 10^{-19}) \cdot (2\hat{i} + 3\hat{j} + 8\hat{k}) \text{ N}$$

#### Part C: Calculating the Magnitude

The rigidly clear problem statement requests solely the **magnitude** of this force, which is physically determined rigidly by the 3D Pythagorean theorem $| \vec{F} | = \sqrt{F_x^2 + F_y^2 + F_z^2}$.

Let's calculate the magnitude of the $\vec{v} \times \vec{B}$ vector first to make it cleaner mathematically:
$$|\vec{v} \times \vec{B}| = \sqrt{2^2 + 3^2 + 8^2}$$
$$|\vec{v} \times \vec{B}| = \sqrt{4 + 9 + 64}$$
$$|\vec{v} \times \vec{B}| = \sqrt{77} \approx 8.775$$

Now multiply by the precise proton charge scalar:
$$|\vec{F}| = |q| \cdot |\vec{v} \times \vec{B}|$$
$$|\vec{F}| = (1.6 \times 10^{-19}) \cdot \sqrt{77}$$
$$|\vec{F}| = (1.6 \times 10^{-19}) \cdot (8.775)$$
$$|\vec{F}| = 14.04 \times 10^{-19} \text{ N}$$
$$|\vec{F}| = 1.404 \times 10^{-18} \text{ N}$$

---

### 3. Final Answers

- **Force Vector:** $\vec{F} = (3.2\hat{i} + 4.8\hat{j} + 12.8\hat{k}) \times 10^{-19} \text{ N}$
- **Magnitude of the Force ($|\vec{F}|$):** $\approx 1.404 \times 10^{-18} \text{ N}$ (or exactly $1.6\sqrt{77} \times 10^{-19} \text{ N}$)
