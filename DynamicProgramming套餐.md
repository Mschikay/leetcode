## 75. Sort Colors
## 795. number of subarrays with bounded maximum
We are given an array A of positive integers, and two positive integers L and R (L <= R).

Return the number of (contiguous, non-empty) subarrays such that the value of the maximum array element in that subarray is at least L and at most R.

Example :

    Input: 
    A = [2, 1, 4, 3]
    L = 2
    R = 3
    Output: 3

Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].

Note:

L, R  and A[i] will be an integer in the range [0, 10^9].
The length of A will be in the range of [1, 50000].

#### 一般地，给了这种数组长度的提示就是要用O(n)

#### 这道题用到了动态规划结合Prefix array！

```py
class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        start = end = -1
        res = 0

        for i in range(len(A)):
            '''如果这个数在least maximum以下，那么子串的个数要加上当前位置的prefix的个数。prefix指的是[start:i+1], [start+1: i+1], ..., [end:i+1]. prefix一定是包含了合法的maximum的。如果start == end,prefix为0，即当前位置之前没有出现合法的maximum'''
            if A[i] < L:
                i += 1
                res += end - start
                continue

            '''如果超过合法的maximum，要重置start和end'''
            if A[i] > R:
                start = end = i
                continue

            '''如果当前位置是一个合法的maximum，同样加上当前位置的prefix'''
            end = i
            res += end - start
        return res
```

#### *存在subarray，统计个数，试着考虑多个指针、prefix*

## 516 Longest Polindromic Subsequence
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
    
    Input:
    "bbbab"
    Output:
    4
One possible longest palindromic subsequence is "bbbb".

Example 2:

    Input:
    "cbbd"
    Output:
    2
One possible longest palindromic subsequence is "bb".

首先，注意这是 sequence 而不是string。sequence是不需要连续的！

假设子序列是以位置j开头，以位置i结尾，那么

当s[i] == s[j]时，longest(i,j)=2+longest(j+1,i-1)

当s[i] != s[j]时，longest(i,j)=longest(j+1,i) or longest(j, i-1).

因此，从小到大遍历i，从大到小遍历j

```py
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if s is None or s == "":
            return 0

        dp = [[1 for i in range(len(s))]for j in range(len(s))]
        for i in range(len(s)):
            for j in range(i, -1, -1):
                if s[i] != s[j]:
                    dp[i][j] = max(dp[i-1][j], dp[i][j+1])
                else:
                    if i - j > 2:
                        dp[i][j] = 2 + dp[i-1][j+1]
                    else:
                        dp[i][j] = 1 + i - j

        return dp[len(s)-1][0]


        preDp = [1 for i in range(len(s))]
        dp = [1 for i in range(len(s))]

    # 以下是仅使用一维数组交替存储的方法
    # tricky的地方是换指针（line116-118）  
    # 因为当前行更新只与前一行的数值有关
    def longestPalindromeSubseq1(self, s: str) -> int:    
        for i in range(len(s)):
            for j in range(i, -1, -1):
                if s[i] != s[j]:
                    dp[j] = max(preDp[j], dp[j+1])
                else:
                    if i - j > 2:
                        dp[j] = 2 + preDp[j+1]
                    else:
                        dp[j] = 1 + i - j
            p = preDp
            preDp = dp
            dp = p
        return preDp[0]
```

## 5. Longest Palindromic Substring
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

    Input: "babad"
    Output: "bab"

Note: "aba" is also a valid answer.

Example 2:

    Input: "cbbd"
    Output: "bb"

这道题目的解与Longest Subsequence差不多。但不需要维护最长的值了，只需要用Boolean type。解法内核是一样的。

#### 怎么用中心扩散法做？


## 647. Palindromic Substrings
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

    Input: "abc"
    Output: 3

Explanation: Three palindromic strings: "a", "b", "c".
 

Example 2:

    Input: "aaa"
    Output: 6
    
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Note:

The input string length won't exceed 1000.


