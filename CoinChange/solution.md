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

1. If amount is zero, return 0 # No work
2. If amount in set(coins), return 1 # If one coin is possible, this is the best option

These are the easier cases to cover. Now, we need to figure out how to know when an amount can't be given equal change.

3. If amount < min(set(coins)), we know there is no change possible.

Recursive case:

4. For each coin in set(coins), we can try to make change with 1 + change(amount-coin). We can then say that the final answer is the min of those each answer given that are greater than -1. If no answer exists, we return -1.

> Note, case 2 can be included in case 4. However, we will save a few cpu cycles by separating it.

```
Let N = length(coins), M = amount
```

The time complexity is given by O(NM). This is because the recursive call stack will be called at worst M times and each call will walk through the set of coins of length N at worst.

The space complexity is O(M). This is because the recursive call stack will be M worst case. We can read the list of coins directly so N has no effect on space complexity.
