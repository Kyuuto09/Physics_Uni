# Problem 1: Propagation of Error I (Sphere Volume)

### 1. Problem Statement

The radius of a sphere is measured to be $r = (6.20 \pm 0.05)\text{ cm}$. Calculate the volume of the sphere and its associated uncertainty.

---

### 2. Solution and Explanation

**Concept Intuition:**
When we measure a physical quantity (like radius) with some uncertainty, any value we *calculate* using that measurement (like volume) will also have an uncertainty. Because the volume of a sphere depends on the radius *cubed* ($r^3$), a small error in measuring the radius will be magnified three times over in the final volume calculation!

We will use the standard rule for propagation of relative uncertainty for powers:
If $y = x^n$, then the relative uncertainty is $\frac{\Delta y}{y} = n \frac{\Delta x}{x}$.

#### Step 1: Calculate the Best Estimate for Volume
First, we calculate the volume using our best estimate for the radius ($r = 6.20\text{ cm}$).
The formula for the volume of a sphere is:
$$V = \frac{4}{3} \pi r^3$$

Substitute the value of $r$:
$$V = \frac{4}{3} \pi (6.20\text{ cm})^3$$
$$V = \frac{4}{3} \pi (238.328\text{ cm}^3)$$
$$V \approx 998.31\text{ cm}^3$$

#### Step 2: Calculate the Uncertainty in Volume ($\Delta V$)
Using the relative error rule for a variable raised to a power ($n=3$):
$$\frac{\Delta V}{V} = 3 \cdot \frac{\Delta r}{r}$$

We want to find the absolute uncertainty ($\Delta V$), so we multiply both sides by $V$:
$$\Delta V = V \cdot 3 \cdot \left( \frac{\Delta r}{r} \right)$$

Substitute our known values ($V \approx 998.31$, $r = 6.20$, $\Delta r = 0.05$):
$$\Delta V = 998.31 \cdot 3 \cdot \left( \frac{0.05}{6.20} \right)$$
$$\Delta V = 998.31 \cdot 3 \cdot (0.008064)$$
$$\Delta V \approx 24.15\text{ cm}^3$$

*(Calculus alternative: You can also use the derivative method: $\Delta V = |\frac{dV}{dr}| \Delta r = 4\pi r^2 \Delta r = 4\pi(6.20)^2(0.05) \approx 24.15\text{ cm}^3$. Both methods yield the exact same result!)*

#### Step 3: Rounding the Final Answer
In experimental physics, uncertainties are typically rounded to one (or sometimes two) significant figures, because stating an error out to many decimal places implies a level of precision we don't actually have. 

If we keep two significant figures for the uncertainty: $\Delta V \approx 24\text{ cm}^3$.
We then round our volume to the same decimal place as the uncertainty (the ones place): $V \approx 998\text{ cm}^3$.

---

### 3. Final Answer

*   **Volume:** $V = (998 \pm 24)\text{ cm}^3$
