## 75.Sort Color:
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

    Input: [2,0,2,1,1,0]
    Output: [0,0,1,1,2,2]

Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.

First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with a one-pass algorithm using only constant space?

```py
def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        try:
            nums is not None and nums != []
        except:
            return []
        
        l = 0
        r = len(nums) - 1
        color = 0
        
        ''' 以下注释部分为使用三根指针的方法 '''
        # while i <= r:
        #     if nums[i] == 0:
        #         nums[l], nums[i] = nums[i], nums[l]
        #         l = l + 1
        #         i += 1
        #     elif nums[i] == 1:
        #         i += 1
        #     elif nums[i] == 2:
        #         nums[r], nums[i] = nums[i], nums[r]
        #         r = r - 1
        #     else:
        #         pass
        # print(nums)
        
        '''Below is a straightforward method
        When l == r, cannot be sure if nums[l] == 0 or nums[l] > 0.'''
        for i in range(2):
            while True:
                while nums[l] == color and l < r:
                    l += 1
                while nums[r] > color and r >= 0:
                    r -= 1
                if l >= r:
                    break
                nums[l], nums[r] = nums[r], nums[l]
                
            r = len(nums) - 1
            color = 1
```
## *Sort Color II*
If there are k colors and n objects(numbers), the optimal solution is nlogk. The core algorithm is Partition Array.

1. Seperate the array into 2 parts. The left is less or equal to k // 2, The right is larger than k // 2
2. For each part(left and right), apply the first algorithm recursively.

## 915. Partition Array into Disjoint Intervals

Given an array A, partition it into two (contiguous) subarrays left and right so that:

Every element in left is less than or equal to every element in right.
left and right are non-empty.
left has the smallest possible size.
Return the length of left after such a partitioning.  It is guaranteed that such a partitioning exists.

 

Example 1:

    Input: [5,0,3,8,6]
    Output: 3
Explanation: left = [5,0,3], right = [8,6]

Example 2:

    Input: [1,1,1,0,6,12]
    Output: 4
Explanation: left = [1,1,1,0], right = [6,12]

```py
    def partitionDisjoint(self, A):
       maxleft = [A[0]]*len(A)
       for i in range(1,len(A)):
           maxleft[i] = max(maxleft[i-1], A[i])
           
       minright = [A[-1]]*len(A)
       for i in range(len(A)-2,-1,-1):
           minright[i] = min(minright[i+1], A[i]) 
       
       for i in range(len(A)-1):
           if maxleft[i] <= minright[i+1]:
               return i+1
```
2 passes solution:
skip the first maxleft pass, keep only the minright array, and use maxleft as a variable:

```py
    def partitionDisjoint(self, A):
       minright = [A[-1]]*len(A)
       for i in range(len(A)-2,-1,-1):
           minright[i] = min(minright[i+1], A[i]) 

       maxleft = -float('inf')
       for i in range(len(A)-1):
           maxleft = max(maxleft, A[i])  
           if maxleft <= minright[i+1]:
               return i+1
```

```py
# One pass solution:
class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        try:
            A is not None and A != []
        except:
            return []
        
        
        currMax = leftMax = A[0]
        res = 0
        
        for i in range(len(A)):
            currMax = max(currMax, A[i])
            if leftMax > A[i]:
                leftMax = currMax
                res = i
                
        return res+1
```