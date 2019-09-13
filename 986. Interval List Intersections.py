class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        a = b = 0
        res = []
        while a < len(A) and b < len(B):
            la, ra = A[a]
            lb, rb = B[b]
            if not rb < la and not ra < lb:
                arr = sorted([la, lb, ra, rb])
                res.append([arr[1], arr[2]])
            if ra < rb:
                a += 1
            else:
                b += 1
        return res
        # events = []
        # for a, b in A:
        #     events.append([a, 1])
        #     events.append([b, -1])
        # for a, b in B:
        #     events.append([a, 1])
        #     events.append([b, -1])
        # events = sorted(events, key=lambda x:(x[0], -x[1]))
        # c = 0
        # ans = []
        # for time, status in events:
        #     pre = c
        #     if status == 1:
        #         c += 1
        #     else:
        #         c -= 1
        #     if c == 2:
        #         ans.append([time, 0])
        #     elif pre == 2 and c == 1:
        #         ans[-1][-1] = time
        # return ans