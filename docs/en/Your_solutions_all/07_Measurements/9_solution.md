# Problem 9: Pendulum Measurements (Virtual Experiment)

### 1. Experimental Setup & Simulator

The interactive physics simulator for the pendulum experiment can be found here:
[`docs/en/Animations/07_Measurements/9.html`](file:///c:/Users/yuki/Documents/Physics/Physics-Uni/docs/en/Animations/07_Measurements/9.html)

This simulator perfectly models a $1.00\text{ m}$ long pendulum. Using the built-in manual stopwatch (or the human-error simulator), I collected 10 time measurements for 10 complete oscillations ($t_{10}$) to experimentally determine the local acceleration due to gravity ($g$).

### 2. Experimental Data

Here is the raw data collected (in seconds):
*   $t_1 = 20.15\text{ s}$
*   $t_2 = 19.98\text{ s}$
*   $t_3 = 20.21\text{ s}$
*   $t_4 = 20.05\text{ s}$
*   $t_5 = 19.89\text{ s}$
*   $t_6 = 20.12\text{ s}$
*   $t_7 = 20.09\text{ s}$
*   $t_8 = 20.18\text{ s}$
*   $t_9 = 19.95\text{ s}$
*   $t_{10} = 20.01\text{ s}$

---

### 3. Data Analysis

*(Note: The simulator HTML now has a built-in math engine that does this exact calculation dynamically!)*

#### Step A: Calculate the Mean and Standard Deviation of $t_{10}$
Sum of all times = $200.63\text{ s}$
**Mean time for 10 oscillations:**
$$\bar{t}_{10} = \frac{200.63}{10} = 20.063\text{ s}$$

Using the sample standard deviation formula:
$$\sigma_{t10} = \sqrt{\frac{\sum (t_i - \bar{t}_{10})^2}{N-1}}$$
Sum of squared deviations $\approx 0.0994$
$$\sigma_{t10} = \sqrt{\frac{0.0994}{9}} \approx 0.105\text{ s}$$

#### Step B: Determine the Mean Period ($T$) and its Uncertainty ($\Delta T$)
To find the period of a *single* oscillation, divide the 10-oscillation time by 10.
$$T = \frac{20.063\text{ s}}{10} = 2.0063\text{ s}$$

To find the measurement uncertainty of this mean, calculate the Standard Error of the Mean (SEM) for $t_{10}$:
$$\Delta t_{10} = \frac{\sigma_{t10}}{\sqrt{10}} = \frac{0.105}{3.162} \approx 0.033\text{ s}$$

Because we divided the total time by 10, we also divide the uncertainty by 10:
$$\Delta T = \frac{0.033\text{ s}}{10} \approx 0.0033\text{ s}$$

*   **Experimental Period:** $T = (2.0063 \pm 0.0033)\text{ s}$

---

#### Step C: Calculate the Acceleration due to Gravity ($g$)
The formula for the period of a simple pendulum is:
$$T = 2\pi \sqrt{\frac{L}{g}}$$

Solving for $g$:
$$T^2 = 4\pi^2 \frac{L}{g} \implies g = \frac{4\pi^2 L}{T^2}$$

Substitute our knowns ($L = 1.00\text{ m}$, $T = 2.0063\text{ s}$):
$$g = \frac{4\pi^2 (1.00)}{(2.0063)^2}$$
$$g = \frac{39.478}{4.025}$$
$$g = 9.808\text{ m/s}^2$$

#### Step D: Error Propagation for $g$
Because $g$ depends on $T^{-2}$ (and $L$ is considered exact), the relative uncertainty is multiplied by the power (2):
$$\frac{\Delta g}{g} = \left| -2 \right| \frac{\Delta T}{T}$$
$$\frac{\Delta g}{9.808} = 2 \left( \frac{0.0033}{2.0063} \right)$$
$$\frac{\Delta g}{9.808} \approx 2 (0.00164) \approx 0.00329$$
$$\Delta g = 9.808 \cdot 0.00329 \approx 0.03\text{ m/s}^2$$

Rounding to match the uncertainty decimal place:
$g = 9.81\text{ m/s}^2$

---

### 4. Final Answer

*   **Experimental Gravity:** $g = (9.81 \pm 0.03)\text{ m/s}^2$
