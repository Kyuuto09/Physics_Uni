# Problem 5: Echo Ranging

### 1. Problem Statement

A person shouts towards a cliff and hears the echo 1 second later. How far away is the cliff? (Speed of sound in air is 343 m/s).

---

### 2. Solution and Explanation

**Concept Intuition:**
Think of an echo exactly like a network `ping`. When you ping a server, the latency metric you get back is the "Round-Trip Time" (RTT)—the time it takes for the data packet to hit the server _and_ travel all the way back to your machine.

If you want to know the one-way distance to the cliff (the server), you cannot use the full round-trip time. You must cut the total time in half before multiplying it by the speed of the sound wave.

#### Step 1: Calculate the One-Way Time

The problem states the total round-trip time is 1 second. We divide this by 2 to find the time it took for the sound to just reach the cliff.
$$t_{one-way} = \frac{t_{total}}{2}$$
$$t_{one-way} = \frac{1}{2} = 0.5 \text{ seconds}$$

#### Step 2: Calculate the Distance

Now we use the standard linear distance formula, multiplying the transmission speed ($v$) by our one-way time:
$$d = v \cdot t_{one-way}$$
$$d = 343 \cdot 0.5$$
$$d = 171.5 \text{ meters}$$

---

### 3. Final Answer

- **Distance to the cliff:** 171.5 meters
