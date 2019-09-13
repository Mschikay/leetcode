class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        i = 0
        while i < len(gas):
            num = 0
            rest = 0
            j = i
            while num < len(gas):
                x = j % len(gas)
                rest += gas[x] - cost[x]
                num += 1
                j += 1

                if rest < 0:
                    i += num
                    break
                else:
                    if num == len(gas): return i

        return -1