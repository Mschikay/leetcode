# 图
## 注意
### 785 二分图
可能有多个连通子块！
二维数组，要考虑空数组在不同位置的情况

### 79
递归需要循环调用函数的时候，如果有
```py
def dfs(n, b)
  for i in a:
      dfs(i, b+[x])
```
要注意这个b是会变化的,所以不能对其修改。即便要改，要在下一次循环之前改回原来的b。否则会在下一次dfs时，b可能已经不是原来的b了……

这个b也可以先深拷贝。
不过在使用深拷贝的时候需要慎重，阅读过源码的都知道，深拷贝需要维护一个 memo 用于记录已经拷贝的对象，这是它比较慢的原因。在绝大多数情况下，程序里都不存在相互引用。但作为通用模块，Python 深拷贝必须为了这 1% 情形，牺牲 99% 情形下的性能。

### 212 word search2
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example:

Input: 
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

Output: ["eat","oath"]

***
核心：DFS 字典树trie

见 leetcode/212wordsearch2.py

### Gray Code
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

Example 1:
```
Input: 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2

For a given n, a gray code sequence may not be uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence.

00 - 0
10 - 2
11 - 3
01 - 1
```
For this kind of problem, the most efficient method is to find a pattern for these numbers. 

can also use dfs to solve it.
But for dfs, f(k) = nf(k-1), while n is the number of bits. Max k is 2**(n-1).
When you input an n as small as n, you would meet "RecursionError: maximum recursion depth exceeded in comparison"
 