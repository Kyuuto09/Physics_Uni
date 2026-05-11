# Problem 3: Mixed Circuit

### 1. Problem Statement

Calculate the equivalent resistance for the circuit shown in the figure. All resistors have a resistance of $5\ \Omega$.

![[Pasted image 20260511155957.png]]

---

### 2. Solution and Explanation

**Concept Intuition:**
When faced with a complex web of resistors, the most reliable strategy is to identify the "Nodes" (the junctions where wires meet) and redraw or map the circuit based on which resistors connect which nodes. By doing this, we can collapse the complex web into simple series and parallel pairs, working from the inside out.

#### Step 1: Identify Key Nodes and Resistors
Let's carefully trace the diagram and label the critical nodes. Assume every gray box is a $5\ \Omega$ resistor.
*   **Node A (Input):** The entire bottom-left section. This includes the input terminal, the bottom-left corner, and the left vertical wire up to the first dot.
*   **Node B (Output):** The bottom-right dot, where the circuit exits.
*   **Node C (Top Junction):** The dot on the top horizontal wire.
*   **Node D (Middle Junction):** The intersection dot in the very center of the diagram.

Now, let's map how the 8 resistors in the diagram connect these nodes:
1.  **Top-Left Outer Path:** Current goes UP from Node A, through a vertical resistor, turns right, and goes through a horizontal resistor to reach Node C. These two are in series.
    $$R_{AC1} = 5\,\Omega + 5\,\Omega = 10\,\Omega$$
2.  **Right Outer Path:** From Node C, wire goes right, turns down, and passes through *two* vertical resistors to reach Node B.
    $$R_{CB} = 5\,\Omega + 5\,\Omega = 10\,\Omega$$
3.  **Bottom Path:** A single horizontal resistor directly connects the input (Node A) to the output (Node B).
    $$R_{AB} = 5\,\Omega$$
4.  **Middle Horizontal:** A resistor connects the left wire (Node A) directly to the center junction (Node D).
    $$R_{AD1} = 5\,\Omega$$
5.  **Middle Vertical (Bottom):** A resistor goes down from the center junction (Node D), turns left, and connects back to the left wire (Node A).
    $$R_{AD2} = 5\,\Omega$$
6.  **Middle Vertical (Top):** A resistor connects Node C straight down to Node D.
    $$R_{CD} = 5\,\Omega$$

#### Step 2: Simplify the Inner Loop
Notice that the middle horizontal resistor ($R_{AD1}$) and the bottom-middle vertical resistor ($R_{AD2}$) are both connected exactly between Node A and Node D. This means they are in **parallel**.
$$R_{AD\_eq} = \frac{5 \times 5}{5 + 5} = \frac{25}{10} = 2.5\,\Omega$$

Now, Node D simply connects Node C to Node A. The path goes from C, through $R_{CD}$ ($5\,\Omega$) to D, and then from D through our new $R_{AD\_eq}$ ($2.5\,\Omega$) to A. These are in **series**.
$$R_{AC2} = 5\,\Omega + 2.5\,\Omega = 7.5\,\Omega$$

#### Step 3: Simplify the Parallel Paths to Node C
We now have two distinct paths connecting Node A to Node C:
1.  The outer top-left path: $R_{AC1} = 10\,\Omega$
2.  The inner middle path we just simplified: $R_{AC2} = 7.5\,\Omega$

Since they both bridge A and C, they are in **parallel**:
$$\frac{1}{R_{AC\_total}} = \frac{1}{10} + \frac{1}{7.5}$$
To make the math easier, use a common denominator ($30$):
$$\frac{1}{R_{AC\_total}} = \frac{3}{30} + \frac{4}{30} = \frac{7}{30}$$
$$R_{AC\_total} = \frac{30}{7}\,\Omega$$

#### Step 4: Final Equivalent Resistance
The entire left and middle portion of the circuit has been collapsed into $R_{AC\_total}$. This block is in **series** with the right-hand path leading to the output.
$$R_{top\_branch} = R_{AC\_total} + R_{CB}$$
$$R_{top\_branch} = \frac{30}{7} + 10 = \frac{30}{7} + \frac{70}{7} = \frac{100}{7}\,\Omega$$

Finally, this entire top branch is in **parallel** with the direct bottom resistor $R_{AB}$ ($5\,\Omega$).
$$R_{eq} = \frac{R_{top\_branch} \times R_{AB}}{R_{top\_branch} + R_{AB}}$$
$$R_{eq} = \frac{\frac{100}{7} \times 5}{\frac{100}{7} + 5}$$
$$R_{eq} = \frac{\frac{500}{7}}{\frac{100}{7} + \frac{35}{7}}$$
$$R_{eq} = \frac{\frac{500}{7}}{\frac{135}{7}}$$
$$R_{eq} = \frac{500}{135} = \frac{100}{27}\,\Omega$$

---

### 3. Final Answer

*   **Equivalent Resistance ($R_{eq}$):** $\frac{100}{27}\,\Omega \approx 3.70\,\Omega$
