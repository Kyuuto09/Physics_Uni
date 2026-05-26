# Problem 7: Standard Deviation (Test Scores)

### 1. Problem Statement

Eleven students received the following scores on a test: 88, 92, 79, 85, 95, 81, 86, 90, 83, 77, 89. 
1. What is the mean $\bar{x}=\frac{1}{N} \sum_{i=1}^N x_i$ and standard deviation $\sigma=\sqrt{\frac{1}{N-1} \sum_{i=1}^N (x_i - \bar{x})^2}$ of these test scores? 
2. If the highest and lowest scores are removed, what are the new mean and standard deviation of the remaining scores?

---

### 2. Solution and Explanation

**Concept Intuition:**
The **mean** gives us the "center of mass" or average of our dataset. The **standard deviation** tells us how "spread out" the data is around that mean. A high standard deviation means the data is widely scattered; a low standard deviation means the data points are tightly clustered together. 

Outliers (extremely high or low values) can heavily skew the standard deviation because the differences from the mean are *squared* in the formula. Removing them should noticeably tighten up our spread.

#### Part 1: All 11 Scores
**Data ($N=11$):** 77, 79, 81, 83, 85, 86, 88, 89, 90, 92, 95

*   **Step A: Calculate the Mean ($\bar{x}$)**
    Sum of all 11 scores = $945$
    $$\bar{x} = \frac{945}{11} \approx 85.91$$

*   **Step B: Calculate the Standard Deviation ($\sigma$)**
    First, we find how far each score is from the mean ($x_i - \bar{x}$), and square that difference. 
    Sum of squared differences:
    $\sum (x_i - \bar{x})^2 = (77-85.91)^2 + (79-85.91)^2 + ... + (95-85.91)^2 \approx 310.91$

    Now, apply the sample standard deviation formula (dividing by $N-1 = 10$):
    $$\sigma = \sqrt{\frac{310.91}{10}} = \sqrt{31.091} \approx 5.58$$

---

#### Part 2: Removing the Highest and Lowest Scores
We identify and remove the lowest score (77) and the highest score (95).
**Remaining Data ($N=9$):** 79, 81, 83, 85, 86, 88, 89, 90, 92

*   **Step C: Calculate the New Mean ($\bar{x}_{new}$)**
    New sum of the 9 scores = $945 - 77 - 95 = 773$
    $$\bar{x}_{new} = \frac{773}{9} \approx 85.89$$
    *(Notice how the mean barely changed! Because the outliers we removed were roughly symmetric around the center, the "center of mass" stayed put.)*

*   **Step D: Calculate the New Standard Deviation ($\sigma_{new}$)**
    Find the new sum of squared differences from the new mean:
    $\sum (x_i - \bar{x}_{new})^2 \approx 148.89$

    Apply the standard deviation formula for the remaining 9 items (dividing by $N-1 = 8$):
    $$\sigma_{new} = \sqrt{\frac{148.89}{8}} = \sqrt{18.61} \approx 4.31$$
    *(Notice how much the standard deviation dropped! By trimming the extreme ends, our data is now mathematically much more "clustered".)*

---

### 3. Final Answer

**Original Data (11 students):**
*   **Mean:** $85.91$
*   **Standard Deviation:** $5.58$

**Trimmed Data (9 students):**
*   **Mean:** $85.89$
*   **Standard Deviation:** $4.31$
