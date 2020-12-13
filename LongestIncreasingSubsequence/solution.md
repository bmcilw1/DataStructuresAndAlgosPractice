# 300. Longest Increasing Subsequence

https://leetcode.com/problems/longest-increasing-subsequence/

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, `[3,6,2,7]` is a subsequence of the array `[0,3,1,6,2,2,7]`.
 
## Explanation

This is a canonical dynamic programming (DP) problem. The process of solving this problem can be generalized to many DP problems.

The first step is to visualize what is being asked. It can help to have a very simple example.

Given
```
[0,3,1,6]
```

You get
```
0 -> 3 -> 6
0 -> 1 -> 6
3 -> 6
1 -> 6
```

The longest chain is the first or the second, either one is irreverent.

Each problem can be broken down into sub problems, and these sub-problems form a series of directed acyclic graph (DAG). This is the first telltale characteristic of a DP problem.

Now, let's see what happens when we add more elements to the end of the list, on the end that's pointed to by the DAG.

Given
```
[0,3,1,6,2,2,7]
```

You get
```
(0 -> 3 -> 6) -> 7
(0 -> 1 -> 6) -> 7
(3 -> 6) -> 7
(1 -> 6) -> 7
2 -> 7
2 -> 7
0 -> 1 -> 2 -> 7
```

Again, the top two are the longest.

Notice that the answer builds directly on top of the previous. This is the second characteristic of a DP problem, it can be broken up into a series of smaller problems. If these smaller problems are upstream of the direction of the DAG, you can usually find a way to just add on one more item to the end of the list while building on the computations you've already done to that point.

Also, notice how the last answer changed part of the answer chain from the subproblem before. This means that just because a solution is best for a subproblem, does not mean it will be for a larger problem. There is generally no greedy algorithm that works for a DP problem.

## Resources
* [This](https://www.youtube.com/watch?v=aPQY__2H3tE) video walks through this particular problem