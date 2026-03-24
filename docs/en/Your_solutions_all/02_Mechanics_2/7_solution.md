# Problem 7: Dynamics with Friction

### 1. Problem Statement

A 5 kg block is placed on a 10 kg block. A horizontal force of 45 N is applied to the 10 kg block, and the 5 kg block is tied to the wall. The coefficient of kinetic friction between all moving surfaces is 0.2. Find the acceleration of the 10 kg block.

---

### 2. Solution and Explanation

**Concept Intuition:**
This problem is about accounting for all the forces resisting movement. Because the top 5 kg block is tied to the wall, it stays perfectly still while the 10 kg block is dragged out from underneath it. 

This means the 10 kg block is scraping against **two** different surfaces at the same time:
1.  **The Top Friction:** The friction between the top of the 10 kg block and the bottom of the 5 kg block.
2.  **The Bottom Friction:** The friction between the bottom of the 10 kg block and the floor.

To find the acceleration, we need to calculate both of these frictional forces, subtract them from the 45 N pull to find the "Net Force", and then use Newton's Second Law ($F = ma$).

#### Step 1: Calculate the Top Friction ($f_{k1}$)
Friction is calculated using the formula $f_k = \mu_k \cdot N$, where $N$ is the Normal Force (the weight pressing the surfaces together, $N = mg$).
For the top surface, only the 5 kg block is pressing down.
$$f_{k1} = \mu_k \cdot (m_1 \cdot g)$$
$$f_{k1} = 0.2 \cdot (5 \cdot 9.81)$$
$$f_{k1} = 0.2 \cdot 49.05$$
$$f_{k1} = 9.81 \text{ N}$$

#### Step 2: Calculate the Bottom Friction ($f_{k2}$)
For the friction against the floor, the floor has to support the weight of **both** blocks pushing down. 
$$f_{k2} = \mu_k \cdot (m_{total} \cdot g)$$
$$f_{k2} = 0.2 \cdot ((5 + 10) \cdot 9.81)$$
$$f_{k2} = 0.2 \cdot (15 \cdot 9.81)$$
$$f_{k2} = 0.2 \cdot 147.15$$
$$f_{k2} = 29.43 \text{ N}$$

#### Step 3: Find the Net Force ($F_{net}$)
The total pulling force is 45 N forward. The two friction forces are pulling backward.
$$F_{net} = F_{applied} - f_{k1} - f_{k2}$$
$$F_{net} = 45 - 9.81 - 29.43$$
$$F_{net} = 45 - 39.24$$
$$F_{net} = 5.76 \text{ N}$$

#### Step 4: Calculate the Acceleration ($a$)
Now we use Newton's Second Law for the 10 kg block.
$$F_{net} = m_2 \cdot a$$
$$5.76 = 10 \cdot a$$

Divide both sides by 10:
$$a = \frac{5.76}{10}$$
$$a = 0.576 \text{ m/s}^2$$

---

### 3. Final Answer

- **Acceleration of the 10 kg block:** $0.576 \text{ m/s}^2$