# Design and Analysis of Algorithms (410241)
**Savitribai Phule Pune University - Computer Engineering (Semester V)**

## In-sem Exam Preparation: Answers to Question Papers

### **Question Paper 1: October 2022**

#### **Q1)**
**a) Why is the correctness of an algorithm important? Define loop invariant property and prove the correctness of finding the summation of n numbers using loop invariant property.** [8 marks]

- **Importance of Correctness**: Correctness ensures that an algorithm produces the expected output for all possible valid inputs. It is crucial because even if an algorithm is efficient, if it produces incorrect results, it is useless.
  
- **Loop Invariant Property**: A loop invariant is a condition that holds true before and after each iteration of a loop. It is used to prove the correctness of algorithms involving loops.

  **Proof Using Loop Invariant for Summation of `n` Numbers**:
  1. **Initialization**: Before the loop starts, the sum is initialized to 0. The invariant holds because the sum of zero elements is zero.
  2. **Maintenance**: During each iteration, a new number is added to the sum. If the invariant holds before an iteration, it still holds afterward.
  3. **Termination**: When the loop terminates after `n` iterations, the sum contains the sum of the first `n` numbers.

**b) What is an iterative algorithm? Explain iterative algorithm design issues using examples.** [7 marks]

- **Iterative Algorithm**: An iterative algorithm repeats a set of instructions until a certain condition is met.
  
- **Design Issues**:
  - **Initialization**: Setting up initial conditions properly.
  - **Termination**: Ensuring the loop will eventually stop.
  - **Efficiency**: Minimizing the number of iterations and operations within each iteration.
  
  **Example**: Finding the factorial of a number using a `for` loop.

**OR**

**Q2)**
**a) How to prove that an algorithm is correct? How to prove the correctness of an algorithm using a counterexample? Give a suitable example.** [7 marks]

- **Proving Correctness**:
  - **Formal Proof**: Using induction or loop invariants.
  - **Counterexample**: Demonstrating an input where the algorithm fails to provide the correct output proves that the algorithm is incorrect.
  
  **Example**: Consider an algorithm that checks for a palindrome. If it fails for the input "racecar", a counterexample is provided.

**b) Write a short note on any 4 problem-solving strategies.** [8 marks]

1. **Divide and Conquer**: Splits a problem into subproblems, solves them independently, and combines results.
2. **Dynamic Programming**: Solves complex problems by breaking them down into simpler subproblems, storing the results to avoid redundant calculations.
3. **Greedy Algorithm**: Makes locally optimal choices with the hope of finding a global optimum.
4. **Backtracking**: Builds a solution incrementally and abandons solutions that fail to satisfy constraints.

#### **Q3)**
**a) What is Best, Average, and Worst-case Analysis of Algorithms? Analyze the following algorithm for Best, Average, and Worst case:**

```c
void sort (int a[], int n) {
    int i, j, key;
    for (i = 1; i < n; i++) {
        j = i - 1;
        key = a[i];
        while (j >= 0 && a[j] > key) {
            a[j + 1] = a[j];
            j = j - 1;
        }
        a[j + 1] = key;
    }
}
```

- **Best Case**: O(n) - When the array is already sorted.
- **Average Case**: O(n^2) - Average scenarios based on input distribution.
- **Worst Case**: O(n^2) - When the array is sorted in reverse order.

**b) Explain P, NP, NP-Hard, and NP-Complete problems with examples. Explain the 3-SAT problem using an example. Why is SAT important in theoretical computer science?** [7 marks]

- **P**: Problems solvable in polynomial time (e.g., Sorting algorithms).
- **NP**: Problems for which a solution can be verified in polynomial time (e.g., Hamiltonian Path).
- **NP-Hard**: As hard as the hardest problems in NP, not necessarily in NP (e.g., Halting Problem).
- **NP-Complete**: Problems that are both in NP and NP-Hard (e.g., 3-SAT).

**3-SAT Problem**:
- A satisfiability problem where each clause has exactly three literals. Used to prove that many computational problems are NP-Complete.

**Importance of SAT**:
- SAT was the first problem proven to be NP-Complete, and it serves as a basis for proving the NP-completeness of other problems.

**OR**

**Q4)**
**a) What is an NP-complete class problem? How would you prove the vertex cover problem is an NP-complete class problem?** [8 marks]

- **NP-Complete**: A problem is NP-Complete if it is in NP and every other problem in NP can be reduced to it in polynomial time.
  
**Vertex Cover Proof**:
1. **Vertex Cover Definition**: A set of vertices such that every edge has at least one endpoint in this set.
2. **Reduction from 3-SAT**: Transform a 3-SAT instance into a graph such that a vertex cover of size `k` exists if and only if the 3-SAT instance is satisfiable.

**b) What is Best, Average, and Worst-case Analysis of Algorithms? Analyze the following algorithm for Best, Average, and Worst case:**

```c
int LinearSearch(int a[], int n, int item) {
    int i;
    for (i = 0; i < n; i++) {
        if (a[i] == item) {
            return i;
        }
    }
    return -1;
}
```

- **Best Case**: O(1) - Item is the first element.
- **Average Case**: O(n) - Item is somewhere in the middle.
- **Worst Case**: O(n) - Item is the last element or not present.

---

### **Question Paper 2**

#### **Q1)**
**a) Given the fastest computer and hypothetically infinite memory, do we still need to study algorithms? Justify.** [2 marks]

- **Answer**: Yes, because the performance of programs depends not just on hardware but on the efficiency of the algorithms used. Efficient algorithms reduce computation time and resource usage, making programs faster and more scalable.

**b) How can we relate algorithms to technology? Briefly explain.** [6 marks]

- **Answer**: Algorithms form the foundation of technology by providing the logic that drives software applications, data processing, and automated systems. They determine how efficiently resources are utilized, how quickly a problem is solved, and how effectively technology can scale to meet user demands.

**c) Consider an array A of `n` integers already in sorted order. Let `x` be the number being searched in the array `A` in a linear fashion. The code fragment performing this task is given below:**

```c
int lin_search(int A[]) {
    int i = 0, flag = 0;
    do {
        if (x == A[i]) {
            return 1;  // Number found
        } else {
            i++;
        }
    } while (i < n);
    return 0;  // Number not found
}
```

- **(i) Is this code fragment efficient?** [Yes, it is efficient within the constraint of using linear search. In a sorted array, a more efficient approach would be binary search (O(log n)), but with linear search, the best-case performance is O(1) if the element is the first one.]
- **(ii) Does it attribute to any design issue with respect to iterative algorithms? Briefly explain.** [Yes, the design issue is not utilizing the fact that the array is sorted; a better design would use binary search for improved efficiency.]

**OR**

**Q2)**
**a) What is an iterative algorithm? Explain iterative algorithm design issues using suitable examples.** [8 marks]

- **Iterative Algorithm**: Repeats operations using loops.
  
- **Design Issues**:
  - **Correct Initialization**: Setting initial values appropriately.
  - **Termination Conditions**: Ensuring loops terminate correctly.
  - **State Update**: Efficiently updating variables after each iteration.

**Example**: Sum of an array of numbers using a `for` loop.

**b) Consider the following algorithm to find the square of a number:**

```c
int sqr(int n) {
    if (n == 0) return 0;
    else return (2 * n + sqr(n - 1) - 1);
}
```

**Prove the correctness of this algorithm using the principle of mathematical induction or otherwise.** [7 marks]

- **Proof by Induction**:
  - **Base Case**: For `n = 0`, `sqr(0) = 0`.
  - **Inductive Step**: Assume it works for `n = k`. For `n = k + 1`, the function computes `2 * (k + 1) + sqr(k) - 1`. By the inductive hypothesis, `sqr(k) = k * k`, so `sqr(k + 1) = (k + 1) * (k + 1)`. Therefore, the algorithm is correct.

#### **Q3)**
**a) Briefly explain P and NP problems in the context of complexity theory. Give a suitable example.** [8 marks]

- **P (Polynomial Time)**: The class of decision problems that can be solved by a deterministic Turing machine in polynomial time. **Example**: Finding the shortest path in a graph (Dijkstra's Algorithm).

- **NP (Nondeterministic Polynomial Time)**: The class of decision problems for which a given solution can be verified by a deterministic Turing machine in polynomial time. **Example**: The Traveling Salesman Problem (TSP).

**b) If `f(n) = O(g(n))`, does it imply `g(n) = O(f(n))`? Discuss.** [5 marks]

- **Answer**: No, `f(n) = O(g(n))` means that `f(n)` grows at most as fast as `g(n)`, but `g(n)` could grow faster than `f(n)`. For example, if `f(n) = n` and `g(n) = n^2`, then `f(n) = O(g(n))`, but `g(n) ≠ O(f(n))`.

**c) Comment on the statement "Best case analysis of an algorithm may not give a clear idea of performance."** [2 marks]

- **Answer**: Best-case analysis only considers the scenario where the algorithm performs the minimum number of operations. This is often not representative of typical inputs or the average behavior of the algorithm. Thus, it does not provide a complete picture of its performance.

**OR**

**Q4)**
**a) What is SAT and 3-SAT problem? Prove that 3-SAT problem is NP-complete.** [8 marks]

- **SAT (Satisfiability Problem)**: Given a Boolean formula, is there an assignment of truth values to variables that makes the formula true?

- **3-SAT**: A special case of SAT where each clause has exactly three literals.

**Proof of NP-Completeness**:
1. **NP Membership**: Given a truth assignment, we can verify in polynomial time if it satisfies the formula.
2. **Reduction from SAT to 3-SAT**: Any SAT instance can be converted into a 3-SAT instance in polynomial time, showing that 3-SAT is at least as hard as SAT, which is NP-complete.

**b) What do you understand by best-case, worst-case, and average-case behavior of an algorithm? Is an average-case efficiency an average of best-case and worst-case efficiencies? Justify your answer.** [7 marks]

- **Best Case**: The scenario where the algorithm performs the minimum number of steps (e.g., finding an item in the first position in a search).
  
- **Worst Case**: The scenario where the algorithm performs the maximum number of steps (e.g., searching an unsorted list where the item is the last).

- **Average Case**: The expected number of steps the algorithm takes, averaged over all possible inputs.

- **Answer**: The average case is not simply the mean of the best and worst cases; it considers all possible inputs and their probabilities, providing a more realistic measure of typical performance.

---

### **Study Notes Summary**

- **Correctness of Algorithms**: Importance, loop invariants, proofs.
- **Algorithm Design Issues**: Iterative vs. recursive, efficiency, termination.
- **Algorithm Analysis**: Best, worst, average case scenarios; Big O notation.
- **Complexity Classes**: P, NP, NP-Hard, NP-Complete, with examples.
- **Problem Solving Strategies**: Divide and Conquer, Dynamic Programming, Greedy, Backtracking.
- **Special Problems**: 3-SAT, Vertex Cover, proving NP-completeness.
