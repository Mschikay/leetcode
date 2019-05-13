# 1
# 2
# 就是说 第1行第1个是queen 第2行第2个是queen，并保证输入的数字不重复，这样可以得出一个结论：同一行 同一列不会出现2个queen。
# 题目要求是求出 对于每个Queen， 最大的威胁次数，威胁指只要一个queen所能移动的范围内有别的queen就算威胁 P.S.同一方向上有2个queen威胁你 只算最近的那个。
# 由于同一行 同一列不会出现2个queen。（由于输入限制）所以只要考虑对角线 和逆对角线。
# 举个例子： 棋盘是：
# 100           ---- 1号 queen
# 010           ---- 2号 queen
# 001           ---- 3号 queen
# 1号和3号queen的受威胁次数都是1， 2号是2（被1和3） 所以答案是2
# 这题我是建了2个hash表 一个是正对角线一个逆对角线来表示对角线上是否有别的queen.
# 从row 0 开始到 最后行， 对于输入的 column位置 先判定 hash表是否有别的Queen没的话就set 1 继续下一行
# 有的话就threats[row]++ 然后向那个方向追踪是谁给你的威胁，把那个点的threat也++ 就好了。

class Solution:
    def queen(self, q):
        count = [[0, 0] for i in range(len(q))]

        for i in range(len(q)):
            for j in range(i+1, len(q)):
                if j - i == abs(q[i] - q[j]):
                    if count[i][0] == 1:
                        pass
                    else:
                        count[i][0] += 1
                    if count[j][1] == 1:
                        pass
                    else:
                        count[j][1] = 1

        return [sum(c) for c in count]


if __name__ == "__main__":
    s = Solution()
    print(s.queen([0, 1, 4, 2, 3]))
