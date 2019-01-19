
import sys
import numpy as np
'''
class Solution:
    def __init__(self, N):
        self.N = N
        self.loc = np.zeros([N, N])
        self.result = []
        self.sum = 0

    def clear(self):
        self.loc = np.zeros([self.N, self.N])
        self.result = []

    def hturn(self, mat):
        h = np.zeros([self.N, self.N])
        for i in range(self.N):
            h[:][i] = mat[:][self.N-1-i]
        return h

    def vturn(self, mat):
        t = np.zeros([self.N, self.N])
        for i in range(self.N):
            t[i][:] = mat[self.N-1-i][:]
        return t

    def dturn(self, mat):
        d = np.zeros([self.N, self.N])
        for i in range(self.N):
            for j in range(self.N):
                d[i][j] = mat[self.N-1-j][self.N-1-i]
        return d

    def nqueens(self, ):
        if self.N % 2 == 0:
            half = self.N//2
        else:
            half = self.N//2+1
        for x in range(N):
            print(x)
            # clear the track before
            self.clear()
            # begin searching from [0, x]
            print(self.search(0, x), "*************")
        print("sum", self.sum)
        #print(self.result)


    def other(self):
        if len(self.result) > 0:
            rr0 = (self.result - self.loc).any(axis=1)
            if False not in rr0:
                self.result.append(self.loc)
                self.sum += 1
                print(self.loc)
        else:
            self.result.append(self.loc)
            self.sum += 1
            print(self.loc)
            
                h = self.hturn(self.loc)
                hh = (self.result - h).any(
                    axis=1)  # After subtracting h, there will be a zero matrix if h is already in self.result
                if False not in hh:
                    self.result.append(h)
                    self.sum += 1
                    print("horizontal turn: ", '\n', h)
                v = self.vturn(self.loc)
                ll = (self.result - v).any(axis=1)
                if False not in ll:
                    self.result.append(v)
                    self.sum += 1
                    print("vetical turn: ", '\n', v)
                t = self.loc.transpose()
                tt = (self.result - t).any(axis=1)
                if False not in tt:
                    self.result.append(t)
                    self.sum += 1
                    print("transpose: ", '\n', t)
                d = self.dturn(self.loc)
                dd = (self.result - d).any(axis=1)
                if False not in dd:
                    self.result.append(d)
                    self.sum += 1
                    print("diagonal turn: ", '\n', d)

                rotate90 = v.transpose()
                rr90 = (self.result - rotate90).any(axis=1)
                if False not in rr90:
                    self.result.append(rotate90)
                    self.sum += 1
                    print("clockwise rotate90: ", '\n', rotate90)
                rotate180 = self.hturn(v)
                rr180 = (self.result - rotate180).any(axis=1)
                if False not in rr180:
                    self.result.append(rotate180)
                    self.sum += 1
                    print("clockwise rotate180: ", '\n', rotate180)
                rotate270 = self.vturn(t)
                rr270 = (self.result - rotate270).any(axis=1)
                if False not in rr270:
                    self.result.append(rotate270)
                    self.sum += 1
                    print("clockwise rotate270: ", '\n', rotate270)
                




    def search(self, i, x):
        self.loc[i][:] = 0
        self.loc[i][x] = 1
        if i >= self.N-1:
            self.other()
            self.loc[i][:] = 0
            return i
        else:
            available = np.arange(self.N)
            diff = np.array([])
            r = np.array([])
            j = i + 1

            for num in range(j):
                # print("?", num, np.where(self.loc[num]))
                reached = np.where(self.loc[num] == 1)[0]
                diff = np.concatenate((diff, reached + j - num))
                diff = np.concatenate((diff, reached - j + num))
                diff = np.concatenate((diff, reached))
                # print("reached", reached)
                r = np.concatenate((r, reached))
            available = np.array([a for a in available if a not in diff])
            #print(i, x, j, r, '\n', diff, '\n', available)
            if available.size == 0:
                return -1
            else:
                for y in available:
                    return self.search(j, y)  # 注意递归函数的返回值 堆栈


'''
# 回溯法：
# 0. a[i]
# 1. 寻找这一行看是否有可以放置的点，如果可以，转2。如果不行，且a=0,退出，否则，转4
# 2  if（a==N-1）且i不是最后一个，继续遍历这一行,看是否有可以放置的点，直到i是最后一个；else 转3
# 3  a = a+1 转1
# 4  a = a-1 转1


def Nqueen(n):
    result = []
    item = [-1] * n
    columns = [True]*n + [False]
    adds = [True]*n*2
    reduces = [True]*n*2
    x = y = 0

    while True:
        if columns[y] and adds[x+y] and reduces[y-x+n]:
            item[x] = y
            columns[y] = adds[x + y] = reduces[y - x + n] = False
            x += 1
            y = 0
            if x == n:
                result.append(['X'*y+'Q'+'X'*(n-y-1) for y in item])
        else:
            y += 1
            while y > n-1 and x!=0:
                x -= 1
                y = item[x] + 1
                columns[item[x]] = adds[x+item[x]] = reduces[item[x]-x+n] = True
            if y > n-1 and x==0:
                length = len(result)
                for i in range(length):
                    print(result[i])
                print(length)

                return

if __name__ == "__main__":
    Nqueen(8)
