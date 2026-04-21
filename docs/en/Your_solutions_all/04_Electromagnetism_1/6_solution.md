# Problem 6: Field at a point from a system of charges

### 1. Problem Statement

Two point charges are given:
* $+q\  \text{at point}\  (-a, 0)$
* $+2q\  \text{at point}\  (a, 0)$

1. Determine the field vector $\vec E(0, y)$, $\vec E(x, 0)$ and generally $\vec E(x, y)$.
2. Determine the condition for which the components $E_x = 0$, $E_y = 0$ and the zero field $\vec E = 0$.
3. Calculate the field for: $a = 0.2\,\mathrm{m}$, $y = 0.3\,\mathrm{m}$, $q = 2\,\mu\mathrm{C}$.
4. Investigate the limit $y \gg a$.

---

### 2. Solution and Explanation

**Concept Intuition:**
Instead of simple one-dimensional lines, we're now unleashing vectors in the 2D plane! The electric field at any specific point is the perfect vector sum of the electric field from the first charge and the electric field from the second charge (Superposition Principle). 

If you zoom incredibly far away from these charges (the limit $y \gg a$), the two individual charges should visually blur together into one massive super-charge. The total charge is $+q + (+2q) = +3q$. Let's see if the hardcore vector calculus mathematically proves this extremely cool visual intuition later in Part 4!

#### Part 1: Establishing the Vectors

We need the position vectors pointing from each charge directly towards our test point $P(x, y)$.
- From Charge 1 ($q$) at $(-a, 0)$ to point $(x,y)$: 
  Distance vector: $\vec{R}_1 = (x - (-a))\hat{i} + (y - 0)\hat{j} = (x + a)\hat{i} + y\hat{j}$
  Distance magnitude: $R_1 = \sqrt{(x + a)^2 + y^2}$
  
- From Charge 2 ($2q$) at $(a, 0)$ to point $(x,y)$:
  Distance vector: $\vec{R}_2 = (x - a)\hat{i} + y\hat{j}$
  Distance magnitude: $R_2 = \sqrt{(x - a)^2 + y^2}$

The general electric field formula using vectors is: $\vec{E} = k \frac{q}{R^3} \vec{R}$.
Let's add both fields straight together to get the completely general $\vec E(x, y)$:
$$\vec E(x, y) = kq \frac{(x+a)\hat{i} + y\hat{j}}{((x+a)^2 + y^2)^{3/2}} + 2kq \frac{(x-a)\hat{i} + y\hat{j}}{((x-a)^2 + y^2)^{3/2}}$$

Now, let's plug in specifics for the axes:
**For the y-axis $(0, y)$, plug in $x = 0$:**
Both denominators powerfully simplify to exactly $(a^2 + y^2)^{3/2}$. We just add the numerators!
$$\vec E(0, y) = \frac{kq}{(a^2 + y^2)^{3/2}} [ (a\hat{i} + y\hat{j}) + (-2a\hat{i} + 2y\hat{j}) ]$$
$$\vec E(0, y) = \frac{kq}{(a^2 + y^2)^{3/2}} ( -a\hat{i} + 3y\hat{j} )$$

**For the x-axis $(x, 0)$, plug in $y = 0$:**
The $\hat{j}$ components are gone. Because of the absolute values naturally hiding inside the square roots when $y=0$, $R^3 = |R|^3$:
$$\vec E(x, 0) = kq \left( \frac{\text{sgn}(x+a)}{(x+a)^2} + \frac{2 \cdot \text{sgn}(x-a)}{(x-a)^2} \right) \hat{i}$$
*(Where $\text{sgn}$ represents whether the charge is pushing left or right).*

#### Part 2: Conditions for Zero Field

**Condition for $E_y = 0$:**
By looking at the general $j$-component of $\vec E(x, y)$:
$$E_y = kq y \left( \frac{1}{R_1^3} + \frac{2}{R_2^3} \right)$$
Since radii are always purely positive, the massive bracket is completely positive. Therefore, $E_y$ is ONLY zero when $y = 0$ (everywhere precisely on the physical x-axis).

**Condition for $E_x = 0$:**
Setting the $i$-component to zero:
$$\frac{x+a}{R_1^3} + \frac{2(x-a)}{R_2^3} = 0$$

**Condition for completely Zero Field ($\vec E = 0$):**
We require BOTH $E_y = 0$ and $E_x = 0$. Since $E_y = 0 \implies y=0$, we examine the line directly between the charges $(-a < x < a)$. We equate the magnitudes pushing against each other exactly like Problem 3!
$$\frac{kq}{(x+a)^2} = \frac{2kq}{(a-x)^2}$$
Taking the square root gracefully simplifies the equation:
$$\frac{1}{x+a} = \frac{\sqrt{2}}{a-x}$$
$$a - x = x\sqrt{2} + a\sqrt{2}$$
$$x(1 + \sqrt{2}) = a(1 - \sqrt{2})$$
$$x = a \frac{1 - \sqrt{2}}{1 + \sqrt{2}} \approx -0.171 a$$
This proves the zero-field equilibrium point rests closely to the weaker $+q$ charge!

#### Part 3: Numerical Calculation

Given values: $a = 0.2\text{ m}$, $y = 0.3\text{ m}$, $q = 2 \times 10^{-6}\text{ C}$. 
Because $y$ is given but not $x$, we evaluate $\vec E(0, 0.3)$.
$$y^2 + a^2 = 0.3^2 + 0.2^2 = 0.09 + 0.04 = 0.13 \text{ m}^2$$
$$(y^2 + a^2)^{3/2} = (0.13)^{1.5} \approx 0.04687$$
$$kq = (8.99 \times 10^9) \times (2 \times 10^{-6}) = 17980$$
$$\text{Multiplier} = \frac{17980}{0.04687} \approx 383,614$$

Plug it into the beautifully derived equation from Part 1 $( -a\hat{i} + 3y\hat{j} )$:
$$-a\hat{i} = -0.2\hat{i} \implies E_x = 383614 \times (-0.2) = -76,723 \text{ N/C}$$
$$3y\hat{j} = 3(0.3)\hat{j} = 0.9\hat{j} \implies E_y = 383614 \times (0.9) = 345,253 \text{ N/C}$$
$$\vec E \approx (-7.67 \times 10^4 \hat{i} + 3.45 \times 10^5 \hat{j}) \text{ V/m}$$

#### Part 4: The Incredible Limit $y \gg a$

Let's explore what happens when we observe from incredibly far away ($y$ is gigantically bigger than $a$).
Because $y \gg a$, $(a^2 + y^2) \approx y^2$. Therefore, $(y^2+a^2)^{3/2} \approx y^3$.
Substituting this approximation securely into our $\vec E(0, y)$ formula:
$$\vec E(0, y) \approx \frac{kq}{y^3} (-a\hat{i} + 3y\hat{j})$$

Because $y$ is incredibly larger than $a$, the $3y\hat{j}$ safely dwarfs the tiny $-a\hat{i}$ horizontal push.
$$\vec E(0, y) \approx \frac{kq}{y^3} (3y\hat{j})$$
$$\vec E(0, y) \approx k \frac{3q}{y^2} \hat{j}$$

**Conclusion:** Look closely at this final formula! $k \frac{3q}{r^2}$ is precisely the formula for the electric field of an isolated point charge containing exactly $+3q$. This profoundly proves our intuition! When you zoom out ridiculously far away, the two separate $+q$ and $+2q$ charges beautifully blend into a single massive point charge of $+3q$.

---

### 3. Final Summary

1. **Analytical forms:** 
   - $\vec E(0, y) = \frac{kq}{(a^2 + y^2)^{3/2}} ( -a\hat{i} + 3y\hat{j} )$
   - $\vec E(x,0) = kq \left( \frac{\text{sgn}(x+a)}{(x+a)^2} + \frac{2\text{sgn}(x-a)}{(x-a)^2} \right) \hat{i}$
2. **Zero conditions:** 
   - $E_y = 0$ exactly on the x-axis ($y = 0$).
   - $\vec E = 0$ perfectly at point $(a \frac{1 - \sqrt{2}}{1 + \sqrt{2}}, 0) \approx (-0.171a, 0)$.
3. **Number values:**
   - $\vec E(0, 0.3) \approx -7.67 \times 10^4 \hat{i} + 3.45 \times 10^5 \hat{j} \text{ V/m}$
4. **The Limit ($y \gg a$):**
   - $\vec E \approx k \frac{3q}{y^2} \hat{j}$, brilliantly proving it acts like a macroscopic single $3q$ charge when viewed from extremely far away.
