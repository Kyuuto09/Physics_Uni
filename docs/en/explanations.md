# Electromagnetism 1 - Presentation Explanations

*A reference sheet so you can explain the solutions naturally without sounding like you are reading a script.*

<br><br>

# PROBLEM 1: Coulomb's Law

**The Core Concept:**
*   **Analogy:** Imagine four people in the corners of a square room, uniformly pulling on you with ropes.
*   **Result:** You don't move. Every pull from one corner is canceled by the opposite corner. This is symmetry.

**Part A: Mathematical Symmetry:**
*   We can prove this using Coulomb's Law: $F = k \frac{|q_1 q_2|}{r^2}$ *($F$ is the electric force, $k$ is Coulomb's constant, $q_1$ and $q_2$ are the two charges, and $r$ is the distance).*
*   Notice that for all four corners, the distance to the center ($r$) and the corner charges ($+1.0\text{ C}$) are exactly the same.
*   Because the values match, the top-left force ($\vec{F}_{TL}$) is equal and opposite to the bottom-right force ($\vec{F}_{BR}$). Mathematically, this means $\vec{F}_{TL} = -\vec{F}_{BR}$.

**Part B: Finding the Net Force:**
*   To find the net force, we use the Superposition Principle and sum all vectors together: $\vec{F}_{net} = \vec{F}_{TL} + \vec{F}_{BR} + \vec{F}_{TR} + \vec{F}_{BL}$ *(We just mathematically add the four corner forces together).*
*   Since the opposite corners cancel each other out, the equation collapses to $0 + 0 = 0 \text{ N}$.

<br><br>
***
<br><br>

# PROBLEM 2: Electric Potential

**The Core Concept:**
*   **Analogy:** Unlike electric force, electric potential is a scalar quantity. It acts like temperature in a room.
*   **Result:** If you place heaters in the corners of a room, the temperature in the center is just the sum of all of them. You don't have to worry about vectors canceling out; you just add the numbers.

**Part A: Distance to the Center:**
*   First, we find the distance $r$ from the corner to the center.
*   Applying the Pythagorean theorem on the 1-meter square, the full diagonal is $\sqrt{2}$. 
*   We only go half-way to the center, so our distance $r$ is $\frac{\sqrt{2}}{2}$ meters. Since it is a square, this distance is the same for every corner.

**Part B: The Principle of Superposition:**
*   To calculate the total voltage $V_{net}$, we use the point-charge potential formula $V = k\frac{q}{r}$ *(where $V$ is electric potential, $k$ is Coulomb's constant, $q$ is the charge, and $r$ is the distance).*
*   Because the distance $r$ and Coulomb's constant $k$ are the same for every term, we can factor them out to simplify the calculation.
*   The equation reduces to $V_{net} = \frac{k}{r} (q_1 + q_2 + q_3 + q_4)$ *(We multiply the constant $\frac{k}{r}$ by the simple sum of all four corner charges).*

**Part C: Calculating the Final Value:**
*   When we add our given charges ($+1, -2, +3,$ and $-4$), they sum to a net charge of $-2\text{ C}$.
*   Plugging $-2$ into our factored equation results in a negative potential of roughly $-2.54 \times 10^{10} \text{ V}$.

<br><br>
***
<br><br>

# PROBLEM 3: Electrostatic Equilibrium

**The Core Concept:**
*   **Analogy:** Imagine standing between two people trying to push you away. The $+9\text{C}$ person pushes much harder than the $+4\text{C}$ person. 
*   **Result:** To balance the two pushing forces, you must stand much closer to the weaker $+4\text{C}$ person, and further away from the stronger $+9\text{C}$ person. 

**Part A: Setting up the Forces:**
*   We let the unknown distance to the weaker $+4\text{C}$ charge be $x$.
*   Since the total gap is 2 meters, the distance to the stronger $+9\text{C}$ charge has to be $(2 - x)$.
*   To find equilibrium, we set the two forces equal to each other: $k \frac{|q_1 q_3|}{x^2} = k \frac{|q_2 q_3|}{(2 - x)^2}$ *(We set the electric force formula of the left charge equal to the formula of the right charge).*

**Part B: Simplifying and Solving:**
*   Notice how we can cross out the constant $k$ and the test charge $q_3$ from both sides of the equation. This demonstrates that the size of the test charge doesn't matter when finding the balance point.
*   After plugging in our $+4$ and $+9$ charges, we can take the square root of both sides to get rid of the squared numbers. This leaves us with $\frac{2}{x} = \frac{3}{2 - x}$ *(We divide 2 by $x$, and set it equal to 3 divided by $2-x$).*
*   From here, we cross multiply to finish the algebra: $2(2 - x) = 3x$ *(We multiply 2 by $(2-x)$ and set it equal to 3 times $x$),* which solves to our position $x = 0.8 \text{ m}$.

<br><br>
***
<br><br>

# PROBLEM 4: Force Comparison

**The Core Concept:**
*   **Analogy:** This problem demonstrates why chemistry and subatomic physics often ignore gravity. Electromagnetic force and gravity are both inverse-square laws. 
*   **Result:** However, the electric force is so much stronger than gravity that gravity essentially has no effect on a proton and an electron.

**Part A, B & C: The Two Forces:**
*   We set up Coulomb's Law for electric force ($F_e = k\frac{q_1 q_2}{r^2}$) and Newton's Universal Law of Gravitation ($F_g = G\frac{m_1 m_2}{r^2}$).
*   By plugging in the standard constants for mass and charge, we calculate that the electric attraction is $8.19 \times 10^{-8} \text{ N}$, but the gravitational attraction is much smaller at $3.61 \times 10^{-47} \text{ N}$.

**Part D: The Force Ratio:**
*   To compare the forces, we divide them to find their ratio *($F_e / F_g$).*
*   The math shows that the electric force is $10^{39}$ times stronger than gravity.
*   Notice how algebraically, the distance fraction $r^2$ cancels out of the ratio equation. This indicates that it does not matter how far apart the electron and proton are; the electric pull is always $10^{39}$ times stronger.

<br><br>
***
<br><br>

# PROBLEM 5: Field Levitation

**The Core Concept:**
*   **Analogy:** Levitation means an object is not falling down. To prevent an object from falling, a force must push it up with the same strength that gravity pulls it down.
*   **Result:** Instead of a table holding the proton up, we use an electric field to push it upwards against gravity. Since a proton has a positive charge, the electric field must point straight up to push it up.

**Part A: Setting up the Balance:**
*   To achieve levitation, the upward Electric Force ($F_e$) must cancel out the downward Gravitational Force ($F_g$).
*   We set the two equations equal to each other: $qE = mg$ *($q$ is charge, $E$ is electric field, $m$ is mass, $g$ is gravity. We multiply the charge by the electric field, and set it equal to mass times gravity).*

**Part B: Solving for the Electric Field:**
*   We want to find the strength of the electric field ($E$), so we isolate $E$ to get $E = \frac{mg}{q}$ *(We multiply mass by gravity, and then divide by the charge $q$).*

**Part C: Calculating the Value:**
*   We plug in the standard mass and charge for a proton, along with Earth's gravity ($9.8 \text{ m/s}^2$).
*   The result is an electric field of $1.02 \times 10^{-7} \text{ N/C}$.
*   This is a very small number. Because the proton's mass is so small, it takes very little electric force to hold it up against gravity.

<br><br>
***
<br><br>

# PROBLEM 6: Field at a Point from Multiple Charges

**The Core Concept:**
*   **Analogy:** Instead of forces pushing strictly along a 1D line, we are evaluating forces in a 2D plane. We have to sum up multiple 2D vectors.
*   **Result:** The total electric field at any point is simply the vector sum of the electric field from the first charge and the electric field from the second charge.

**Part 1: Establishing the Vectors:**
*   We use coordinates to build distance vectors from each charge directly to our test point $P(x,y)$.
*   By substituting these distance vectors into the general electric field formula $\vec{E} = k \frac{q}{R^3}\vec{R}$ *($\vec{E}$ is the electric field vector, $k$ is the constant, $q$ is charge, $\vec{R}$ is the distance vector, and $R^3$ is the distance cubed),* we generate our full equation.

**Part 2: Conditions for Zero Field:**
*   By analyzing the $y$-component of our equation, we see that $E_y$ is only zero when you are flat on the x-axis ($y=0$).
*   To find where the entire field is exactly zero ($\vec E = 0$), we look along the x-axis between the two charges. We set the opposing forces equal, just like we did in Problem 3.
*   The math shows the zero-field point rests slightly closer to the weaker $+q$ charge, at roughly $x = -0.17a$.

**Part 3: Numerical Calculation:**
*   We plug the given values ($a = 0.2\text{ m}$, $y = 0.3\text{ m}$) directly into the specific axis equations we mathematically derived in Part 1. 
*   This gives us the final physical components of the force vector.

**Part 4: The Limit ($y \gg a$):**
*   This part asks what happens if we observe from very far away ($y$ is much larger than $a$).
*   By approximating our equations for large distances, the field simplifies to $\vec E \approx k \frac{3q}{y^2} \hat{j}$ *(We multiply Coulomb's constant $k$ by the combined charge $3q$, and divide by the large distance squared $y^2$).*
*   This final equation means that from far away, the two separate $+q$ and $+2q$ charges blur together and mathematically act like a single point charge of $+3q$.

<br><br>
***
<br><br>

# PROBLEM 7: Cyclotron Motion

**The Core Concept:**
*   **Analogy:** This problem shows how particle accelerators work. First, an electric field forces an electron to speed up in a straight line. Then, a magnetic field grabs it and forces it to travel in a circle.
*   **Result:** The Lorentz force from a magnetic field pushes perpendicular to the particle's movement. It acts like a string holding a spinning ball; it forces the electron into a circular orbit without speeding it up or slowing it down.

**Part A: Electric Acceleration:**
*   The electric voltage converts potential energy into kinetic energy. We write this balance as $eV = \frac{1}{2}m_ev^2$ *($e$ is electron charge, $V$ is voltage, $m_e$ is mass, and $v$ is velocity).*
*   We algebraicaly solve this equation to isolate the velocity $v$.

**Part B: The Magnetic Circle:**
*   Once inside the magnetic field, the magnetic Lorentz force $F_B = evB$ *(charge times velocity times magnetic field)* acts as the centripetal force ($F_c = \frac{m_ev^2}{R}$), keeping the electron in a circle.
*   We set these equal: $evB = \frac{m_ev^2}{R}$.
*   We cancel one $v$ from each side and solve for the radius $R$, giving us $R = \frac{m_ev}{eB}$ *(To find radius $R$, we multiply mass and velocity, then divide by the charge times the magnetic field).*

**Part C & D: Algebraic Combination and Calculation:**
*   Rather than calculating intermediate speeds, we substitute our velocity equation from Part A directly into our radius equation.
*   We plug in the standard mass and charge for an electron, along with the given 5000 V and 0.1 T.
*   The math gives a radius of $2.39 \times 10^{-3} \text{ m}$, which equates to 2.39 millimeters.

<br><br>
***
<br><br>

# PROBLEM 8: Lorentz Force

**The Core Concept:**
*   **Analogy:** Unlike gravity or electric forces that push and pull directly between objects, the magnetic Lorentz Force has a unique property: it only pushes sideways. 
*   **Result:** A magnetic field only affects particles that are moving. When a particle enters the field, the force pushes it perpendicular to the direction it is traveling.

**Part A: Application of the Lorentz Formula:**
*   We calculate the magnitude of the magnetic force using the equation: $F_L = |q|vB \sin(\theta)$ *($F_L$ is the Lorentz force, $q$ is charge, $v$ is speed, $B$ is the magnetic field, and $\theta$ is the angle. We multiply all these together).*

**Part B: The Perpendicular Effect:**
*   The problem states that the particle enters perpendicular to the magnetic field. This means the angle $\theta$ is $90^\circ$.
*   Since $\sin(90^\circ) = 1$, the particle experiences the maximum possible force, reducing our formula to $F_L = |q|vB$ *(We just multiply the absolute charge, speed, and magnetic field together).*

**Part C: Complete Numerical Calculation:**
*   We substitute the provided numbers into our equation: $q = 2 \times 10^{-19} \text{ C}$, $v = 10^6 \text{ m/s}$, and $B = 0.5 \text{ T}$.
*   When we multiply these together, we get a final magnetic force of $1 \times 10^{-13} \text{ N}$.
*   Notice that we did not use the given mass of the particle. The mass is irrelevant for finding the force itself; it is only needed if we want to calculate the resulting acceleration using $F=ma$.

<br><br>
***
<br><br>

# PROBLEM 9: Vector Lorentz Force

**The Core Concept:**
*   **Analogy:** In previous problems, the velocity and magnetic field were given as perpendicular, allowing us to simply multiply the numbers. Here, they are 3D vectors pointing in complex diagonal directions.
*   **Result:** To find the exact part of the velocity that is perpendicular to the magnetic field, we use the vector cross product ($\vec{v} \times \vec{B}$). This automatically calculates both the force magnitude and its 3D direction.

**Part A: The Cross Product Setup:**
*   We use the vector Lorentz force equation: $\vec{F} = q (\vec{v} \times \vec{B})$ *($\vec{F}$ is the force vector. We mathematically take the cross product of the velocity vector $\vec{v}$ and magnetic field vector $\vec{B}$, then multiply by the charge $q$).*
*   We calculate the cross product using a standard matrix determinant setup with our given $\vec{v}$ and $\vec{B}$ vectors.
*   Expanding the matrix gives us the resulting direction vector: $2\hat{i} + 3\hat{j} + 8\hat{k}$.

**Part B & C: The Full Force Vector and Magnitude:**
*   We multiply this resulting vector by the standard charge of a proton ($1.6 \times 10^{-19} \text{ C}$) to get the final exact force vector.
*   Since the problem asks for the absolute magnitude of this force, we apply the 3D Pythagorean theorem: $\sqrt{F_x^2 + F_y^2 + F_z^2}$ *(We square each of the three $x, y, z$ direction values, add them together, and take their square root).*
*   We calculate the magnitude of the cross product vector as $\sqrt{77}$ (or about $8.775$), and then multiply by the proton charge.
*   This gives a final force magnitude of $1.404 \times 10^{-18} \text{ N}$.

<br><br>
***
<br><br>

# PROBLEM 10: Lorentz Force on a Wire

**The Core Concept:**
*   **Analogy:** Instead of tracking a single microscopic particle, we look at a solid wire carrying billions of electrons as a steady current ($I$).
*   **Result:** The formula for a long wire is structurally identical to the single-particle formula. The formula is $F = I L B \sin(\theta)$ *($F$ is force, $I$ is current, $L$ is explicitly the length of the wire, $B$ is the magnetic field, and $\theta$ is the angle. We multiply all of them together).*

**Part A, B & C: Evaluating the Angles:**
*   We can pre-calculate the constants before looking at the angles: $I \cdot L \cdot B = 10 \text{ A} \cdot 2.0 \text{ m} \cdot 0.5 \text{ T} = 10 \text{ N}$.
*   **For $90^\circ$ (Perpendicular):** Since $\sin(90^\circ) = 1$, the wire experiences the maximum force possible. The result is exactly $10 \text{ N}$.
*   **For $45^\circ$ (Angled):** Some of the current isn't positioned perfectly against the magnetic field. With $\sin(45^\circ) = \frac{\sqrt{2}}{2}$, the force reduces to $5\sqrt{2} \text{ N}$ (or $7.07 \text{ N}$).
*   **For $0^\circ$ (Parallel):** The current moves exactly in the same direction as the magnetic field. Because $\sin(0^\circ) = 0$, the magnetic field ignores the wire entirely, resulting in $0 \text{ N}$ of force.
