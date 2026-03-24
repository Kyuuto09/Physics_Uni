# Problem 1: Gravitational Dependence

### 1. Problem Statement

A simple pendulum has a period of 4 seconds on Earth. What would its period be on the Moon, where the gravitational acceleration is about 1/6th of Earth's?

What is the required length of a simple pendulum to have a period of exactly 1 second on Earth?

---

### 2. Solution and Explanation

**Concept Intuition:**
The time it takes for a pendulum to swing back and forth one time is called its "period". This time depends entirely on two physical things: the length of the string ($L$) and how hard gravity is pulling down ($g$). It actually does _not_ matter how heavy the weight at the bottom is!

The standard formula for the period of a pendulum is:
$$T = 2\pi \sqrt{\frac{L}{g}}$$

#### Part 1: Period on the Moon

We know the period on Earth is 4 seconds. The gravity on the Moon ($g_M$) is $\frac{1}{6}$ of the gravity on Earth ($g_E$).

Instead of trying to find the exact length of the string, we can use a "cheat code" by setting up a ratio. Let's write the formula for the Moon:
$$T_M = 2\pi \sqrt{\frac{L}{\frac{g_E}{6}}}$$

Using basic fraction rules, dividing by a fraction is the same as multiplying by its reciprocal, so that 6 flips up to the top:
$$T_M = 2\pi \sqrt{\frac{6L}{g_E}}$$

Now, we pull the $\sqrt{6}$ out to the front:
$$T_M = \sqrt{6} \cdot \left( 2\pi \sqrt{\frac{L}{g_E}} \right)$$

Notice that the piece inside the parentheses is the exact formula for the period on Earth, which we already know is 4 seconds! So we just replace that whole chunk with 4:
$$T_M = \sqrt{6} \cdot 4$$
$$T_M \approx 2.449 \cdot 4$$
$$T_M \approx 9.8 \text{ seconds}$$

Because gravity is weaker, the pendulum falls much slower, taking more than twice as long to complete a swing.

#### Part 2: Length for a 1-Second Period on Earth

Here, we are working backward. We know the exact time we want ($T = 1$ second), and we know the Earth's standard gravity ($g \approx 9.81$ m/s²). We just need to use algebra to isolate the length ($L$).

Start with the formula:
$$T = 2\pi \sqrt{\frac{L}{g}}$$

1. Plug in our known numbers:
   $$1 = 2\pi \sqrt{\frac{L}{9.81}}$$

2. Divide both sides by $2\pi$:
   $$\frac{1}{2\pi} = \sqrt{\frac{L}{9.81}}$$

3. Square both sides to break the $L$ out of the square root:
   $$\left(\frac{1}{2\pi}\right)^2 = \frac{L}{9.81}$$
   $$\frac{1}{4\pi^2} = \frac{L}{9.81}$$

4. Multiply both sides by 9.81 to get $L$ completely by itself:
   $$L = \frac{9.81}{4\pi^2}$$

5. Calculate the final value (using $\pi \approx 3.14159$):
   $$L \approx \frac{9.81}{39.48}$$
   $$L \approx 0.248 \text{ meters}$$

---

### 3. Final Answers

- **Period on the Moon:** $\approx 9.8 \text{ seconds}$
- **Required Length on Earth:** $\approx 0.248 \text{ meters}$ (or 24.8 cm)
