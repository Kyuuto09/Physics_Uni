# Problem 2: Resistors Combinations

### 1. Problem Statement

You have a supply of exactly three $1\,\Omega$ resistors. What are all the possible equivalent resistances you can create by combining them? List all unique values.

---

### 2. Solution and Explanation

**Concept Intuition:**
When given a fixed number of identical components, we must exhaustively list out all topological combinations. With exactly three resistors, there are four distinct ways to connect them:
1. All three in a single line (**Series**).
2. All three branching off the same nodes (**Parallel**).
3. Two in a line, with the third bypassing them (**Two in Series, parallel to the third**).
4. Two branching parallel to each other, placed in line with the third (**Two in Parallel, series with the third**).

Because each resistor has a value of exactly $R = 1\,\Omega$, the math is exceptionally clean!

#### Configuration 1: All 3 in Series
When placed end-to-end, the resistances add together directly.
$$R_{eq} = R_1 + R_2 + R_3$$
$$R_{eq} = 1 + 1 + 1 = 3\,\Omega$$

#### Configuration 2: All 3 in Parallel
When placed in separate parallel branches, their reciprocals add together.
$$\frac{1}{R_{eq}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3}$$
$$\frac{1}{R_{eq}} = \frac{1}{1} + \frac{1}{1} + \frac{1}{1} = 3$$
Flipping both sides:
$$R_{eq} = \frac{1}{3}\,\Omega \approx 0.33\,\Omega$$

#### Configuration 3: Two in Series, combined in Parallel with the third
First, combine the two resistors in series to find the resistance of that specific branch:
$$R_{branch} = 1 + 1 = 2\,\Omega$$
Next, combine this $2\,\Omega$ branch in parallel with the remaining $1\,\Omega$ resistor:
$$\frac{1}{R_{eq}} = \frac{1}{R_{branch}} + \frac{1}{R_{remaining}}$$
$$\frac{1}{R_{eq}} = \frac{1}{2} + \frac{1}{1}$$
$$\frac{1}{R_{eq}} = \frac{1}{2} + \frac{2}{2} = \frac{3}{2}$$
Flipping both sides:
$$R_{eq} = \frac{2}{3}\,\Omega \approx 0.67\,\Omega$$

#### Configuration 4: Two in Parallel, combined in Series with the third
First, combine the two parallel resistors into a single equivalent "block":
$$\frac{1}{R_{block}} = \frac{1}{1} + \frac{1}{1} = 2 \implies R_{block} = \frac{1}{2}\,\Omega = 0.5\,\Omega$$
Next, place this $0.5\,\Omega$ block in series with the remaining $1\,\Omega$ resistor:
$$R_{eq} = R_{block} + R_{remaining}$$
$$R_{eq} = 0.5 + 1 = 1.5\,\Omega \quad \left(\text{or } \frac{3}{2}\,\Omega\right)$$

---

### 3. Final Answers

There are exactly **4 unique values** you can create with three $1\,\Omega$ resistors. Listed from lowest to highest:

1. **$1/3\,\Omega$** (All parallel)
2. **$2/3\,\Omega$** (Two in series, parallel to third)
3. **$3/2\,\Omega$** (Two in parallel, series with third)
4. **$3\,\Omega$** (All series)
