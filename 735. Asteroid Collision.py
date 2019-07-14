

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for a in asteroids:
            cur = a
            while cur < 0 and st and st[-1] > 0:
                x = st.pop()
                if abs(cur) > abs(x):
                    cur = cur
                elif abs(cur) < abs(x):
                    cur = x
                else:
                    cur = None
                    break
            if cur: st.append(cur)
        return st