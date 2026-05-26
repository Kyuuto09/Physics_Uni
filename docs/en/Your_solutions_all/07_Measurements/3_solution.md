# Problem 3: Propagation of Error III (Ohm's Law)

### 1. Problem Statement

The resistance $R$ is calculated using Ohm's Law, $R = V/I$. If the voltage is measured as $V = (10.0 \pm 0.2)\text{ V}$ and the current as $I = (2.00 \pm 0.05)\text{ A}$, what is the calculated resistance and its uncertainty?

---

### 2. Solution and Explanation

**Concept Intuition:**
This problem involves calculating a value using division ($R = V/I$). In error propagation, multiplication and division follow the exact same mathematical rule: the total uncertainty is determined by adding the *relative uncertainties* (the percentage errors) of the components. 

Because the measurements of voltage and current are independent of each other, we will again use the standard scientific method of adding their relative uncertainties in **quadrature**.

#### Step 1: Calculate the Best Estimate for Resistance
First, we calculate the expected resistance using the central values for voltage and current.
$$R = \frac{V}{I}$$
$$R = \frac{10.0\text{ V}}{2.00\text{ A}}$$
$$R = 5.00\,\Omega$$

#### Step 2: Calculate the Uncertainty in Resistance ($\Delta R$)
The formula for adding relative uncertainties in quadrature for a quotient ($R = V/I$) is identical to the one used for a product:
$$\frac{\Delta R}{R} = \sqrt{\left(\frac{\Delta V}{V}\right)^2 + \left(\frac{\Delta I}{I}\right)^2}$$

Substitute our known values:
$$\frac{\Delta R}{5.00} = \sqrt{\left(\frac{0.2}{10.0}\right)^2 + \left(\frac{0.05}{2.00}\right)^2}$$

Calculate the fractions:
$$\frac{\Delta R}{5.00} = \sqrt{(0.02)^2 + (0.025)^2}$$
$$\frac{\Delta R}{5.00} = \sqrt{0.0004 + 0.000625}$$
$$\frac{\Delta R}{5.00} = \sqrt{0.001025}$$
$$\frac{\Delta R}{5.00} \approx 0.03202$$

Now, multiply both sides by $R$ ($5.00$) to find the absolute uncertainty ($\Delta R$):
$$\Delta R = 5.00 \cdot 0.03202$$
$$\Delta R \approx 0.1601\,\Omega$$

#### Step 3: Rounding the Final Answer
We round our absolute uncertainty to an appropriate number of significant figures (usually one or two). Let's round to two decimal places to match the precision of our input current:
$\Delta R \approx 0.16\,\Omega$.

We then ensure our best estimate of the resistance matches that same decimal place (the hundredths place):
$R = 5.00\,\Omega$.

---

### 3. Final Answer

*   **Calculated Resistance:** $R = (5.00 \pm 0.16)\,\Omega$
