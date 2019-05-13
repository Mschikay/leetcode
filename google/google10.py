# 一道是两排骰子互换的，两排骰子的值，对应位置的骰子可以互换，问最少的交换次数使其中一排变为一排一样的数。
import sys


def xdice(d1, d2):
    time = [0 for i in range(6)]
    dice = {}

    for i, k in enumerate(d1):
        index = dice.setdefault(k, [])
        index.append(i)

    for i, k in enumerate(d2):
        value = dice.get(k, [])
        if i not in value:
            time[k] += 1
            dice.setdefault(k, []).append(i)
        else:
            continue

    minx = sys.maxsize
    for k, v in dice.items():
        if len(v) == len(d1):
            minx = min(minx, time[k])

    if minx == sys.maxsize:
        return None

    return minx


if __name__ == "__main__":
    print(xdice([3, 1, 1, 1, 1, 1], [2, 1, 1, 2, 3, 2]))