# Problem 4: Mixed Circuit

### 1. Problem Statement

Calculate the equivalent resistance for the circuit shown in the figure. All resistors have a resistance of $10\ \Omega$.

![[Pasted image 20260511160247.png]]

---

### 2. Solution and Explanation

**Concept Intuition:**
Just like the previous problem, we can solve this by breaking the circuit down into smaller, simpler chunks. We start from the most "nested" part of the circuit (the small parallel pair in the bottom branch) and work our way outward, replacing complex blocks with single equivalent resistors until we are left with a single value.

#### Step 1: Identify the Branches
Let's break the circuit down into three main sections based on the diagram:
1.  **Top Branch:** Two resistors in series.
2.  **Bottom Branch:** One resistor in series with a nested parallel pair of resistors.
3.  **Output Branch:** One resistor in series with the entire main parallel block.

Assume every gray box is a $10\ \Omega$ resistor.

#### Step 2: Simplify the Bottom Branch
Let's look closely at the bottom branch.
First, there is a small parallel block where the wire splits, goes through two separate resistors (let's call them $R_{B2}$ and $R_{B3}$), and joins back together.
Since they are in **parallel**:
$$R_{parallel\_pair} = \frac{10 \times 10}{10 + 10} = \frac{100}{20} = 5\,\Omega$$

Now, this entire $5\,\Omega$ pair is in **series** with the first resistor in that bottom path ($R_{B1} = 10\,\Omega$). 
$$R_{bottom\_total} = R_{B1} + R_{parallel\_pair}$$
$$R_{bottom\_total} = 10\,\Omega + 5\,\Omega = 15\,\Omega$$

#### Step 3: Simplify the Top Branch
The top branch is much simpler. The current just flows straight through two resistors in a row. They are in **series**.
$$R_{top\_total} = 10\,\Omega + 10\,\Omega = 20\,\Omega$$

#### Step 4: Calculate the Main Parallel Block
Now, we can treat the entire middle section of the circuit as two simple branches in **parallel**:
*   Top path: $20\,\Omega$
*   Bottom path: $15\,\Omega$

Let's find the equivalent resistance of this main block ($R_{block}$):
$$R_{block} = \frac{R_{top\_total} \times R_{bottom\_total}}{R_{top\_total} + R_{bottom\_total}}$$
$$R_{block} = \frac{20 \times 15}{20 + 15}$$
$$R_{block} = \frac{300}{35}$$
$$R_{block} = \frac{60}{7}\,\Omega \approx 8.57\,\Omega$$

#### Step 5: Final Equivalent Resistance
Finally, all the current that exits this massive parallel block must flow through the last remaining resistor ($R_{out} = 10\,\Omega$) on the far right. This means the block and $R_{out}$ are in **series**.
$$R_{eq} = R_{block} + R_{out}$$
$$R_{eq} = \frac{60}{7} + 10$$
$$R_{eq} = \frac{60}{7} + \frac{70}{7}$$
$$R_{eq} = \frac{130}{7}\,\Omega$$

---

### 3. Final Answer

*   **Equivalent Resistance ($R_{eq}$):** $\frac{130}{7}\,\Omega \approx 18.57\,\Omega$
