class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        def find(start, t):
            l, h = start, len(numbers) - 1
            while l <= h:
                mid = (l + h) // 2
                if numbers[mid] == t:
                    return mid
                if numbers[mid] > t:
                    h = mid - 1
                if numbers[mid] < t:
                    l = mid + 1
            return l

        for i in range(len(numbers)):
            idx = find(i + 1, target - numbers[i])
            if idx < len(numbers) and target - numbers[i] == numbers[idx]:
                return [i + 1, idx + 1]
        return []