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

Each problem can be broken down into sub problems, and these sub-problems form a series of directed acyclic graphs (DAG). It's directed because we can only go one way through the graph. It's acyclic because there are no edges going to prior elements or creating loops. This is the first telltale characteristic of a DP problem.

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
[0 -> 1] -> 2 -> 7  # [0 -> 1] would have been taken into account in the subset [0, 3, 1]
```

Again, the top two are the longest.

Notice that the answer builds directly on top of the previous. This is the second characteristic of a DP problem, it can be broken up into a series of smaller problems. If these smaller problems are upstream of the direction of the DAG, you can usually find a way to just add on one more item to the end of the list while building on the computations you've already done to that point.

Also, notice how the last answer changed part of the answer chain from the subproblem before. This means that just because a solution is best for some subproblem, does not mean that solution will be best for a larger problem. However, the part (0 -> 1) would have been contained in an even smaller sub-problem (before adding the 6).

There is generally no greedy algorithm that works for a DP problem. For a given LIS of k, you need to take into account the answers to all LIS from 0 to k-1, not just the k-1 case / not just the last best overall case. This means there is not going to be any O(N) solution to this particular problem.

## First Solution

The first way we can solve this is by starting at the beginning of the list and asking what's the longest increasing subsequence ending at element k? For k=0, the answer is 1, or just the one node. In general, we get the following relation.

```
LIS(nums, k) = 1 + max(LIS(j) for all j < k where nums[j] < nums[k])
```

If we compute that for all k, our final answer is `LIS(nums, N-1)`. N-1 is passed due to zero-based indexing of arrays. If we store answers to LIS in an array of size N, then `LIS(nums, N-1) = LIS[N-1]`

If we compute LIS for all k < n with the nested for loop, we get a solution that runs in O(N^2) time and taking O(N) space (for storing the LIS array).

## Resources
* [This](https://www.youtube.com/watch?v=aPQY__2H3tE) video walks through this particular problem