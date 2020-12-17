# 322. Coin Change

https://leetcode.com/problems/coin-change/

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example:

Let's look at a few base cases

```
Input: coins = [1], amount = 1
Output: 1
```

The only coin needed is the coin given.

```
Input: coins = [10], amount = 0
Output: 0
```
No coins are required for a zero total.

```
Input: coins = [2], amount = 3
Output: -1
```

No possible number of coins exists to get exactly 3.


```
Input: coins = [1], amount = 2
Output: 2
```
Two copies of 1 are needed.

```
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
```

In this example, there are a lot of different possibilities.

1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1
2 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 
2 + 2 + 1 + 1 + 1 + 1 + 1 + 1 + 1
2 + 2 + 2 + 1 + 1 + 1 + 1 + 1
2 + 2 + 2 + 2 + 1 + 1 + 1
2 + 2 + 2 + 2 + 1 + 1 + 1

...

5 + 1 + 1 + 1 + 1 + 1 + 1
5 + 2 + 1 + 1 + 1 + 1
5 + 2 + 2 + 1 + 1
5 + 5 + 1

## Solution

With a shared coins array, this can be written as
Change(11) = Change(5) + Change(6)
Change(11) = Change(5) + Change(5) + Change(1)

Notice the multiple calls to Change(5). This indicates that this will be a DP problem.

We can now work on a recursive definition for Change.

Base cases:
If amount is zero, return 0 # No work
If amount in set(coins), return 1 # Exact change

These are the easier cases to cover. Now, we need to figure out how to know when an amount can't be given equal change.