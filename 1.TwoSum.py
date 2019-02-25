class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        try:
            assert nums is not None and len(nums) >= 2
        except:
            return []


        number = {}
        for i in range(len(nums)):
            number.setdefault(nums[i], [])
            number[nums[i]].append(i)

        for i in range(len(nums)):
            if nums[i] == target - nums[i]:
                if len(number.get(nums[i], None)) > 1:
                    return ([number[nums[i]][0], number[target - nums[i]][1]])
                else:
                    continue
            if number.get(nums[i], None) and number.get(target - nums[i], None):
                return ([number[nums[i]][0], number[target - nums[i]][0]])
        return []