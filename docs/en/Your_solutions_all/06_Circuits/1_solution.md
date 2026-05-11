# Problem 1: Series and Parallel Circuit

### 1. Problem Statement

You have three resistors, $R_1=15\,\Omega$, $R_2=30\,\Omega$, and $R_3=50\,\Omega$ and a $12\text{ V}$ battery. Consider the case when they are all connected in series and when all of them are connected in parallel. Calculate the total equivalent resistance in each case. Calculate the current flowing from the battery in each case.

---

### 2. Solution and Explanation

**Concept Intuition:**
* **Series Connection:** Think of this as a single-lane road with three toll booths in a row. The electricity is forced to push through *every single resistor* sequentially. Therefore, the resistances simply stack on top of each other, creating a high total resistance, which chokes the total current down.
* **Parallel Connection:** Think of this as taking that single-lane road and splitting it into three separate parallel lanes. The electricity now has multiple paths to choose from. Even though the individual lanes have resistance, having *more paths available* actually makes it easier for the total current to flow. The total resistance of a parallel circuit is always *less* than the smallest individual resistor!

#### Part A: Series Circuit

**Step 1: Calculate Equivalent Resistance ($R_{series}$)**
In a series circuit, you simply add the resistances together:
$$R_{series} = R_1 + R_2 + R_3$$
$$R_{series} = 15\,\Omega + 30\,\Omega + 50\,\Omega$$
$$R_{series} = 95\,\Omega$$

**Step 2: Calculate Total Current ($I_{series}$)**
Using Ohm's Law ($V = I \cdot R$), we can rearrange to solve for current ($I = \frac{V}{R}$):
$$I_{series} = \frac{V}{R_{series}}$$
$$I_{series} = \frac{12\text{ V}}{95\,\Omega}$$
$$I_{series} \approx 0.1263\text{ A} \quad \text{(or } 126.3\text{ mA)}$$

---

#### Part B: Parallel Circuit

**Step 1: Calculate Equivalent Resistance ($R_{parallel}$)**
In a parallel circuit, you add the *reciprocals* of the resistances:
$$\frac{1}{R_{parallel}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3}$$
$$\frac{1}{R_{parallel}} = \frac{1}{15} + \frac{1}{30} + \frac{1}{50}$$

To add these fractions, we find a common denominator (which is $150$):
$$\frac{1}{R_{parallel}} = \frac{10}{150} + \frac{5}{150} + \frac{3}{150}$$
$$\frac{1}{R_{parallel}} = \frac{18}{150}$$

Now, "flip" both sides of the equation to solve for $R_{parallel}$:
$$R_{parallel} = \frac{150}{18}\,\Omega$$
$$R_{parallel} = \frac{25}{3}\,\Omega \approx 8.33\,\Omega$$
*(Notice how the total resistance of $8.33\,\Omega$ is indeed smaller than our smallest resistor, $15\,\Omega$!)*

**Step 2: Calculate Total Current ($I_{parallel}$)**
Again, using Ohm's Law:
$$I_{parallel} = \frac{V}{R_{parallel}}$$
$$I_{parallel} = \frac{12\text{ V}}{25/3\,\Omega}$$
$$I_{parallel} = 12 \times \frac{3}{25}$$
$$I_{parallel} = \frac{36}{25}\text{ A} = 1.44\text{ A}$$

---

### 3. Final Answers

**Series Case:**
* **Equivalent Resistance:** $95\,\Omega$
* **Total Current:** $\approx 0.126\text{ A}$ (or $126\text{ mA}$)

**Parallel Case:**
* **Equivalent Resistance:** $\approx 8.33\,\Omega$ (or $\frac{25}{3}\,\Omega$)
* **Total Current:** $1.44\text{ A}$
