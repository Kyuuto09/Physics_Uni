# Problem 6: Wave Equation

### 1. Problem Statement

A wave is described by the equation $y(x,t) = 0.05 \sin(2\pi x - 50\pi t)$, where $x$ and $y$ are in meters and $t$ is in seconds. Determine the waves':
a) Amplitude $A$.
b) Wavelength $\lambda$.
c) Frequency $f$.
d) Wave speed $v$.

---

### 2. Solution and Explanation

**Concept Intuition:**
Think of the standard traveling wave equation as a predefined class or blueprint:
$$y(x,t) = A \sin(kx - \omega t)$$

When we are handed a specific object instance like $y(x,t) = 0.05 \sin(2\pi x - 50\pi t)$, we can simply map our given numbers directly to the variables in the blueprint:

- **$A$ (Amplitude)** is the multiplier in front: $0.05$
- **$k$ (Wave Number)** is the multiplier attached to $x$: $2\pi$
- **$\omega$ (Angular Frequency)** is the multiplier attached to $t$: $50\pi$

Once we have parsed these three core variables, finding the physical properties is just running them through basic translation formulas.

#### a) Find the Amplitude ($A$)

We parse this directly from the equation. It is the maximum displacement from the center.
$$A = 0.05\text{ meters}$$

#### b) Find the Wavelength ($\lambda$)

We parsed the wave number ($k = 2\pi$) from the equation. The formula connecting $k$ to the physical wavelength is $k = \frac{2\pi}{\lambda}$.
$$2\pi = \frac{2\pi}{\lambda}$$
Solve for $\lambda$ by multiplying both sides by $\lambda$ and dividing by $2\pi$:
$$\lambda = \frac{2\pi}{2\pi} = 1\text{ meter}$$

#### c) Find the Frequency ($f$)

We parsed the angular frequency ($\omega = 50\pi$) from the equation. This is the "clock speed" in radians. The formula to convert radians per second into standard Hertz (cycles per second) is $\omega = 2\pi f$.
$$50\pi = 2\pi f$$
Solve for $f$ by dividing both sides by $2\pi$:
$$f = \frac{50\pi}{2\pi} = 25\text{ Hz}$$

#### d) Find the Wave Speed ($v$)

Now that we have the physical size of the wave ($\lambda = 1\text{ m}$) and how many times it cycles per second ($f = 25\text{ Hz}$), we use the fundamental wave equation ($v = f \cdot \lambda$) to find how fast it is traveling across the screen.
$$v = 25 \cdot 1$$
$$v = 25\text{ m/s}$$

_(Alternative developer shortcut: You can also find speed directly from the parsed variables without calculating $f$ or $\lambda$ first using the formula $v = \frac{\omega}{k} = \frac{50\pi}{2\pi} = 25\text{ m/s}$.)_

---

### 3. Final Answers

- **a) Amplitude ($A$):** $0.05\text{ m}$
- **b) Wavelength ($\lambda$):** $1\text{ m}$
- **c) Frequency ($f$):** $25\text{ Hz}$
- **d) Wave Speed ($v$):** $25\text{ m/s}$
