# Problem 10: Linear Regression Analysis

### 1. Experimental Setup & Interactive Tool

To fully visualize how Linear Regression works, I have built an interactive HTML tool where you can plot these points and see the math happen in real-time!
[`docs/en/Animations/07_Measurements/10.html`](file:///c:/Users/yuki/Documents/Physics/Physics-Uni/docs/en/Animations/07_Measurements/10.html)

### 2. Problem Statement

A series of voltage and current measurements for a resistor are taken. Use linear regression to find the best-fit line $V = I R + V_0$ and calculate the resistance $R$ and the zero-offset $V_0$. Estimate the uncertainties in $R$ and $V_0$.
**Data $(I, V)$:** $(0.1, 1.1), (0.2, 2.1), (0.3, 2.9), (0.4, 4.1), (0.5, 4.9)$

---

### 3. Solution and Explanation

**Concept Intuition:**
We are fitting a line $y = mx + c$ to our data, where the slope ($m$) represents the Resistance ($R$) and the y-intercept ($c$) represents the voltmeter's zero-offset ($V_0$). We use the **Least Squares** method to find the line that mathematically minimizes the squared vertical distances (residuals) from the points to the line.

#### Step 1: Calculate the Sums
Let $x = I$ and $y = V$. We have $N = 5$ data points.
*   $\sum x = 0.1 + 0.2 + 0.3 + 0.4 + 0.5 = 1.5$
*   $\sum y = 1.1 + 2.1 + 2.9 + 4.1 + 4.9 = 15.1$
*   $\sum x^2 = (0.1)^2 + (0.2)^2 + (0.3)^2 + (0.4)^2 + (0.5)^2 = 0.55$
*   $\sum xy = (0.1)(1.1) + (0.2)(2.1) + (0.3)(2.9) + (0.4)(4.1) + (0.5)(4.9) = 5.49$

We also calculate the denominator determinant ($\Delta$):
$$\Delta = N \sum x^2 - (\sum x)^2$$
$$\Delta = 5(0.55) - (1.5)^2 = 2.75 - 2.25 = 0.5$$

#### Step 2: Calculate Slope ($R$) and Intercept ($V_0$)
**Resistance (Slope):**
$$R = \frac{N \sum xy - \sum x \sum y}{\Delta}$$
$$R = \frac{5(5.49) - (1.5)(15.1)}{0.5} = \frac{27.45 - 22.65}{0.5} = \frac{4.8}{0.5} = 9.6\,\Omega$$

**Zero-offset (Intercept):**
$$V_0 = \frac{\sum x^2 \sum y - \sum x \sum xy}{\Delta}$$
$$V_0 = \frac{(0.55)(15.1) - (1.5)(5.49)}{0.5} = \frac{8.305 - 8.235}{0.5} = \frac{0.07}{0.5} = 0.14\text{ V}$$

#### Step 3: Calculate Uncertainties
First, find the variance of the residuals ($s_y^2$), which measures how far the points are from our new line $V = 9.6I + 0.14$.
$$s_y = \sqrt{\frac{\sum(y_i - y_{fit})^2}{N-2}}$$
*(Skipping the individual residual arithmetic, the sum of squared residuals is $0.032$)*
$$s_y = \sqrt{\frac{0.032}{3}} \approx 0.1033$$

Now, calculate the final uncertainties:
**Uncertainty in R:**
$$\Delta R = s_y \sqrt{\frac{N}{\Delta}} = 0.1033 \sqrt{\frac{5}{0.5}} = 0.1033 \sqrt{10} \approx 0.326\,\Omega \rightarrow 0.3\,\Omega$$

**Uncertainty in $V_0$:**
$$\Delta V_0 = s_y \sqrt{\frac{\sum x^2}{\Delta}} = 0.1033 \sqrt{\frac{0.55}{0.5}} = 0.1033 \sqrt{1.1} \approx 0.108\text{ V} \rightarrow 0.11\text{ V}$$

---

### 4. Final Answer

*   **Resistance:** $R = (9.6 \pm 0.3)\,\Omega$
*   **Zero-offset:** $V_0 = (0.14 \pm 0.11)\text{ V}$
