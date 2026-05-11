# Problem 5: Kirchhoff's Laws

### 1. Problem Statement

Using Kirchhoff’s laws, find the currents $I_1$, $I_2$, $I_3$ (going through the resistors $R_1$, $R_2$, $R_3$ respectively) in the following two-loop circuit:

- Left loop: ammeter $A$, top resistor $R_1 = 20\,\Omega$, and bottom source $\mathcal{E}_1 = 4.5\,\text{V}$ in series with internal resistance $r_w = 1\,\Omega$.
- Right loop: source $\mathcal{E}_2 = 9\,\text{V}$ in series with internal resistance $r_w = 1\,\Omega$.
- Shared branch: resistor $R_2 = 10\,\Omega$ connecting the top-right node to the bottom node.

*(Note: The problem text mentions an $R_3$, which is absent from the diagram. We will assume $I_3$ refers to the current flowing through the right branch containing $\mathcal{E}_2$ and its internal resistance $r_w$.)
![[Pasted image 20260511160726.png]]

---

### 2. Solution and Explanation

**Concept Intuition:**
Kirchhoff's Laws give us a foolproof way to solve any complex circuit by setting up a system of algebraic equations. 
1.  **Kirchhoff's Current Law (KCL):** What goes in must come out. At any junction, the total current flowing in equals the total current flowing out.
2.  **Kirchhoff's Voltage Law (KVL):** The total energy gained from batteries in a closed loop must be completely spent by the time you finish the loop. The sum of all voltage changes around a loop is exactly zero.

#### Step 1: Define Current Directions
Before writing equations, we must guess the direction of the currents. It doesn't matter if we guess wrong; the math will simply give us a negative number at the end, telling us the current flows the opposite way!

*   Let **$I_1$** be the current in the left loop, flowing **clockwise**. (It flows RIGHT across the top wire).
*   Let **$I_3$** be the current in the right loop, flowing **counter-clockwise**. (It flows UP the right wire and LEFT across the top wire).
*   Let **$I_2$** be the current in the shared middle branch, flowing **DOWN**.

#### Step 2: Apply Kirchhoff's Current Law (KCL)
Look at the **top junction**. Current $I_1$ is entering from the left, and $I_3$ is entering from the right. They combine and flow straight down as $I_2$.
$$I_1 + I_3 = I_2 \quad \text{--- (Equation 1)}$$

#### Step 3: Apply Kirchhoff's Voltage Law (KVL)
We will trace around each loop and sum the voltage drops. 
*Rule:* Going from the short line ($-$) to the long line ($+$) of a battery gives a **positive** voltage change. Flowing *with* our defined current through a resistor gives a **negative** voltage drop ($-I \cdot R$).

**Left Loop (trace clockwise):**
Start at the bottom junction and trace clockwise around the left square.
1.  Go left along the bottom wire. We pass through $\mathcal{E}_1$. The long bar is on the left, so we go from $-$ to $+$. Voltage change: **$+4.5\text{ V}$**.
2.  Pass through $r_w = 1\,\Omega$. We are flowing with $I_1$. Voltage change: **$-1 \cdot I_1$**.
3.  Go up and right, passing through $R_1 = 20\,\Omega$. Voltage change: **$-20 \cdot I_1$**.
4.  Go down the middle branch through $R_2 = 10\,\Omega$. We are flowing with $I_2$. Voltage change: **$-10 \cdot I_2$**.
$$+4.5 - 1 I_1 - 20 I_1 - 10 I_2 = 0$$
$$4.5 - 21 I_1 - 10 I_2 = 0 \quad \text{--- (Equation 2)}$$

**Right Loop (trace counter-clockwise):**
Start at the bottom junction and trace counter-clockwise around the right square.
1.  Go right and up the outer wire. We pass through $\mathcal{E}_2$. The long bar is on top, so we go from $-$ to $+$. Voltage change: **$+9\text{ V}$**.
2.  Pass through $r_w = 1\,\Omega$ with current $I_3$. Voltage change: **$-1 \cdot I_3$**.
3.  Go left and down the middle branch through $R_2$ with current $I_2$. Voltage change: **$-10 \cdot I_2$**.
$$+9 - 1 I_3 - 10 I_2 = 0$$
$$9 - I_3 - 10 I_2 = 0 \quad \text{--- (Equation 3)}$$

#### Step 4: Solve the System of Equations
Let's rearrange Equation 3 to isolate $I_3$:
$$I_3 = 9 - 10 I_2$$

Substitute this into Equation 1 to find $I_1$:
$$I_1 + (9 - 10 I_2) = I_2$$
$$I_1 = 11 I_2 - 9$$

Now, substitute $I_1$ into Equation 2:
$$4.5 - 21(11 I_2 - 9) - 10 I_2 = 0$$
$$4.5 - 231 I_2 + 189 - 10 I_2 = 0$$
$$193.5 - 241 I_2 = 0$$
$$241 I_2 = 193.5$$
$$I_2 = \frac{193.5}{241} \approx 0.803\text{ A}$$

Now plug $I_2$ back into our substituted equations to find $I_1$ and $I_3$:
$$I_1 = 11(0.8029) - 9 = 8.8319 - 9 \approx -0.168\text{ A}$$
*(The negative sign simply means our initial guess for $I_1$ was backwards. It actually flows counter-clockwise!)*

$$I_3 = 9 - 10(0.8029) = 9 - 8.029 \approx 0.971\text{ A}$$

---

### 3. Final Answers

*   **Current $I_1$ (through left branch):** $-0.168\text{ A}$ (Flows counter-clockwise)
*   **Current $I_2$ (through middle $R_2$):** $0.803\text{ A}$ (Flows downwards)
*   **Current $I_3$ (through right branch):** $0.971\text{ A}$ (Flows counter-clockwise)

*(Exact fractions: $I_1 = \frac{-40.5}{241}\text{ A}$, $I_2 = \frac{193.5}{241}\text{ A}$, $I_3 = \frac{234}{241}\text{ A}$)*
