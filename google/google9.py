# 一道是用水壶从左到右一排植物浇水，一个int[] 代表每个植物需要得水，一个int代表水壶容量，每个植物必须一次浇完，要是水壶剩余的水不够，必须走回起点处加满水再过来，算总的步数。


def water(p, c):
    curRest = c
    i = step = 0

    while i < len(p):
        if curRest >= p[i]:
            curRest -= p[i]
            step += 1
            i += 1
            print(step, i)
        else:
            step += 2 * i
            curRest = c

    return step


if __name__ == "__main__":
    print(water([1, 2, 3, 5, 6, 4], 17))