# Problem 4: Vector Calculus

### 1. Problem Statement

The position of an object is given by the vector:
$$\vec{r}(t) = (3t^2)\hat{i} + (5t - 8t^2)\hat{j}$$
Find the object's velocity and acceleration vectors as a function of time.

---

### 2. Solution and Explanation

**Concept Intuition:**
In physics, if you know where an object is (Position), you can find out how fast it is moving (Velocity) by taking the first derivative. If you want to know how hard it is being pushed (Acceleration), you take the derivative one more time.

The $\hat{i}$ just means "horizontal $x$-direction" and the $\hat{j}$ means "vertical $y$-direction". We treat them as completely separate problems that just happen to sit next to each other.

#### Step 1: Find Velocity (First Derivative)

Velocity $\vec{v}(t)$ is the derivative of position $\vec{r}(t)$ with respect to time $t$.
$$\vec{v}(t) = \frac{d\vec{r}}{dt}$$

We apply the basic Power Rule (multiply by the exponent, then drop the exponent by 1) to each piece separately:

- **The $\hat{i}$ component:** The derivative of $3t^2$ is $6t$.
- **The $\hat{j}$ component:** The derivative of $5t$ is $5$, and the derivative of $-8t^2$ is $-16t$.

Putting it together:
$$\vec{v}(t) = (6t)\hat{i} + (5 - 16t)\hat{j}$$

#### Step 2: Find Acceleration (Second Derivative)

Acceleration $\vec{a}(t)$ is the derivative of velocity $\vec{v}(t)$ with respect to time $t$.
$$\vec{a}(t) = \frac{d\vec{v}}{dt}$$

We apply the Power Rule one more time to our new velocity equation:

- **The $\hat{i}$ component:** The derivative of $6t$ is just $6$.
- **The $\hat{j}$ component:** The derivative of $5$ is $0$ (since it's a constant), and the derivative of $-16t$ is $-16$.

Putting it together:
$$\vec{a}(t) = 6\hat{i} - 16\hat{j}$$

_(Notice that the acceleration has no $t$ left in it. This means the object is experiencing a constant, unchanging acceleration)._

---

### 3. Final Answers

- **Velocity Vector:** $\vec{v}(t) = (6t)\hat{i} + (5 - 16t)\hat{j}$
- **Acceleration Vector:** $\vec{a}(t) = 6\hat{i} - 16\hat{j}$
