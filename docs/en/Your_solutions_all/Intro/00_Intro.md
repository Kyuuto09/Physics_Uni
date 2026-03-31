# Section 0: Mathematical Foundations - Vector Algebra

**Table of Contents**

- [Problem 1: Magnitude, Dot Product, Cross Product, and Angle](#problem-1-magnitude-dot-product-cross-product-and-angle)
- [Problem 2: Systems of Equations](#problem-2-systems-of-equations)
- [Problem 3: Proportionality in Physics](#problem-3-proportionality-in-physics)
- [Problem 4: Rearranging Formulas](#problem-4-rearranging-formulas)
- [Problem 5: Trigonometry - Vector Components](#problem-5-trigonometry---vector-components)
- [Problem 6: Function Analysis](#problem-6-function-analysis)
- [Problem 7: Logic & Series - The Fly and the Bicycle](#problem-7-logic--series---the-fly-and-the-bicycle)
- [Problem 8: Definite Integrals](#problem-8-definite-integrals)
- [Problem 9: Optimization Problem](#problem-9-optimization-problem)
- [Problem 10: Infinite Series - The Ant's Path](#problem-10-infinite-series---the-ants-path)

---

## Problem 1: Magnitude, Dot Product, Cross Product, and Angle

### 1. Problem Statement

Given two vectors in 3D space:

$$\vec{a} = [2, 1, -3]$$
$$\vec{b} = [4, -2, 1]$$

Compute the magnitude, dot product, cross product, and the angle between them.

---

### 2. Solutions and Explanations

#### a) Magnitude

The magnitude represents the straight-line length of the vector.

**Formula:**
$$|\vec{v}| = \sqrt{x^2 + y^2 + z^2}$$

**Calculation for $\vec{a}$:**
$$|\vec{a}| = \sqrt{2^2 + 1^2 + (-3)^2}$$
$$|\vec{a}| = \sqrt{4 + 1 + 9} = \sqrt{14} \approx 3.74$$

**Calculation for $\vec{b}$:**
$$|\vec{b}| = \sqrt{4^2 + (-2)^2 + 1^2}$$
$$|\vec{b}| = \sqrt{16 + 4 + 1} = \sqrt{21} \approx 4.58$$

---

#### b) Dot Product ($\vec{a} \cdot \vec{b}$)

The dot product is a single number (scalar) found by multiplying the corresponding parts of each vector and adding them together.

**Formula:**
$$\vec{a} \cdot \vec{b} = (a_x \cdot b_x) + (a_y \cdot b_y) + (a_z \cdot b_z)$$

**Calculation:**
$$\vec{a} \cdot \vec{b} = (2 \cdot 4) + (1 \cdot -2) + (-3 \cdot 1)$$
$$\vec{a} \cdot \vec{b} = 8 + (-2) + (-3)$$
$$\vec{a} \cdot \vec{b} = 3$$

---

#### c) Cross Product ($\vec{a} \times \vec{b}$)

The cross product creates a new vector that is perpendicular to both $\vec{a}$ and $\vec{b}$. We use a matrix determinant to find the three new coordinates.

**Formula:**
$$\vec{a} \times \vec{b} = [(a_y b_z - a_z b_y), (a_z b_x - a_x b_z), (a_x b_y - a_y b_x)]$$

**Calculation:**

1. **x-component:** $(1 \cdot 1) - (-3 \cdot -2) = 1 - 6 = -5$
2. **y-component:** $(-3 \cdot 4) - (2 \cdot 1) = -12 - 2 = -14$
3. **z-component:** $(2 \cdot -2) - (1 \cdot 4) = -4 - 4 = -8$

**Result:**
$$\vec{a} \times \vec{b} = [-5, -14, -8]$$

---

#### d) Angle Between Vectors ($\theta$)

We can find the angle by using the dot product and the lengths (magnitudes) of the vectors.

**Formula:**
$$\cos(\theta) = \frac{\vec{a} \cdot \vec{b}}{|\vec{a}| \cdot |\vec{b}|}$$

**Calculation:**
$$\cos(\theta) = \frac{3}{\sqrt{14} \cdot \sqrt{21}}$$
$$\cos(\theta) = \frac{3}{\sqrt{294}} \approx 0.1749$$

To find the angle $\theta$:
$$\theta = \arccos(0.1749) \approx 79.93^\circ$$

---

## Problem 2: Systems of Equations

### 1. Problem Statement

Find the values of $x$ and $y$ that satisfy both equations:
$$2x + 3y = 12$$
$$x - y = 1$$

---

### 2. Solution and Explanation

**Concept Intuition:**
Imagine these two equations as two straight lines on a graph. Finding the values of $x$ and $y$ that satisfy _both_ equations means finding the exact coordinates where these two lines intersect.

We will use the **Substitution Method**. This involves getting one variable by itself, and then "substituting" it into the other equation.

#### Step 1: Isolate one variable

Always look for the easiest letter to get by itself. In the second equation ($x - y = 1$), it is very easy to isolate $x$ by adding $y$ to both sides.

$$x - y = 1$$
$$x = y + 1$$

Now we have a temporary "definition" for $x$.

#### Step 2: Substitute into the other equation

Take the first equation and replace the $x$ with our new definition ($y + 1$).

Original first equation:
$$2x + 3y = 12$$

Substitute $x$:
$$2(y + 1) + 3y = 12$$

#### Step 3: Solve for $y$

Now we have an equation with only $y$, which is easy to solve. First, expand the brackets by multiplying by $2$:

$$2y + 2 + 3y = 12$$

Combine the matching $y$ terms ($2y + 3y$):

$$5y + 2 = 12$$

Subtract $2$ from both sides to get the $y$ term by itself:

$$5y = 12 - 2$$
$$5y = 10$$

Divide by $5$:

$$y = 2$$

#### Step 4: Find $x$

Now that we know exactly what $y$ is, we can plug it back into our isolated $x$ equation from Step 1.

$$x = y + 1$$
$$x = 2 + 1$$
$$x = 3$$

---

### 3. Final Answer

The solution that satisfies both equations is:
$$x = 3$$
$$y = 2$$

_(Self-Check: You can verify this by plugging them into the original equations. $2(3) + 3(2) = 6 + 6 = 12$. And $3 - 2 = 1$. The math is perfectly balanced.)_

---

## Problem 3: Proportionality in Physics

### 1. Problem Statement

Consider the Universal Law of Gravitation:
$$F = G \frac{m_1 m_2}{r^2}$$
where $F$ is the gravitational force between two masses $m_1$ and $m_2$, $r$ is the distance between their centers, and $G$ is the gravitational constant.

Determine the factor by which the force $F$ changes if the distance $r$ is _doubled_ and both masses ($m_1$ and $m_2$) are _halved_.

---

### 2. Solution and Explanation

**Concept Intuition:**
Proportionality is about understanding cause and effect. We are changing the "inputs" (the masses and the distance) to see how the "output" (the force) reacts.

- **Masses (Numerator):** Because masses are on the top of the fraction, making them smaller directly makes the force smaller.
- **Distance (Denominator):** Because distance is on the bottom and is _squared_, changing the distance has a massive, opposite effect on the force. Making the distance larger makes the force much smaller.

#### Step 1: Define the "New" Variables

Let's write down our new values based on the rules given in the problem. We will use a prime symbol ($'$) to represent the "new" versions.

- The new first mass is half the original: $m_1' = \frac{m_1}{2}$
- The new second mass is half the original: $m_2' = \frac{m_2}{2}$
- The new distance is twice the original: $r' = 2r$

#### Step 2: Substitute into the Formula

Now, plug these new variables into the formula to find the new force ($F'$).

$$F' = G \frac{m_1' \cdot m_2'}{(r')^2}$$

Substitute the definitions from Step 1:
$$F' = G \frac{(\frac{m_1}{2}) \cdot (\frac{m_2}{2})}{(2r)^2}$$

#### Step 3: Simplify the Math

First, multiply the two fractions in the top part (numerator):
$$(\frac{m_1}{2}) \cdot (\frac{m_2}{2}) = \frac{m_1 \cdot m_2}{4}$$

Next, square the bottom part (denominator). Remember to apply the square to both the $2$ and the $r$:
$$(2r)^2 = 2^2 \cdot r^2 = 4r^2$$

Now put them back into the main equation:
$$F' = G \frac{\frac{m_1 m_2}{4}}{4r^2}$$

#### Step 4: Isolate the Original Formula

To simplify a fraction that is divided by another number, you multiply the denominators together ($4 \cdot 4 = 16$).

$$F' = G \frac{m_1 m_2}{16r^2}$$

Now, pull the $\frac{1}{16}$ out to the front so we can clearly see the original formula:
$$F' = \frac{1}{16} \left( G \frac{m_1 m_2}{r^2} \right)$$

Notice that the part inside the parentheses is exactly our original force formula, $F$.

$$F' = \frac{1}{16} F$$

---

### 3. Final Answer

The new force is $\frac{1}{16}$ of the original force.
Therefore, the force $F$ changes by a factor of $\frac{1}{16}$.

---

## Problem 4: Rearranging Formulas

### 1. Problem Statement

The formula for the period of a simple pendulum is:
$$T = 2\pi \sqrt{\frac{L}{g}}$$

Rearrange the equation to give a formula for $g$ (acceleration due to gravity).

---

### 2. Solution and Explanation

**Concept Intuition:**
Rearranging a formula is like unpacking a box. You have to remove the outer layers one by one until you reach the item you want ($g$) in the middle. The operations we use are always the exact opposite of what is currently happening to the variable.

#### Step 1: Isolate the square root

Right now, the square root is being multiplied by $2\pi$. To "unpack" this outer layer, we do the opposite: divide both sides by $2\pi$.

$$\frac{T}{2\pi} = \sqrt{\frac{L}{g}}$$

#### Step 2: Eliminate the square root

The next layer is the square root. The opposite of a square root is squaring. We must square both sides of the entire equation. Remember to apply the square to everything inside the parentheses.

$$\left(\frac{T}{2\pi}\right)^2 = \left(\sqrt{\frac{L}{g}}\right)^2$$

$$\frac{T^2}{2^2 \cdot \pi^2} = \frac{L}{g}$$

$$\frac{T^2}{4\pi^2} = \frac{L}{g}$$

#### Step 3: Get $g$ out of the denominator

Right now, $g$ is trapped at the bottom of the fraction. The fastest trick to fix this is to flip both fractions completely upside down (taking the reciprocal of both sides).

$$\frac{4\pi^2}{T^2} = \frac{g}{L}$$

#### Step 4: Isolate $g$

Now $g$ is on top, but it is being divided by $L$. We do the opposite and multiply both sides by $L$.

$$\frac{4\pi^2 \cdot L}{T^2} = g$$

---

### 3. Final Answer

The rearranged formula for the acceleration due to gravity is:
$$g = \frac{4\pi^2 L}{T^2}$$

---

## Problem 5: Trigonometry - Vector Components

### 1. Problem Statement

A vector $\vec{A}$ has a magnitude of $15$ and makes an angle of $\theta = 60^\circ$ with the horizontal axis. Calculate its horizontal and vertical components.

---

### 2. Solution and Explanation

**Concept Intuition:**
Imagine you are programming a character to move diagonally across a screen. The computer doesn't natively understand "diagonal." Instead, it needs to know exactly how many pixels to move right (the horizontal component) and how many pixels to move up (the vertical component).

We use Trigonometry to slice the diagonal vector into these two straight pieces:

- **Cosine ($\cos$)** is used for the **horizontal** ($x$) piece (the side touching the angle).
- **Sine ($\sin$)** is used for the **vertical** ($y$) piece (the side opposite to the angle).

#### Step 1: The Horizontal Component ($A_x$)

To find how far the vector goes along the $x$-axis, we multiply the total length (magnitude) by the cosine of the angle.
**Formula:**
$$A_x = A \cos(\theta)$$

**Calculation:**
$$A_x = 15 \cdot \cos(60^\circ)$$

From standard trigonometry rules, we know that $\cos(60^\circ)$ is exactly $0.5$ (or $\frac{1}{2}$).
$$A_x = 15 \cdot 0.5$$
$$A_x = 7.5$$

#### Step 2: The Vertical Component ($A_y$)

To find how far the vector goes along the $y$-axis, we multiply the total length by the sine of the angle.

**Formula:**
$$A_y = A \sin(\theta)$$

**Calculation:**
$$A_y = 15 \cdot \sin(60^\circ)$$

The exact value of $\sin(60^\circ)$ is $\frac{\sqrt{3}}{2}$, which is approximately $0.866$.
$$A_y = 15 \cdot \frac{\sqrt{3}}{2}$$
$$A_y \approx 15 \cdot 0.866$$
$$A_y \approx 12.99$$

---

### 3. Final Answer

The components of the vector $\vec{A}$ are:

- **Horizontal component ($A_x$):** $7.5$
- **Vertical component ($A_y$):** $\frac{15\sqrt{3}}{2}$ (approximately $12.99$)

---

## Problem 6: Function Analysis

### 1. Problem Statement

Consider the function:
$$f(x) = 3x^2 - 12x + 7$$

Identify any local maxima or minima.

---

### 2. Solution and Explanation

**Concept Intuition:**
This function is a quadratic equation, meaning its graph forms a U-shape called a parabola.

- Because the first number ($3$) is positive, the U-shape opens upwards.
- This means the function has a "bottom" point (a local minimum) but no "top" point (it goes up forever, so there is no maximum).

To find this minimum, we need to find the exact coordinates of the vertex (the tip of the U-shape).

#### Step 1: Use the Vertex Formula for the $x$-coordinate

In algebra, the fastest way to find the center (vertex) of a parabola $ax^2 + bx + c$ is using the vertex formula.

- $a = 3$
- $b = -12$
- $c = 7$

**Formula:**
$$x = \frac{-b}{2a}$$

**Calculation:**
$$x = \frac{-(-12)}{2(3)}$$
$$x = \frac{12}{6}$$
$$x = 2$$

The minimum occurs when $x = 2$.

#### Step 2: Find the $y$-coordinate (the actual minimum value)

Now that we know _where_ the minimum happens on the $x$-axis, we plug that number back into the original function to find out exactly _how low_ the graph goes.

**Formula:**
$$f(2) = 3(2)^2 - 12(2) + 7$$

**Calculation:**
$$f(2) = 3(4) - 24 + 7$$
$$f(2) = 12 - 24 + 7$$
$$f(2) = -12 + 7$$
$$f(2) = -5$$

---

### 3. Final Answer

The function has a **local minimum at the point $(2, -5)$**.
Because the parabola opens upwards, it does not have a local maximum.

---

## Problem 7: Logic & Series - The Fly and the Bicycle

### 1. Problem Statement

A bicycle is $10\text{ meters}$ from a wall and moves towards it at a constant speed of $1\text{ m/s}$. A fly starts from the bicycle's front wheel and flies towards the wall at $2\text{ m/s}$. When it hits the wall, it instantly turns back and flies to the bicycle, and so on.

What is the total distance the fly travels before being crushed?

---

### 2. Solution and Explanation

**Concept Intuition:**
This problem is a trap designed to make you do unnecessary math. Instead of trying to track every single zigzag the fly makes, we just need to change our perspective.

Think about the situation like a stopwatch. The fly will keep flying at a constant speed until the exact moment the bicycle hits the wall. If we know **how long** the bicycle takes to crash, we know exactly how long the fly is in the air.

#### Step 1: Calculate the total time until the crash

We ignore the fly completely for a second and just look at the bicycle. We know its distance and its speed.

**Formula for Time:**
$$t = \frac{\text{Distance}}{\text{Speed}}$$

**Calculation for the Bicycle:**
$$t = \frac{10\text{ m}}{1\text{ m/s}}$$
$$t = 10\text{ seconds}$$

The bicycle takes exactly $10\text{ seconds}$ to hit the wall. This means the "stopwatch" for the whole event is exactly $10\text{ seconds}$.

#### Step 2: Calculate the fly's total distance

Now we look at the fly. We don't care about the zigzags or the changing directions. We only care about two facts:

1. The fly is moving at a constant speed of $2\text{ m/s}$.
2. The fly is moving for exactly $10\text{ seconds}$ (before the bike crashes).

**Formula for Distance:**
$$d = \text{Speed} \cdot \text{Time}$$

**Calculation for the Fly:**
$$d = 2\text{ m/s} \cdot 10\text{ seconds}$$
$$d = 20\text{ meters}$$

---

### 3. Final Answer

The total distance the fly travels before the bicycle hits the wall is **$20\text{ meters}$**.

---

## Problem 8: Definite Integrals

### 1. Problem Statement

Calculate the area under the curve of the function:
$$f(x) = \sin(x)$$
from $x = 0$ to $x = \pi$.

---

### 2. Solution and Explanation

**Concept Intuition:**
In calculus, a "definite integral" is the mathematical tool we use to find the exact area underneath a curve between two specific points. Since $f(x) = \sin(x)$ creates a repeating wave, asking for the area from $0$ to $\pi$ is exactly like asking for the size of one complete "arch" or "bump" of that wave sitting right above the horizontal axis.

To solve this, we find the **antiderivative** (the mathematical opposite of a derivative) and then subtract the value at our starting point from the value at our ending point.

#### Step 1: Set up the integral

We write the area as a definite integral with a lower limit of $0$ and an upper limit of $\pi$.

$$\text{Area} = \int_{0}^{\pi} \sin(x) \, dx$$

#### Step 2: Find the antiderivative

We need to ask ourselves: "What function, when I take its derivative, gives me $\sin(x)$?"
The rule from Calculus tells us the antiderivative of $\sin(x)$ is $-\cos(x)$.

$$\text{Area} = \left[ -\cos(x) \right]_{0}^{\pi}$$

#### Step 3: Evaluate at the limits (Top minus Bottom)

The rule for definite integrals is to plug the top number ($\pi$) into our new function, and subtract the result of plugging the bottom number ($0$) into it.

$$\text{Area} = (-\cos(\pi)) - (-\cos(0))$$

#### Step 4: Calculate the trigonometric values

From trigonometry and the unit circle, we know these exact values:

- $\cos(\pi) = -1$
- $\cos(0) = 1$

Substitute these numbers back into our equation:
$$\text{Area} = (-(-1)) - (-(1))$$
$$\text{Area} = (1) - (-1)$$
$$\text{Area} = 1 + 1$$
$$\text{Area} = 2$$

---

### 3. Final Answer

The exact area under the sine curve from $x = 0$ to $x = \pi$ is exactly **$2$**.

---

## Problem 9: Optimization Problem

### 1. Problem Statement

A rectangle is under the curve:
$$y = 3 - x^2$$
in the first quadrant. What are the dimensions of the rectangle with the maximum area?

---

### 2. Solution and Explanation

**Concept Intuition:**
We want to draw the biggest possible rectangle tucked between the x-axis, the y-axis, and our curve.

- If we make the rectangle too wide (large $x$), it gets very short because it hits the curve closer to the ground.
- If we make it too narrow (small $x$), it gets tall, but its width is too small to have a good area.

To find the perfect balance, we have to write a formula for the Area, and then use Calculus (a derivative) to find the exact peak of that Area function.

#### Step 1: Define the Area Function

The formula for the area of any rectangle is:
$$\text{Area} = \text{width} \cdot \text{height}$$

Looking at the coordinate plane:

- The width of the rectangle is just the distance along the x-axis, which we call $x$.
- The height of the rectangle is determined by the curve, which is $y = 3 - x^2$.

Substitute these into the Area formula:
$$A(x) = x \cdot (3 - x^2)$$

Multiply the $x$ through the parentheses to expand it:
$$A(x) = 3x - x^3$$

#### Step 2: Take the Derivative

Just like in Problem 6, we want to find the maximum point. In Calculus, the maximum point of a curve happens exactly where the "slope" (the derivative) is flat, or zero.

We take the derivative of our area function, $A(x)$. The rule is to multiply by the exponent and drop the exponent by one:

- The derivative of $3x$ is $3$.
- The derivative of $-x^3$ is $-3x^2$.

$$A'(x) = 3 - 3x^2$$

#### Step 3: Set the Derivative to Zero

To find the peak, we set the derivative equal to zero and solve for $x$.

$$0 = 3 - 3x^2$$

Move the $3x^2$ to the other side:
$$3x^2 = 3$$

Divide both sides by 3:
$$x^2 = 1$$

Take the square root:
$$x = 1$$
_(Note: We only use the positive $+1$ because the problem states the rectangle is in the first quadrant, where $x$ is positive)._

#### Step 4: Find the Height

Now we know the perfect width is $x = 1$. To find the corresponding height, we plug this $x$ value back into our original height equation (the curve).

$$y = 3 - x^2$$
$$y = 3 - (1)^2$$
$$y = 3 - 1$$
$$y = 2$$

---

### 3. Final Answer

To achieve the maximum possible area, the dimensions of the rectangle must be:

- **Width ($x$):** $1$ unit
- **Height ($y$):** $2$ units
  _(The maximum area itself would be $1 \cdot 2 = 2$ square units)._

---

## Problem 10: Infinite Series - The Ant's Path

### 1. Problem Statement

Determine the final position of an ant that starts at the origin $(0,0)$ and moves according to the following pattern: $1\text{ m}$ east, $1/2\text{ m}$ north, $1/3\text{ m}$ west, $1/4\text{ m}$ south, $1/5\text{ m}$ east, and so on.

---

### 2. Solution and Explanation

**Concept Intuition:**
Trying to map a spiral with infinite steps is incredibly difficult. Instead, we use the same logic we use for vectors: we separate the horizontal ($x$) movements from the vertical ($y$) movements.

- East is positive $x$, West is negative $x$.
- North is positive $y$, South is negative $y$.

#### Step 1: Isolate the Horizontal ($x$) Position

Let's list only the movements along the $x$-axis (East and West):

- Move 1: $1\text{ m}$ East ($+1$)
- Move 3: $1/3\text{ m}$ West ($-1/3$)
- Move 5: $1/5\text{ m}$ East ($+1/5$)
- Move 7: $1/7\text{ m}$ West ($-1/7$)

If we write this as an endless pattern, it looks like this:
$$x = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \dots$$

In calculus, this specific alternating pattern of odd fractions is very famous. It is called the **Leibniz formula**. Mathematicians have proven that if you let this pattern run forever, it perfectly equals:
$$x = \frac{\pi}{4}$$

#### Step 2: Isolate the Vertical ($y$) Position

Now let's list only the movements along the $y$-axis (North and South):

- Move 2: $1/2\text{ m}$ North ($+1/2$)
- Move 4: $1/4\text{ m}$ South ($-1/4$)
- Move 6: $1/6\text{ m}$ North ($+1/6$)
- Move 8: $1/8\text{ m}$ South ($-1/8$)

Written as an endless pattern:
$$y = \frac{1}{2} - \frac{1}{4} + \frac{1}{6} - \frac{1}{8} + \dots$$

To make this easier to recognize, we can divide the entire pattern by $2$ (or factor out a $1/2$):
$$y = \frac{1}{2} \cdot \left(1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \dots \right)$$

The pattern inside the parentheses is another famous formula called the **Alternating Harmonic Series**. It is a known mathematical rule that this specific sequence always equals the natural logarithm of 2, written as $\ln(2)$.

So, we substitute that back in:
$$y = \frac{1}{2} \cdot \ln(2)$$

---

### 3. Final Answer

After an infinite number of steps, the ant comes to a complete stop at the exact coordinates:
$$(x, y) = \left( \frac{\pi}{4}, \frac{\ln(2)}{2} \right)$$
