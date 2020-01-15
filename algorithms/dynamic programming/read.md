# Dynamic Programming

Dynamic programming and the counterpart greedy methods are ways to solve
optimization problems. Optimization problems mean, we want to either find
max or min of some problem.

Dynamic programming works on `principle of optimality` which says, a sequence
of decisions need to be taken to come to the best solution.

### Tabulation and Memoization
When you solve a dynamic programming problem using __tabulation__ you solve the 
problem "bottom up", i.e., by solving all related sub-problems first, typically 
by filling up an n-dimensional table. Based on the results in the table, 
the solution to the "top" / original problem is then computed.

If you use memoization to solve the problem you do it by maintaining a map of 
already solved sub problems. You do it "top down" in the sense that you solve 
the "top" problem first (which typically recurses down to solve the sub-problems).
