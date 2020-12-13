# 300. Longest Increasing Subsequence

https://leetcode.com/problems/longest-increasing-subsequence/

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, `[3,6,2,7]` is a subsequence of the array `[0,3,1,6,2,2,7]`.
 
## Explanation

This is a canonical dynamic programming (DP) problem. The process of solving this problem can be generalized to many DP problems.

The first step is to visualize what is being asked. It can help to have a very simple example.

Given
[0,3,1,6]

You get
0 -> 3 -> 6
0 -> 1 -> 6
3 -> 6
1 -> 6

The longest chain is the first or the second, either one is irreverent.

Each problem can be broken down into sub problems, and they form a series of directed acyclic graph (DAG).

Given
[0,3,1,6,2,2,7]
0 -> 3 -> 6
0 -> 1 -> 6
3 -> 6
1 -> 6

### Resources
* [This](https://www.youtube.com/watch?v=aPQY__2H3tE) video walks through this particular problem