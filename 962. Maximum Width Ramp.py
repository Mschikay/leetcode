# Use two array to solve this problem. min_arr[i] is the minimum of the first i + 1 elements of A, max_arr[j] is the maximum of the last len(A) - j elements of A.
#
# The idea of this solution is: Suppose (i, j) is the answer, then A[i] must be the smallest element among the first i + 1 elements of A and A[j] must be the largeset element among the last len(A) - j elements of A. Otherwise, we can always find an element smaller than A[i] or larger than A[j], so that (i, j) is not the maximum width ramp.
#
# For example, the input is [6, 0, 8, 2, 1, 5]. Then min_arr=[6, 0, 0, 0, 0, 0] and max_arr=[8, 8, 8, 5, 5, 5].
#
# We can find the ramp use two points, left and right. left starts from the beginning of min_arr[i] and right starts from the beginning of max_arr[i]. Increase right by 1 when min_arr[left] <= max_arr[right], else increase left by 1.

# def maxWidthRamp(self, A):
#     min_arr = [A[0]] * len(A)
#     for i in range(1, len(A)):
#         min_arr[i] = min(min_arr[i - 1], A[i])
#     max_arr = [A[-1]] * len(A)
#     for i in range(len(A) - 2, -1, -1):
#         max_arr[i] = max(max_arr[i + 1], A[i])
#
#     ans = 0
#     left = 0
#     right = 0
#     while right < len(A):
#         if min_arr[left] <= max_arr[right]:
#             ans = max(ans, right - left)
#             right += 1
#         else:
#             left += 1
#     return ans

# 使用栈
class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        if A is None or len(A) <= 1:
            return 0

        stack = [0]
        for i in range(1, len(A)):
            if A[i] <= A[stack[-1]]:
                stack.append(i)

        r = len(A) - 1
        l = len(stack) - 1
        w = 0
        while l >= 0:
            if A[r] >= A[stack[l]]:
                if r > stack[l]:
                    w = max(w, r - stack[l])
                l -= 1
            else:
                r -= 1
        return w

# 不使用栈，但也是两根指针
# 只与索引有关
class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        pair = []
        for i, k in enumerate(A):
            pair.append((k, i))

        pair.sort()
        index = [p[1] for p in pair]
        w = l = 0
        r = 1

        while r < len(index):
            if index[r] >= index[l]:
                if l != r:
                    w = max(w, index[r] - index[l])
                r += 1
            else:
                l += 1

        return w
