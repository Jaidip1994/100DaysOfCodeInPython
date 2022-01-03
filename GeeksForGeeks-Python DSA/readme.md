# Points Learnt from Course
- What is Asymptotic Analysis

    1. No dependency on the Machine, programming languages , etc
    2. No need to implement all the ideas/algos, even the pseudo code works
    3. Asymptotic Analysis is about measuring order of growth in terms of input size. 

- What is order of growth
    1. Usefull while doing theoritical analysis of Algorithm
    2. A function f(n) is said to be growing faster than g(n), if one of the condition is true
    $$~  \lim_{n \rightarrow - \infty} \frac{f(n)}{g(n)} = \infty ~$$
    or
    $$~  \lim_{n \rightarrow - \infty} \frac{g(n)}{f(n)} = 0 ~$$

    - How to calculate the order of growth
        - Ignore lower order terms
        - Ignore leading constants
    $$~ c < loglogn < logn < n^\frac{1}{3} < n^\frac{1}{2} < n < nlogn < n^2 ~$$