	# Problem 2: Propagation of Error II (Area of a Rectangle)

### 1. Problem Statement

The length and width of a rectangular plate are measured to be $L = (15.3 \pm 0.1)\text{ cm}$ and $W = (8.4 \pm 0.1)\text{ cm}$. Calculate the area of the plate and its uncertainty.

---

### 2. Solution and Explanation

**Concept Intuition:**
The area of a rectangle is found by multiplying its length by its width ($A = L \cdot W$). Because both the length and the width measurements have some inherent uncertainty, the final calculated area will carry an uncertainty contributed by *both* of these measurements.

For multiplication and division of independent variables, the standard scientific method to find the total uncertainty is to add the **relative uncertainties in quadrature** (meaning we square them, add them, and take the square root). 

#### Step 1: Calculate the Best Estimate for Area
First, calculate the area using the central (best estimate) values for length and width.
$$A = L \cdot W$$
$$A = 15.3\text{ cm} \cdot 8.4\text{ cm}$$
$$A = 128.52\text{ cm}^2$$

#### Step 2: Calculate the Uncertainty in Area ($\Delta A$)
The formula for adding relative uncertainties in quadrature for a product $A = L \cdot W$ is:
$$\frac{\Delta A}{A} = \sqrt{\left(\frac{\Delta L}{L}\right)^2 + \left(\frac{\Delta W}{W}\right)^2}$$

Substitute our known values:
$$\frac{\Delta A}{128.52} = \sqrt{\left(\frac{0.1}{15.3}\right)^2 + \left(\frac{0.1}{8.4}\right)^2}$$

Calculate the fractions:
$$\frac{\Delta A}{128.52} = \sqrt{(0.006536)^2 + (0.011905)^2}$$
$$\frac{\Delta A}{128.52} = \sqrt{0.0000427 + 0.0001417}$$
$$\frac{\Delta A}{128.52} = \sqrt{0.0001844}$$
$$\frac{\Delta A}{128.52} \approx 0.01358$$

Now, multiply both sides by $A$ ($128.52$) to find the absolute uncertainty ($\Delta A$):
$$\Delta A = 128.52 \cdot 0.01358$$
$$\Delta A \approx 1.745\text{ cm}^2$$

*(Note: Some introductory physics courses teach a simpler "worst-case scenario" method where you just add the relative errors linearly without squaring them: $\frac{\Delta A}{A} \approx \frac{\Delta L}{L} + \frac{\Delta W}{W}$. This would give a slightly larger, more conservative error bound of $\Delta A \approx 2.37\text{ cm}^2$. We use the root-sum-square method above because it is statistically correct for independent random measurements.)*

#### Step 3: Rounding the Final Answer
Standard practice dictates rounding the absolute uncertainty to one (or sometimes two) significant figures.
Let's round the uncertainty to one decimal place: $\Delta A \approx 1.7\text{ cm}^2$.
We must then round our best estimate of the area to match that same decimal place (the tenths place):
$A \approx 128.5\text{ cm}^2$.

---

### 3. Final Answer

*   **Calculated Area:** $A = (128.5 \pm 1.7)\text{ cm}^2$
