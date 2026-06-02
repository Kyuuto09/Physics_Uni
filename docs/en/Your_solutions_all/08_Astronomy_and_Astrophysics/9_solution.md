# Problem 9: Size and Distance of the Sun (Aristarchus' Method)

### 1. Problem Statement

Aristarchus from Samos attempted to determine the relative distances and sizes of the Sun and the Moon using geometric methods. At exact half-Moon, the Earth–Moon–Sun system forms a right triangle with the right angle at the Moon. 

Given:
*   Angular separation $\theta = 89.85^\circ$
*   Apparent angular diameter $\alpha = 0.53^\circ$
*   Earth–Moon distance $d_{EM} = 3.84 \times 10^5\text{ km}$

Calculate $d_{ES}$, $D_S$, the ratio $D_M / D_S$, and how much $d_{ES}$ changes if Aristarchus' historical angle of $89.75^\circ$ is used instead.

---

### 2. Solution and Explanation

**Concept Intuition:**
Aristarchus realized that when the Moon is exactly half illuminated (a first quarter moon), the angle connecting the Earth, Moon, and Sun must form a perfect $90^\circ$ right angle. By simply measuring the angle between the Sun and Moon in the sky ($\theta$), he could use basic trigonometry to map the entire solar system!

#### Part 1: The Earth-Sun Distance ($d_{ES}$)
If we have a right triangle with the right angle at the Moon, the distance from Earth to the Sun is the hypotenuse. We know the adjacent side ($d_{EM}$) and the angle ($\theta$). Therefore, we use the cosine function.

$$\cos(\theta) = \frac{\text{adjacent}}{\text{hypotenuse}}$$
$$\cos(\theta) = \frac{d_{EM}}{d_{ES}}$$

We rearrange this to solve for $d_{ES}$:
$$d_{ES} = \frac{d_{EM}}{\cos(\theta)}$$
*(In words: The distance to the sun is equal to the distance to the moon divided by the cosine of the angle between them).*

$$d_{ES} = \frac{384,000\text{ km}}{\cos(89.85^\circ)}$$
$$d_{ES} = \frac{384,000}{0.002618}$$
$$d_{ES} \approx 146,677,000\text{ km}$$
*(This is remarkably close to the true value of 149.6 million km!)*

#### Part 2: True Diameter of the Sun ($D_S$)
Because the Sun and Moon look like they are the exact same size in the sky (which is why perfect solar eclipses happen), they have the same angular diameter ($\alpha = 0.53^\circ$). We must first convert this angle into radians by multiplying by $\pi/180$:
$$\alpha_{\text{rad}} = 0.53^\circ \times \frac{\pi}{180} \approx 0.00925\text{ radians}$$

Now we use the small-angle approximation formula:
$$\alpha \approx \frac{D_S}{d_{ES}}$$
$$D_S = \alpha \cdot d_{ES}$$
*(In words: The true diameter of the Sun is equal to its angular size in radians multiplied by its distance from Earth).*

$$D_S = 0.00925 \cdot 146,677,000\text{ km}$$
$$D_S \approx 1,356,762\text{ km}$$
*(The true diameter of the Sun is about 1.39 million km, so this is very close!)*

#### Part 3: Ratio of True Diameters
Since they both have the same angular size ($\alpha$), their true sizes are directly proportional to their distances.
$$\frac{D_M}{d_{EM}} = \frac{D_S}{d_{ES}}$$
$$\frac{D_M}{D_S} = \frac{d_{EM}}{d_{ES}}$$

But wait! We know from Part 1 that $\frac{d_{EM}}{d_{ES}}$ is just $\cos(\theta)$. So:
$$\frac{D_M}{D_S} = \cos(89.85^\circ) \approx 0.002618$$
This means the Moon is roughly $0.26\%$ the width of the Sun.

#### Part 4: The Flaw in Aristarchus' Method
What if Aristarchus measured the angle as $89.75^\circ$ instead of $89.85^\circ$?
$$d_{ES} = \frac{384,000\text{ km}}{\cos(89.75^\circ)}$$
$$d_{ES} = \frac{384,000}{0.004363}$$
$$d_{ES} \approx 88,000,000\text{ km}$$

**Change in distance:**
$$146,677,000 - 88,000,000 = 58,677,000\text{ km}$$

**Comment on Sensitivity:**
By being off by just $0.1$ degrees (a microscopic sliver of the sky), the calculated distance to the Sun completely collapsed by roughly **$58.7\text{ million kilometers}$** (a staggering $40\%$ error)! 

This implies that Aristarchus' method, while mathematically brilliant in theory, was practically useless in reality. Measuring the exact moment of a "perfect half-moon" with the naked eye to a precision of $0.01$ degrees is completely impossible without modern optical instruments.

---

### 3. Final Answer

1.  **Earth-Sun Distance:** $d_{ES} \approx 1.467 \times 10^8\text{ km}$
2.  **Diameter of the Sun:** $D_S \approx 1.357 \times 10^6\text{ km}$
3.  **Ratio ($D_M / D_S$):** $\approx 0.0026$
4.  **Flaw:** A tiny $0.1^\circ$ measurement error leads to a massive $58.7\text{ million km}$ calculation error. The method is too sensitive to be used with the naked eye.
