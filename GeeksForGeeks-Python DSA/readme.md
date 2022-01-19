# Points Learnt from Course
- What is Asymptotic Analysis

    1. No dependency on the Machine, programming languages , etc
    2. No need to implement all the ideas/algos, even the pseudo code works
    3. Asymptotic Analysis is about measuring order of growth in terms of input size. 
---
- What is order of growth
    1. Usefull while doing theoritical analysis of Algorithm
    2. A function f(n) is said to be growing faster than g(n), if one of the condition is true
![image](https://user-images.githubusercontent.com/11685096/147967217-d3737bd0-cd28-449c-a8c1-87a276759044.png)


    - How to calculate the order of growth
        - Ignore lower order terms
        - Ignore leading constants
        
    ![image](https://user-images.githubusercontent.com/11685096/147967260-4c0d1c10-c233-41be-b914-07669bbf7f5c.png)

- Order of Growth can be measured in three ways - *Best, Worst & Average Cases*
- Asymptotic Notation
    - Big O - represent exact or upper bound
    
    ![bigONotation](https://user-images.githubusercontent.com/11685096/148276958-f5933984-9628-4682-b5e3-a31c491c1633.jpeg)
    - Theta - represent exact bound
    ![ThetaPart1](https://user-images.githubusercontent.com/11685096/149486080-1b25cf12-41ee-4422-8db6-8edb1efc6283.jpeg)
    ![ThetaPart2](https://user-images.githubusercontent.com/11685096/149486200-6dfd0a5e-4b36-413e-b69c-f62097a1e906.jpeg)

    - Omega - represent exact or lower bound
    ![Omega](https://user-images.githubusercontent.com/11685096/149277925-6b86fa34-0155-42d6-abb5-10c8669c878c.jpeg)
        - if f(n) = Omega(g(n))
        - then g(n) = BigO(f(n))
    
---
- What is Space Complexity
Order of growth of memory(RAM) usage in terms of input
- What is Auxiliary Space
Order of growth of extra space( other than i/p or o/p)
