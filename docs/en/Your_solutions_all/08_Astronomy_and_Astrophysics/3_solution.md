# Problem 3: Microgravity

### 1. Problem Statement

What is the acceleration due to gravity ($g$) at the altitude of the ISS ($400\text{ km}$)? Why do astronauts experience a state of "weightlessness" despite this gravity?

---

### 2. Solution and Explanation

**Concept Intuition:**
There is a massive public misconception that there is "zero gravity" in space. In reality, gravity reaches everywhere! The International Space Station is relatively close to Earth, so the pull of gravity up there is actually still incredibly strong. 

We can calculate exactly how strong it is using Newton's law of universal gravitation. 

#### Step 1: Calculate the Acceleration Due to Gravity
The formula to find the acceleration due to gravity ($g$) at a certain distance is:
$$g = \frac{G \cdot M_E}{r^2}$$
*(In words: The gravity is equal to the Gravitational constant multiplied by the Mass of the Earth, and then that result is divided by the square of the total orbital radius).*

Just like in Problem 2, we must use the **total radius** from the center of the Earth to the ISS (Earth's radius + altitude), converted into meters: 
$r = 6,378\text{ km} + 400\text{ km} = 6,778\text{ km} = 6,778,000\text{ m}$.

Now, we plug in our numbers:
*   $G = 6.674 \times 10^{-11}\text{ m}^3\text{/(kg}\cdot\text{s}^2)$
*   $M_E = 5.97 \times 10^{24}\text{ kg}$

$$g = \frac{(6.674 \times 10^{-11}) \cdot (5.97 \times 10^{24})}{(6,778,000)^2}$$
$$g = \frac{3.984 \times 10^{14}}{4.594 \times 10^{13}}$$
$$g \approx 8.67\text{ m/s}^2$$

Gravity on the surface of the Earth is $9.81\text{ m/s}^2$. This means that at the altitude of the ISS, gravity is still about **88% as strong** as it is on the ground!

#### Step 2: Explain "Weightlessness"
If gravity is still 88% as strong, why do the astronauts float around? 

The sensation of "weight" does not actually come from gravity pulling you down—it comes from the floor pushing *up* against your feet (this is called the **Normal Force**). 

The astronauts and the ISS are actually falling towards the Earth constantly! However, as we calculated in Problem 2, the ISS is moving sideways at a blistering **$7.67\text{ km/s}$**. Because they are moving forward so incredibly fast, the spherical surface of the Earth curves away from beneath them at the exact same rate that they fall. 

They are in a perpetual state of **free-fall**. Because the spaceship is falling at the exact same speed as the astronauts inside it, the floor never pushes up against their feet. Without that upward push, their brains perceive a state of total weightlessness!

---

### 3. Final Answer

*   **Gravity at ISS Altitude:** $g \approx 8.67\text{ m/s}^2$
*   **Why they float:** They are not experiencing "zero gravity"; they are experiencing **continuous free-fall**. Their massive sideways velocity causes them to continuously fall *around* the curvature of the Earth without ever hitting it. Without a solid surface pushing back up against them, they feel weightless.
