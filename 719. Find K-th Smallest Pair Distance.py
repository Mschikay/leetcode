import sys


class Solution:
    def smallestDistancePair(self, nums, k):
        if nums is None or nums == []:
            return None

        nums.sort()
        interval = [nums[i] - nums[i - 1] for i in range(1, len(nums))]
        interval.sort()
        print(interval)
        # bfs
        queue = [([], -1)]
        q = 0
        length = 0
        while q < len(queue):
            total, i = queue[q][0], queue[q][1]
            for j in range(i + 1, len(interval)):
                length += 1
                queue.append((total + [interval[j]], j))
                if length < 23:
                    print(length, queue, '\n')
            q += 1
        queue.sort()
        return queue[k][0]


if __name__ == "__main__":
    s = Solution()
    s.smallestDistancePair([9,10,7,10,6,1,5,4,9,8], 18)