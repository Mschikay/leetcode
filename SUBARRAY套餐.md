这几天一直在做关于数组的题目，大概都和subarray有关。所以整理一下

# 一根指针
## Maximum Subarray
```
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:
```
这是一道简单的动态规划。当前位置的最大值如果不是自己本身，那么就是前一个位置的最大值加上自己

```
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
```
## Maximum Product Subarray
```
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

    Input: [2,3,-2,4]
    Output: 6
    Explanation: [2,3] has the largest product 6.
Example 2:

    Input: [-2,0,-1]
    Output: 0

Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
```
这道题类似于求和最大的子数组。但乘法由于有负数略有不同。除了需要维护当前的最大值，还有当前的最小值。因为当前位置的最大值可能是本身，或本身与前一个最大值的积，或本身与前一个最小值的积。这是因为乘数中有负数的原因。

这个方法无需考虑为不为零，也是动态规划

## Subarray Sum Equals K
```
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
```
不同于*subarray product less than k*那道题目。在那道题目中，向右移动乘积总是增大，向左乘积总是减小。在这里使用两根指针没有这种保证。

但这道题也很tricky。使用了prefix array，维护了从0开始，到每一个位置的子数组的和。任意子数组之间的和可以通过差得到。

假设一个子数组a[0, i]本身由两个子数组a1[0, j], a2[j+1, i]构成:

subSum(a) == subSum(a1) + subSum(a2)

令SubSum(a2) == k，判断有没有subSum(a1) == subSum(a) - k即可

用字典存储，一次遍历就可以完成。
# 两根指针
## Subarray Product Less Than K
```
Your are given an array of **positive integers** nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:

    Input: nums = [10, 5, 2, 6], k = 100
    Output: 8

Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].

Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.
```
这道题目竟然是用两个指针！右指针控制乘，左指针控制除。在不超过k的情况下，右指针会一直往右移动，直到>=k。此时，移动左指针使subarray的乘积回归到k以内。

比较tricky的地方是，左指针无需遍历整个数组，左右指针之间的距离就可以决定这之中有多少个合法的子数组

这道题显然并不需要数组是有序数列！！
## 2Sum Input array is sorted
```
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
```
两个指针从两端开始往中间搜索。这样的操作使得最开始两个位置的数字的和处于中位数。右指针往左移，和会越来越小；左指针往右移，和会越来越大。这样就一定可以遍历到等于target的数组对了！并且时间复杂度只有O(n)
## 3Sum
```
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
```
和2Sum的解决方法核心一模一样，先将数组排好序即可。

由于多了一个数，时间复杂度O(n^2)

**注意**，需要考虑去重。但只有在恰好和为target时才需要去重。不为target时，去不去重对于结果没有影响。

## 3Sum closest
```
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
```
指针还是从两端往中间走。需要注意，这个当下最接近的和比target小还是大。如果小，为了更接近target，应当向右挪动左指针，反之，向左挪动右指针。

总而言之，两端的指针可以遍历出所有的和，用这个就没错了。