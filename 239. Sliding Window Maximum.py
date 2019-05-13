from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k):

        i, j = 0, k - 1
        N = len(nums)
        res = []
        m = float("-inf")
        idx = -1

        while j < N:
            if i <= idx:
                if nums[j] > m:
                    m = nums[j]
                    idx = j
            else:
                m = float("-inf")
                for n in range(i, j + 1):
                    # print(n,nums[n])
                    if nums[n] > m:
                        m = nums[n]
                        idx = n
            res.append(m)
            i += 1
            j += 1

        return [] if not nums else res

    def maxSlidingWindow1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Checking for base case
        if not nums:
            return []
        if k == 0:
            return nums
        # Defining Deque and result list
        deq = deque()
        result = []

        # First traversing through K in the nums and only adding maximum value's index to the deque.
        # Note: We are olny storing the index and not the value.
        # Now, Comparing the new value in the nums with the last index value from deque,
        # and if new valus is less, we don't need it

        for i in range(k):
            while len(deq) != 0:
                if nums[i] > nums[deq[-1]]:
                    deq.pop()
                else:
                    break

            deq.append(i)
            print(i, deq)
        # Here we will have deque with index of maximum element for the first subsequence of length k.

        # Now we will traverse from k to the end of array and do 4 things
        # 1. Appending left most indexed value to the result
        # 2. Checking if left most is still in the range of k (so it only allows valid sub sequence)
        # 3. Checking if right most indexed element in deque is less than the new element found, if yes we will remove it
        # 4. Append i at the end of the deque  (Not: 3rd and 4th steps are similar to previous for loop)

        for i in range(k, len(nums)):
            result.append(nums[deq[0]])

            if deq[0] < i - k + 1:
                deq.popleft()

            while len(deq) != 0:
                if nums[i] > nums[deq[-1]]:
                    deq.pop()
                else:
                    break

            deq.append(i)

        # Adding the maximum for last subsequence
        result.append(nums[deq[0]])

        return result

s = Solution()
s.maxSlidingWindow1([8, 9, 7, 6, 6, 7], 3)