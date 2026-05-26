
# Physics 6 — Presentation Cheat Sheet

*A simple reference sheet for reading out the solutions naturally during class.*

<br><br>

# PROBLEM 1: Series and Parallel Circuit

**Part A: Series Connection**
* In a series circuit, the resistors are connected one after another.
* So we just add them directly:

$$R_{\text{series}} = R_1 + R_2 + R_3$$

*(Equivalent resistance equals resistor 1 plus resistor 2 plus resistor 3.)*

$$R_{\text{series}} = 15 + 30 + 50 = 95\,\Omega$$

* Then use Ohm’s law to find the current:

$$I_{\text{series}} = \frac{V}{R_{\text{series}}}$$

*(Current equals voltage divided by resistance.)*

$$I_{\text{series}} = \frac{12}{95} \approx 0.126\,\text{A}$$

**Part B: Parallel Connection**
* In parallel, the reciprocal values add:

$$\frac{1}{R_{\text{parallel}}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3}$$

*(One over the total resistance equals one over each resistor added together.)*

$$\frac{1}{R_{\text{parallel}}} = \frac{1}{15} + \frac{1}{30} + \frac{1}{50} = \frac{18}{150}$$

$$R_{\text{parallel}} = \frac{150}{18} = \frac{25}{3} \approx 8.33\,\Omega$$

* Then the current is:

$$I_{\text{parallel}} = \frac{V}{R_{\text{parallel}}} = \frac{12}{25/3} = 1.44\,\text{A}$$

**Final Answers:**
* Series: $R = 95\,\Omega$, $I \approx 0.126\,\text{A}$
* Parallel: $R \approx 8.33\,\Omega$, $I = 1.44\,\text{A}$

<br><br>
***

<br><br>

# PROBLEM 2: Resistors Combinations

**Core Idea:**
* With three identical $1\,\Omega$ resistors, we list every unique way to connect them.
* The possible equivalent resistances come from only four distinct arrangements.

**Configuration 1: All in Series**
$$R_{\text{eq}} = 1 + 1 + 1 = 3\,\Omega$$
*(In series, resistances simply add.)*

**Configuration 2: All in Parallel**
$$\frac{1}{R_{\text{eq}}} = 1 + 1 + 1 = 3$$
$$R_{\text{eq}} = \frac{1}{3}\,\Omega$$
*(In parallel, the reciprocals add.)*

**Configuration 3: Two in Series, then Parallel with the Third**
$$R_{\text{branch}} = 1 + 1 = 2\,\Omega$$
*(First combine the two series resistors.)*

$$\frac{1}{R_{\text{eq}}} = \frac{1}{2} + 1 = \frac{3}{2}$$
$$R_{\text{eq}} = \frac{2}{3}\,\Omega$$

**Configuration 4: Two in Parallel, then Series with the Third**
$$R_{\text{block}} = \left(\frac{1}{1} + \frac{1}{1}\right)^{-1} = \frac{1}{2}\,\Omega$$
*(First combine the parallel pair.)*

$$R_{\text{eq}} = R_{\text{block}} + 1 = \frac{1}{2} + 1 = \frac{3}{2}\,\Omega$$

**Final Answer:**
The unique values are:

$$\frac{1}{3}\,\Omega,\quad \frac{2}{3}\,\Omega,\quad \frac{3}{2}\,\Omega,\quad 3\,\Omega$$

<br><br>
***

<br><br>

# PROBLEM 3: Mixed Circuit

**Part 1: Identify the Main Connections**
* The easiest way is to break the circuit into smaller pieces.
* We first find the parts that are clearly in series or parallel.

**Part 2: Simplify the Inner Parallel Pair**
* The two resistors in the small branch are in parallel:

$$R_{\parallel} = \frac{5 \cdot 5}{5 + 5} = 2.5\,\Omega$$

*(Parallel resistance equals the product divided by the sum.)*

**Part 3: Build the Next Series Path**
* That $2.5\,\Omega$ part is in series with another $5\,\Omega$ resistor:

$$R = 5 + 2.5 = 7.5\,\Omega$$

**Part 4: Combine the Two Paths**
* Now we have two paths between the same nodes: $10\,\Omega$ and $7.5\,\Omega$.
* These are in parallel:

$$\frac{1}{R_{\text{eq}}} = \frac{1}{10} + \frac{1}{7.5}$$

$$R_{\text{eq}} = \frac{30}{7}\,\Omega$$

**Part 5: Add the Final Series Resistor**
* The last resistor on the right is in series with that block:

$$R_{\text{final}} = \frac{30}{7} + 10 = \frac{100}{7}\,\Omega$$

**Part 6: Final Parallel Step**
* Finally, that whole top branch is in parallel with the bottom $5\,\Omega$ resistor:

$$R_{\text{eq}} = \frac{\left(\frac{100}{7}\right)(5)}{\frac{100}{7} + 5} = \frac{100}{27}\,\Omega$$

**Final Answer:**

$$R_{\text{eq}} = \frac{100}{27}\,\Omega \approx 3.70\,\Omega$$

<br><br>
***

<br><br>

# PROBLEM 4: Mixed Circuit

**Part 1: Start from the Inside**
* We again simplify the circuit from the most nested part first.
* The small bottom pair is in parallel.

$$R_{\parallel} = \frac{10 \cdot 10}{10 + 10} = 5\,\Omega$$
*(Equal resistors in parallel give half the value.)*

**Part 2: Add the Series Resistor**
* That $5\,\Omega$ result is in series with another $10\,\Omega$ resistor:

$$R_{\text{bottom}} = 10 + 5 = 15\,\Omega$$

**Part 3: Simplify the Top Branch**
* The top branch has two $10\,\Omega$ resistors in series:

$$R_{\text{top}} = 10 + 10 = 20\,\Omega$$

**Part 4: Combine the Two Main Branches**
* Now the top branch and bottom branch are in parallel:

$$R_{\text{block}} = \frac{20 \cdot 15}{20 + 15} = \frac{60}{7}\,\Omega$$

**Part 5: Add the Final Resistor**
* The resistor on the far right is in series with that block:

$$R_{\text{eq}} = \frac{60}{7} + 10 = \frac{130}{7}\,\Omega$$

**Final Answer:**

$$R_{\text{eq}} = \frac{130}{7}\,\Omega \approx 18.57\,\Omega$$

<br><br>
***

<br><br>

# PROBLEM 5: Kirchhoff’s Laws

**Core Idea:**
* Kirchhoff’s Current Law means current in equals current out at a junction.
* Kirchhoff’s Voltage Law means the total voltage change around a loop is zero.

**Part 1: Choose Current Directions**
* Let $I_1$ go through the left branch.
* Let $I_3$ go through the right branch.
* Let $I_2$ go through the middle resistor.

**Part 2: Apply Current Law**
At the top junction:

$$I_1 + I_3 = I_2$$

*(The two side currents join and go through the middle branch.)*

**Part 3: Left Loop Equation**
Going around the left loop:

$$4.5 - 21I_1 - 10I_2 = 0$$

So:

$$I_1 = \frac{4.5 - 10I_2}{21}$$

**Part 4: Right Loop Equation**
Going around the right loop:

$$9 - I_3 - 10I_2 = 0$$

So:

$$I_3 = 9 - 10I_2$$

**Part 5: Solve for the Middle Current**
Substitute into the current law:

$$\frac{4.5 - 10I_2}{21} + (9 - 10I_2) = I_2$$

This gives:

$$I_2 \approx 0.803\,\text{A}$$

Then:

$$I_1 \approx -0.168\,\text{A}$$

$$I_3 \approx 0.971\,\text{A}$$

**Final Answers:**
* $I_1 \approx -0.168\,\text{A}$
* $I_2 \approx 0.803\,\text{A}$
* $I_3 \approx 0.971\,\text{A}$

<br><br>
***

<br><br>

# PROBLEM 6: Kirchhoff’s Laws Again

**Core Idea:**
* This circuit has three parallel branches.
* We find the ammeter current by writing one current law equation and two voltage loop equations.

**Part 1: Define the Currents**
* Let $I_1$ go left through the top branch.
* Let $I_3$ go left through the bottom branch.
* Let $I_2$ go right through the middle branch.

**Part 2: Apply Current Law**
At Node L:

$$I_1 + I_3 = I_2$$

**Part 3: Top Loop**
Going around the top loop:

$$4.5 - I_1 - 20I_2 = 0$$

So:

$$I_1 = 4.5 - 20I_2$$

**Part 4: Bottom Loop**
Going around the bottom loop:

$$9 - 11I_3 - 20I_2 = 0$$

So:

$$I_3 = \frac{9 - 20I_2}{11}$$

**Part 5: Solve for the Ammeter Current**
Substitute into the current law:

$$\left(4.5 - 20I_2\right) + \frac{9 - 20I_2}{11} = I_2$$

This gives:

$$I_2 = \frac{117}{502}\,\text{A} \approx 0.233\,\text{A}$$

**Final Answer:**

$$I_2 \approx 0.233\,\text{A}$$

<br><br>
***

<br><br>

# PROBLEM 7: Capacitors in Parallel

**Core Idea:**
* Capacitors in parallel act like one bigger capacitor.
* In parallel, capacitances add directly.
* Both capacitors have the same voltage.

**Part 1: Find the Equivalent Capacitance**
$$C_{\text{eq}} = C_1 + C_2 = 4\,\mu\text{F} + 6\,\mu\text{F} = 10\,\mu\text{F}$$

*(Capacitance in parallel is just added.)*

**Part 2: Find the Total Charge**
Use:

$$Q = CV$$

*(Charge equals capacitance multiplied by voltage.)*

$$Q_{\text{total}} = (10\,\mu\text{F})(10\,\text{V}) = 100\,\mu\text{C}$$

**Part 3: Find the Total Energy**
Use:

$$U = \frac{1}{2}CV^2$$

*(Energy equals one-half times capacitance times voltage squared.)*

$$U_{\text{total}} = \frac{1}{2}(10\,\mu\text{F})(10^2) = 500\,\mu\text{J}$$

**Final Answers:**
* Total charge: $100\,\mu\text{C}$
* Total energy: $500\,\mu\text{J}$

<br><br>
***

<br><br>

# PROBLEM 8: AC Voltage Equation

**Core Idea:**
* In a pure resistor, voltage and current are in phase.
* So we can use Ohm’s law at each moment in time:

$$V(t) = I(t)R$$

*(Voltage equals current multiplied by resistance.)*

**Part 1: Substitute the Given Current**
$$I(t) = 2\sin(120\pi t)$$
$$R = 50\,\Omega$$

So:

$$V(t) = \left[2\sin(120\pi t)\right](50)$$

**Part 2: Simplify**
$$V(t) = 100\sin(120\pi t)$$

**Final Answer:**

$$V(t) = 100\sin(120\pi t)\ \text{V}$$

<br><br>
***

<br><br>

# PROBLEM 9: Current from Charge

**Core Idea:**
* Current is the rate at which charge changes with time.
* So we use the derivative:

$$I(t) = \frac{dQ}{dt}$$

*(Current equals the time derivative of charge.)*

**Part 1: Differentiate the Charge Function**
Given:

$$Q(t) = 5t^2 + 5$$

Differentiate:

$$I(t) = \frac{d}{dt}(5t^2+5) = 10t$$

**Part 2: Evaluate at $t=3\text{ s}$**
$$I(3) = 10(3) = 30\,\text{A}$$

**Final Answer:**

$$I = 30\,\text{A}$$

<br><br>
***

<br><br>

# PROBLEM 10: Average Current of a Lightning Bolt

**Core Idea:**
* Average current is total charge divided by total time.

$$I_{\text{avg}} = \frac{Q}{\Delta t}$$

*(Average current equals charge divided by time.)*

**Part 1: Convert the Time**
$$2\,\text{ms} = 2 \times 10^{-3}\,\text{s} = 0.002\,\text{s}$$

**Part 2: Substitute the Values**
$$I_{\text{avg}} = \frac{30}{0.002} = 15000\,\text{A}$$

**Final Answer:**

$$I_{\text{avg}} = 1.5\times 10^4\,\text{A}$$

<br><br>
***

<br><br>

# PROBLEM 11: Power & Energy

**Core Idea:**
* Power tells us how fast energy is used.
* Energy is power times time.

**Part 1: Find the Power**
Use the resistor power formula:

$$P = \frac{V^2}{R}$$

*(Power equals voltage squared divided by resistance.)*

$$P = \frac{50^2}{100} = 25\,\text{W}$$

**Part 2: Find the Energy**
First convert time:

$$5\,\text{min} = 300\,\text{s}$$

Then use:

$$E = Pt$$

*(Energy equals power multiplied by time.)*

$$E = 25 \times 300 = 7500\,\text{J}$$

**Final Answers:**
* Power: $25\,\text{W}$
* Energy: $7500\,\text{J}$

<br><br>
***

<br><br>

# PROBLEM 12: Transformer Currents

**Core Idea:**
* In an ideal transformer, the voltage ratio matches the turns ratio.
* Power is conserved, so if voltage goes down, current goes up.

**Part 1: Find the Secondary Voltage**
Use:

$$\frac{V_s}{V_p} = \frac{N_s}{N_p}$$

*(Secondary voltage over primary voltage equals secondary turns over primary turns.)*

$$V_s = V_p\left(\frac{N_s}{N_p}\right)$$

$$V_s = 120\left(\frac{200}{1000}\right) = 24\,\text{V}$$

**Part 2: Find the Primary Current**
Use power conservation:

$$P_p = P_s$$

$$V_p I_p = V_s I_s$$

*(Power equals voltage times current on both sides.)*

So:

$$I_p = I_s\left(\frac{V_s}{V_p}\right)$$

$$I_p = 3\left(\frac{24}{120}\right) = 0.6\,\text{A}$$

**Final Answers:**
* Secondary voltage: $24\,\text{V}$
* Primary current: $0.6\,\text{A}$

<br><br>
***

<br><br>

# PROBLEM 13: Transformer Ratio

**Core Idea:**
* The transformer voltage ratio equals the turns ratio.

$$\frac{V_s}{V_p} = \frac{N_s}{N_p}$$

*(Voltage ratio equals turns ratio.)*

**Part 1: Solve for the Secondary Turns**
Rearrange:

$$N_s = N_p\left(\frac{V_s}{V_p}\right)$$

Substitute the values:

$$N_s = 400\left(\frac{9.0}{120}\right) = 30$$

**Final Answer:**

$$N_s = 30\ \text{turns}$$

<br><br>
***

<br><br>

# PROBLEM 14: The RLC Circuit and Harmonic Oscillator

**Core Idea:**
* A series RLC circuit behaves like a damped harmonic oscillator.
* The math looks the same, so we compare the terms one by one.

**Part 1: Write the Circuit Equation**
Using Kirchhoff’s Voltage Law:

$$V_L + V_R + V_C = V(t)$$

Where:

$$V_L = L\frac{dI}{dt}$$
$$V_R = RI$$
$$V_C = \frac{Q}{C}$$

And since:

$$I = \frac{dQ}{dt}$$

we get:

$$L\frac{d^2Q}{dt^2} + R\frac{dQ}{dt} + \frac{1}{C}Q = V(t)$$

*(This is the standard RLC differential equation.)*

**Part 2: Write the Mechanical Equation**
For a damped spring-mass system:

$$m\frac{d^2x}{dt^2} + b\frac{dx}{dt} + kx = F(t)$$

**Part 3: Compare the Terms**
* $L \leftrightarrow m$  
  *(inductance acts like mass / inertia)*
* $R \leftrightarrow b$  
  *(resistance acts like damping / friction)*
* $\frac{1}{C} \leftrightarrow k$  
  *(small capacitance acts like a strong spring)*
* $Q \leftrightarrow x$  
  *(charge plays the role of position)*
* $I \leftrightarrow v$  
  *(current plays the role of velocity)*
* $V(t) \leftrightarrow F(t)$  
  *(voltage source plays the role of external force)*

**Final Answer:**
The two equations are:

$$L\frac{d^2Q}{dt^2} + R\frac{dQ}{dt} + \frac{1}{C}Q = V(t)$$

$$m\frac{d^2x}{dt^2} + b\frac{dx}{dt} + kx = F(t)$$

<br><br>
***

<br><br>

# PROBLEM 15: The Resistor Cube

**Core Idea:**
* The cube is perfectly symmetric.
* So the current splits evenly at each stage.

**Part 1: Current Leaving the First Corner**
There are 3 identical paths, so the current splits into thirds:

$$\frac{I}{3}$$

**Part 2: Current in the Middle**
At the next junction, the current splits again into 2 equal paths:

$$\frac{I}{6}$$

**Part 3: Current Entering the Last Corner**
The three final paths each carry:

$$\frac{I}{3}$$

**Part 4: Add the Voltage Drops**
Along one path, the total voltage is:

$$V_{\text{total}} = \frac{IR}{3} + \frac{IR}{6} + \frac{IR}{3} = \frac{5IR}{6}$$

Then:

$$R_{\text{eq}} = \frac{V_{\text{total}}}{I} = \frac{5}{6}R$$

**Final Answer:**

$$R_{\text{eq}} = \frac{5}{6}R$$
