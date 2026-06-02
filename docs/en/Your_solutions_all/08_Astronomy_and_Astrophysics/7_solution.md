# Problem 7: Megastructures (Dyson Sphere)

### 1. Problem Statement

A "Dyson Sphere" is a hypothetical megastructure that completely encompasses a star to capture its energy output. If the mass of Mercury ($3.3 \times 10^{23}\text{ kg}$) were used to build a solar panel sphere with a surface density of $10\text{ kg/m}^2$, what would be the radius of the sphere?

---

### 2. Solution and Explanation

**Concept Intuition:**
A Dyson Sphere is the ultimate science fiction power plant—a giant shell built completely around a star to collect 100% of its sunlight. But where would you get the material to build something so impossibly massive? A common trope is to dismantle an entire planet (like Mercury) and flatten it out into ultra-thin solar panels. 

We can figure out how big this sphere would be by converting the planet's mass into total surface area, and then working backward to find the radius of a sphere with that exact surface area.

#### Step 1: Calculate the Total Surface Area
First, we need to know the total area ($A$) of solar panels we can build out of Mercury. We know the total mass ($M = 3.3 \times 10^{23}\text{ kg}$) and the surface density ($\sigma = 10\text{ kg/m}^2$), which tells us that every square meter of solar panel weighs 10 kg.

$$A = \frac{M}{\sigma}$$
*(In words: The total area is equal to the total mass of the planet divided by the surface density).*

$$A = \frac{3.3 \times 10^{23}\text{ kg}}{10\text{ kg/m}^2}$$
$$A = 3.3 \times 10^{22}\text{ m}^2$$

We now have enough material to build $3.3 \times 10^{22}$ square meters of solar panels!

#### Step 2: Calculate the Radius of the Sphere
The geometric formula for the surface area of a sphere is $A = 4 \pi R^2$. Since we already know the Area, we need to algebraically rearrange this formula to solve for the Radius ($R$):

$$R = \sqrt{\frac{A}{4\pi}}$$
*(In words: The radius of the sphere is equal to the square root of the entire result of: the total surface area divided by $4\pi$).*

Let's plug in our massive surface area:
$$R = \sqrt{\frac{3.3 \times 10^{22}}{4 \cdot 3.14159}}$$
$$R = \sqrt{\frac{3.3 \times 10^{22}}{12.566}}$$
$$R \approx \sqrt{2.626 \times 10^{21}}$$
$$R \approx 51,245,000,000\text{ meters}$$

To make this number slightly more readable, let's convert it to kilometers by dividing by 1,000:
**$R \approx 51,245,000\text{ km}$** (or $51.2 \times 10^6\text{ km}$).

*(For astronomical context: Mercury currently orbits the sun at a distance of about $58 \times 10^6\text{ km}$. Therefore, if you dismantled Mercury to build this Dyson sphere, the sphere would fit perfectly inside Mercury's old orbit!)*

---

### 3. Final Answer

*   **Radius of the Dyson Sphere:** $R \approx 51.2 \times 10^6\text{ km}$
