# **Unit 3: Greedy and Dynamic Programming Algorithmic Strategies**
## **Greedy Algorithm**

### **Principle**
A greedy algorithm makes a sequence of choices, each of which looks best at the moment, to solve an optimization problem. It relies on two key properties:
1. **Greedy Choice Property**:  
   A global (overall) optimal solution can be arrived at by choosing the best local option at every step.
2. **Optimal Substructure**:  
   A problem exhibits optimal substructure if an optimal solution can be constructed from optimal solutions to its subproblems.

---

### **Steps of a Greedy Algorithm**
1. Sort the data (if necessary).
2. Make the greedy choice that appears to be the best at the current step.
3. Check if the choice is feasible.
4. Repeat until the solution is complete.

---

### **Examples**

#### **1. Fractional Knapsack Problem**
- **Problem Statement**: Given `n` items with weights and values, maximize the total value in a knapsack of capacity `W`, allowing fractional items.
- **Approach**:
  1. Calculate \( \frac{\text{value}}{\text{weight}} \) for each item.
  2. Sort items in descending order of \( \frac{\text{value}}{\text{weight}} \).
  3. Pick items in sorted order, adding as much as possible until the knapsack is full.
  4. Include fractional parts if needed.
- **Algorithm**:
  ```
  1. Sort items by value-to-weight ratio.
  2. Initialize total_value = 0.
  3. For each item:
       if capacity >= weight:
           Add full item to knapsack.
           Update capacity and total_value.
       else:
           Add fractional part to knapsack.
           Break.
  ```
- **Time Complexity**: \( O(n \log n) \) (due to sorting).

#### **2. Activity Selection Problem**
- **Problem Statement**: Given `n` activities with start and finish times, select the maximum number of non-overlapping activities.
- **Approach**:
  1. Sort activities by finish time.
  2. Select the first activity.
  3. For each subsequent activity, include it if its start time is greater than or equal to the finish time of the last selected activity.
- **Algorithm**:
  ```
  1. Sort activities by finish time.
  2. Select the first activity.
  3. For each remaining activity:
       If activity.start >= last_selected.finish:
           Include the activity.
  ```
- **Time Complexity**: \( O(n \log n) \) (due to sorting).

#### **3. Job Sequencing Problem**
- **Problem Statement**: Given `n` jobs, each with a deadline and profit, schedule jobs to maximize profit such that each job is completed within its deadline.
- **Approach**:
  1. Sort jobs by profit in descending order.
  2. For each job, find the latest available slot before its deadline and assign it.
- **Algorithm**:
  ```
  1. Sort jobs by profit in descending order.
  2. Initialize an array to track available slots.
  3. For each job:
       Find the latest free slot (if any) before its deadline.
       Assign the job to that slot and add its profit.
  ```
- **Time Complexity**: \( O(n^2) \) or \( O(n \log n) \) (with optimized data structures).

---

## **Dynamic Programming (DP)**

### **Principle**
Dynamic Programming solves problems by dividing them into overlapping subproblems, solving each subproblem only once, and storing the result for reuse.

#### Key Properties:
1. **Optimal Substructure**: An optimal solution can be constructed from optimal solutions to subproblems.
2. **Overlapping Subproblems**: The same subproblems are solved multiple times.

---

### **Steps of a DP Algorithm**
1. Define the recursive relation for the problem.
2. Identify base cases.
3. Store the results of subproblems in a table (bottom-up approach) or cache (top-down approach with memoization).
4. Use stored results to build the final solution.

---

### **Examples**

#### **1. 0/1 Knapsack Problem**
- **Problem Statement**: Maximize the total value in a knapsack of capacity `W`, where items are indivisible.
- **Recursive Relation**:
  \[
  K[i, w] =
  \begin{cases} 
  K[i-1, w] & \text{if } w < \text{weight}[i] \\ 
  \max(K[i-1, w], K[i-1, w - \text{weight}[i]] + \text{value}[i]) & \text{otherwise}
  \end{cases}
  \]
- **Approach**:
  1. Create a DP table with dimensions `[n+1][W+1]`.
  2. Fill the table iteratively based on the recursive relation.
  3. The final value \( K[n, W] \) gives the maximum profit.
- **Algorithm**:
  ```
  1. Initialize a DP table dp[n+1][W+1] to 0.
  2. For i = 1 to n:
       For w = 1 to W:
           If weight[i] > w:
               dp[i][w] = dp[i-1][w]
           Else:
               dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight[i]] + value[i])
  3. Return dp[n][W].
  ```
- **Time Complexity**: \( O(n \cdot W) \).

#### **2. Matrix Chain Multiplication**
- **Problem Statement**: Minimize the number of scalar multiplications required to compute the product of matrices \( A_1 \times A_2 \times \dots \times A_n \).
- **Recursive Relation**:
  \[
  m[i, j] = \min_{i \leq k < j} \big(m[i, k] + m[k+1, j] + p_{i-1}p_kp_j\big)
  \]
- **Approach**:
  1. Create a DP table to store costs.
  2. Calculate costs for increasing chain lengths.
  3. Use the table to compute the minimum cost.
- **Algorithm**:
  ```
  1. Initialize m[i][i] = 0 for all i.
  2. For chain length l = 2 to n:
       For i = 1 to n-l+1:
           j = i + l - 1
           m[i][j] = min(m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]) for all k in [i, j)
  3. Return m[1][n].
  ```
- **Time Complexity**: \( O(n^3) \).

#### **3. Longest Common Subsequence (LCS)**
- **Problem Statement**: Find the longest subsequence common to two strings.
- **Recursive Relation**:
  \[
  L[i, j] =
  \begin{cases} 
  0 & \text{if } i = 0 \text{ or } j = 0 \\ 
  L[i-1, j-1] + 1 & \text{if } X[i] = Y[j] \\ 
  \max(L[i-1, j], L[i, j-1]) & \text{otherwise}
  \end{cases}
  \]
- **Algorithm**:
  ```
  1. Initialize a DP table L[m+1][n+1] to 0.
  2. For i = 1 to m:
       For j = 1 to n:
           If X[i] == Y[j]:
               L[i][j] = L[i-1][j-1] + 1
           Else:
               L[i][j] = max(L[i-1][j], L[i][j-1])
  3. Return L[m][n].
  ```
- **Time Complexity**: \( O(m \cdot n) \).

---

## **Comparison of Greedy and DP**

| Aspect               | Greedy                     | Dynamic Programming         |
|-----------------------|----------------------------|------------------------------|
| Problem Decomposition | Local decisions            | Global problem decomposition |
| Overlapping Subproblems | No                        | Yes                          |
| Optimal Substructure  | Yes                        | Yes                          |
| Memory Usage         | Minimal                    | High (due to table storage)  |
| Examples             | Fractional Knapsack, Activity Selection | 0/1 Knapsack, LCS, Matrix Chain |

---
---

# **Unit 4: Graph Algorithms**
## **Introduction to Graphs**
Graphs are data structures consisting of nodes (**vertices**) and edges that connect pairs of nodes. They are used to model relationships between objects.

### **Types of Graphs**
- **Directed Graph (Digraph)**: Edges have a direction (e.g., \( A \to B \)).
- **Undirected Graph**: Edges have no direction (e.g., \( A \text{—} B \)).
- **Weighted Graph**: Edges have weights (e.g., cost, distance).
- **Unweighted Graph**: Edges have no weights.
- **Connected Graph**: There is a path between every pair of vertices.
- **Disconnected Graph**: Some vertices are not connected by paths.
- **Cyclic Graph**: Contains at least one cycle.
- **Acyclic Graph**: No cycles exist in the graph.

### **Graph Representations**
1. **Adjacency Matrix**: A 2D array where \( M[i][j] = 1 \) if there is an edge from vertex \( i \) to \( j \); otherwise \( M[i][j] = 0 \).
   - **Space Complexity**: \( O(V^2) \), where \( V \) is the number of vertices.
2. **Adjacency List**: A list where each vertex has a list of connected vertices.
   - **Space Complexity**: \( O(V + E) \), where \( E \) is the number of edges.

---

## **1. Minimum Spanning Tree (MST)**

### **Definition**
A **Minimum Spanning Tree** is a subset of edges in a connected, weighted, undirected graph that connects all the vertices with the minimum possible total edge weight and without forming any cycles.

### **Algorithms**
#### **1. Kruskal’s Algorithm**
- **Approach**:
  1. Sort all edges in non-decreasing order of weights.
  2. Use the **Union-Find** data structure to detect cycles.
  3. Add edges to the MST one by one, ensuring no cycles are formed.

- **Algorithm**:
  ```plaintext
  1. Sort edges by weight.
  2. Initialize MST as empty.
  3. For each edge (u, v):
       If u and v are not in the same set (no cycle):
           Add (u, v) to MST.
           Union(u, v).
  ```
- **Time Complexity**: \( O(E \log E + V \alpha(V)) \), where \( \alpha(V) \) is the inverse Ackermann function.

#### **2. Prim’s Algorithm**
- **Approach**:
  - Use a priority queue to greedily pick the smallest edge that connects a vertex in the MST to a vertex not in the MST.

- **Algorithm**:
  ```plaintext
  1. Initialize MST set as empty and pick any starting vertex.
  2. Push all edges of the starting vertex into the priority queue.
  3. While MST does not include all vertices:
       Pop the minimum weight edge (u, v) from the queue.
       If v is not in MST:
           Add v to MST.
           Add all edges of v to the queue.
  ```
- **Time Complexity**: \( O(E \log V) \).

---

## **2. Shortest Path Algorithms**

### **1. Dijkstra’s Algorithm**
- **Purpose**: Finds the shortest path from a source vertex to all other vertices in a graph with non-negative weights.
- **Algorithm**:
  ```plaintext
  1. Initialize distance[source] = 0, all others = ∞.
  2. Push (source, 0) to the priority queue.
  3. While the queue is not empty:
       Pop the vertex u with the smallest distance.
       For each neighbor v of u:
           If distance[u] + weight(u, v) < distance[v]:
               Update distance[v].
               Push (v, distance[v]) to the queue.
  ```
- **Time Complexity**: \( O(E \log V) \).

### **2. Bellman-Ford Algorithm**
- **Purpose**: Computes the shortest path from a single source to all vertices, even with negative weights.
- **Algorithm**:
  ```plaintext
  1. Initialize distance[source] = 0, all others = ∞.
  2. Repeat V-1 times:
       For each edge (u, v) with weight w:
           If distance[u] + w < distance[v]:
               Update distance[v].
  3. For each edge (u, v) with weight w:
       If distance[u] + w < distance[v]:
           Report a negative weight cycle.
  ```
- **Time Complexity**: \( O(VE) \).

---

## **3. All-Pairs Shortest Paths**

### **Floyd-Warshall Algorithm**
- **Purpose**: Computes shortest paths between all pairs of vertices.
- **Algorithm**:
  ```plaintext
  1. Initialize dist[i][j] = weight(i, j) if edge exists, else ∞.
  2. For k = 1 to V:
       For i = 1 to V:
           For j = 1 to V:
               dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
  ```
- **Time Complexity**: \( O(V^3) \).

---

## **4. Graph Traversal**

### **1. Breadth-First Search (BFS)**
- **Purpose**: Traverses the graph level by level.
- **Algorithm**:
  ```plaintext
  1. Initialize all vertices as unvisited.
  2. Enqueue the starting vertex and mark it as visited.
  3. While the queue is not empty:
       Dequeue a vertex u.
       For each neighbor v of u:
           If v is unvisited:
               Mark v as visited.
               Enqueue v.
  ```
- **Time Complexity**: \( O(V + E) \).

### **2. Depth-First Search (DFS)**
- **Purpose**: Explores as far as possible along a branch before backtracking.
- **Algorithm**:
  ```plaintext
  1. Initialize all vertices as unvisited.
  2. Start at a vertex and mark it as visited.
  3. For each neighbor of the current vertex:
       If the neighbor is unvisited:
           Recur for the neighbor.
  ```
- **Time Complexity**: \( O(V + E) \).

---

## **5. Topological Sorting**
- **Purpose**: Orders vertices in a Directed Acyclic Graph (DAG) such that for every directed edge \( u \to v \), \( u \) appears before \( v \).

- **DFS-Based Algorithm**:
  ```plaintext
  1. Perform DFS and record finish times of vertices.
  2. Push vertices onto a stack in reverse order of their finish times.
  3. Pop vertices from the stack for the topological order.
  ```
- **Time Complexity**: \( O(V + E) \).

---
---
# **Unit 5: Tries, Segment Trees, and Disjoint Set Union (DSU)**
## **1. Tries**

### **Introduction**
- A **Trie** (or prefix tree) is a tree-based data structure used for efficient string operations like searching, inserting, and deleting.
- Common applications include autocomplete, spell checking, and IP routing.

---

### **Properties**
1. Each node represents a single character of a string.
2. The root node represents an empty string.
3. Edges represent connections between characters.
4. Words are identified by paths from the root to terminating nodes.

---

### **Operations**

#### **1. Insert**
- Traverse the tree and create nodes for characters that are not present.
- Mark the last node as the end of the word.

**Algorithm**:
1. Start at the root node.
2. For each character in the word:
   - If the character is not a child of the current node, create a new node.
   - Move to the child node.
3. Mark the last node as the end of the word.

**Time Complexity**: \( O(L) \), where \( L \) is the word length.

#### **2. Search**
- Traverse nodes corresponding to each character and check if the last node is marked as the end of the word.

**Algorithm**:
1. Start at the root node.
2. For each character in the word:
   - If the character is not a child, return `false`.
   - Move to the child node.
3. Return `true` if the last node is marked as the end of the word.

**Time Complexity**: \( O(L) \).

#### **3. Delete**
- Unmark the last node and remove nodes not part of any other word.

**Algorithm**:
1. Recursively traverse the word.
2. Unmark the last character as the end of the word.
3. Remove nodes no longer part of other words.

**Time Complexity**: \( O(L) \).

---

### **Applications**
- Autocomplete systems.
- Spell checking.
- Longest prefix matching in network routing.
- Pattern matching.

---

## **2. Segment Trees**

### **Introduction**
- A **Segment Tree** is a binary tree structure used for efficient range queries and updates.
- Common operations include sum, minimum, maximum, and GCD over a range.

---

### **Structure**
1. Represents segments (ranges) of an array.
2. Root represents the entire range, while leaf nodes represent individual elements.

---

### **Operations**

#### **1. Build**
- Recursively divide the array into segments and compute results for each node.

**Algorithm**:
1. If the range contains one element:
   - Store the element in the node.
2. Otherwise:
   - Recursively build left and right child nodes.
   - Combine their results for the current node.

**Time Complexity**: \( O(N) \).

#### **2. Range Query**
- Compute results for a given range by traversing the tree.

**Algorithm**:
1. If the current node's range is inside the query range:
   - Return the node's value.
2. If the current node's range is outside the query range:
   - Return a neutral value (e.g., 0 for sum).
3. Otherwise:
   - Recursively query left and right child nodes and combine results.

**Time Complexity**: \( O(\log N) \).

#### **3. Update**
- Update an element and propagate changes up the tree.

**Algorithm**:
1. If the current node represents the element:
   - Update the value.
2. Otherwise:
   - Recursively update the left or right child.
   - Recalculate the current node's value.

**Time Complexity**: \( O(\log N) \).

---

### **Applications**
- Range sum, minimum, and maximum queries.
- Range GCD or LCM queries.
- Lazy propagation for range updates.

---

## **3. Disjoint Set Union (DSU)**

### **Introduction**
- DSU (or Union-Find) manages collections of disjoint sets.
- Used in graph algorithms like Kruskal’s MST and dynamic connectivity.

---

### **Operations**

#### **1. Find**
- Determine the root of the set containing an element.
- **Path Compression** flattens the structure for faster future queries.

**Algorithm**:
1. If the element is the root, return it.
2. Otherwise:
   - Recursively find the root.
   - Update the element's parent.

---

#### **2. Union**
- Merge two sets by attaching one root to another.
- **Union by Rank** keeps the structure balanced.

**Algorithm**:
1. Find the roots of both sets.
2. If roots are different:
   - Attach the smaller tree under the larger tree.

---

### **Time Complexity**
- **Amortized**: \( O(\alpha(N)) \), where \( \alpha \) is the inverse Ackermann function (almost constant).

---

### **Applications**
- Kruskal’s MST algorithm.
- Finding connected components in a graph.
- Dynamic connectivity problems.
- Network connectivity.

---

## **Comparison Table**

| **Data Structure** | **Operations**          | **Time Complexity**          |
|---------------------|-------------------------|--------------------------------|
| Trie                | Insert/Search/Delete   | \( O(L) \)                    |
| Segment Tree        | Build/Query/Update     | \( O(N), O(\log N) \)         |
| DSU                 | Find/Union             | \( O(\alpha(N)) \)            |

---

## **Summary**
1. **Trie**: Efficient for string operations and prefix-based queries.
2. **Segment Tree**: Ideal for range queries and updates with logarithmic complexity.
3. **DSU**: Powerful for dynamic connectivity and union operations in graph algorithms.

---
---
# **Unit 6: Graph Algorithms**
## **1. Basics of Graphs**

### **Introduction**
- A **Graph** is a data structure consisting of nodes (or vertices) and edges connecting them.
- Graphs can represent networks, relationships, paths, etc.

---

### **Types of Graphs**
1. **Directed Graph**:
   - Edges have a direction, going from one vertex to another.
   - Represented as \( G = (V, E) \), where \( V \) is the set of vertices, and \( E \) is the set of directed edges.

2. **Undirected Graph**:
   - Edges have no direction.
   - Both vertices are considered connected.

3. **Weighted Graph**:
   - Edges have weights (costs, distances, etc.).
   
4. **Unweighted Graph**:
   - All edges are treated equally without weights.

5. **Cyclic Graph**:
   - Contains at least one cycle (a path where the first and last vertices are the same).

6. **Acyclic Graph**:
   - Contains no cycles.

---

### **Graph Representations**
1. **Adjacency Matrix**:
   - 2D array of size \( V \times V \), where \( matrix[i][j] \) represents the presence of an edge between vertex \( i \) and \( j \).
   - **Space Complexity**: \( O(V^2) \).

2. **Adjacency List**:
   - Array of lists where each vertex has a list of its adjacent vertices.
   - **Space Complexity**: \( O(V + E) \).

---

### **Applications**
- Social networks.
- Route optimization.
- Electrical circuits.
- Web page ranking.

---

## **2. Depth First Search (DFS)**

### **Introduction**
- A traversal algorithm that explores as far as possible along each branch before backtracking.
- Uses a stack (or recursion).

---

### **Algorithm**
1. Start from a given vertex.
2. Mark the current vertex as visited.
3. Explore all adjacent vertices that are not visited.
4. Backtrack when no unvisited adjacent vertices are left.

- **Time Complexity**: \( O(V + E) \).
- **Space Complexity**: \( O(V) \).

---

### **Applications**
- Finding connected components.
- Detecting cycles.
- Solving mazes.
- Topological sorting.

---

## **3. Breadth First Search (BFS)**

### **Introduction**
- A traversal algorithm that explores all vertices at the current depth before moving to the next depth level.
- Uses a queue.

---

### **Algorithm**
1. Start from a given vertex.
2. Mark the current vertex as visited and enqueue it.
3. Dequeue a vertex and visit all its unvisited adjacent vertices.
4. Repeat until the queue is empty.

- **Time Complexity**: \( O(V + E) \).
- **Space Complexity**: \( O(V) \).

---

### **Applications**
- Shortest path in an unweighted graph.
- Level order traversal.
- Finding connected components.

---

## **4. Dijkstra’s Algorithm**

### **Introduction**
- A greedy algorithm to find the shortest path from a source vertex to all other vertices in a weighted graph.
- Works for graphs with non-negative weights.

---

### **Algorithm**
1. Initialize distances of all vertices as infinity except the source, which is 0.
2. Use a priority queue to pick the vertex with the minimum distance.
3. Update distances of adjacent vertices.
4. Repeat until all vertices are processed.

- **Time Complexity**: \( O((V + E) \log V) \).

---

### **Applications**
- GPS navigation systems.
- Network routing protocols.
- Minimum cost spanning paths.

---

## **5. Bellman-Ford Algorithm**

### **Introduction**
- Used to find the shortest path from a source vertex to all other vertices in a weighted graph.
- Handles graphs with negative weights.

---

### **Algorithm**
1. Initialize distances as infinity except for the source, which is 0.
2. For \( V - 1 \) iterations:
   - Relax all edges by updating the distance if a shorter path is found.
3. Check for negative weight cycles.

- **Time Complexity**: \( O(V \times E) \).

---

### **Applications**
- Detecting negative weight cycles.
- Shortest path in networks with negative weights.

---

## **6. Floyd-Warshall Algorithm**

### **Introduction**
- A dynamic programming algorithm to find the shortest paths between all pairs of vertices.
- Handles both directed and undirected graphs.

---

### **Algorithm**
1. Initialize the distance matrix with weights.
2. Update the distance between pairs using intermediate vertices.
3. \( dist[i][j] = \min(dist[i][j], dist[i][k] + dist[k][j]) \).

- **Time Complexity**: \( O(V^3) \).

---

### **Applications**
- All-pairs shortest paths.
- Network analysis.
- Graph closure problems.

---

## **7. Minimum Spanning Tree (MST)**

### **Definition**
- A spanning tree of a graph is a subgraph that connects all vertices with the minimum total edge weight and no cycles.

---

### **Kruskal’s Algorithm**
1. Sort all edges by weight.
2. Pick the smallest edge that doesn’t form a cycle.
3. Repeat until all vertices are connected.

- **Time Complexity**: \( O(E \log E) \).

---

### **Prim’s Algorithm**
1. Start with an arbitrary vertex.
2. Add the smallest edge connecting the tree to a new vertex.
3. Repeat until all vertices are connected.

- **Time Complexity**: \( O(V^2) \) or \( O((V + E) \log V) \) with a priority queue.

---

### **Applications**
- Designing networks (e.g., roads, telecommunication).
- Circuit design.

---

## **8. Topological Sorting**

### **Definition**
- A linear ordering of vertices in a directed acyclic graph (DAG) such that for every edge \( u \to v \), \( u \) appears before \( v \).

---

### **Algorithm**
1. Perform a DFS and push vertices onto a stack after visiting all their neighbors.
2. Pop vertices from the stack to get the topological order.

- **Time Complexity**: \( O(V + E) \).

---

### **Applications**
- Task scheduling.
- Dependency resolution in build systems.

---

## **9. Graph Coloring**

### **Definition**
- Assign colors to vertices such that no two adjacent vertices have the same color.

---

### **Greedy Coloring Algorithm**
1. Assign the smallest available color to each vertex.
2. Ensure no two adjacent vertices share the same color.

- **Time Complexity**: \( O(V + E) \).

---

### **Applications**
- Map coloring.
- Register allocation in compilers.

---

### **Summary**
| **Algorithm**        | **Use Case**                      | **Time Complexity**   |
|-----------------------|------------------------------------|------------------------|
| DFS                  | Traversal, cycle detection        | \( O(V + E) \)         |
| BFS                  | Traversal, shortest path          | \( O(V + E) \)         |
| Dijkstra             | Shortest path (non-negative)      | \( O((V + E) \log V) \) |
| Bellman-Ford         | Shortest path (negative weights)  | \( O(V \times E) \)    |
| Floyd-Warshall       | All-pairs shortest path           | \( O(V^3) \)           |
| Kruskal              | Minimum spanning tree             | \( O(E \log E) \)      |
| Prim                 | Minimum spanning tree             | \( O(V^2) \) or better |