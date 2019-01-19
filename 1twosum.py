import sys


def twosum(arr, target):
    seen = {}
    for i, n in enumerate(arr):
        if target-n in seen:
            print(seen[target-n], i)
        seen[n] = i

if __name__ == "__main__":
    # x = sys.argv[1].split(',')
    # for i in range(len(x)):
    #     x[i] = int(x[i])
    # target = int(sys.argv[2])
    x = [2, 7, 11, 15, 6, 3]
    target = 9
    twosum(x, target)

