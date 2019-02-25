nums = [int(x) for x in input().split()]
middle1 = [[4, 5], [6, 7], [8, 9], [22, 23]]
middle2 = [0, 2, 3, 1]
front1 = [2, 3, 8, 14, 17, 16, 11, 5]
front2 = [6, 7, 13, 12]
right1 = [[1, 3], [21, 23], [17, 19], [7, 13]]
right2 = [8, 9, 15, 14]


def operate(i, clockwise, surface):
    if surface == "middle":
        if clockwise == 0:
            first1 = middle1[0]
            first2 = middle2[0]
            for i in range 3:
                middle1[i] = middle1[i + 1]
                middle2[i] = middle2[i + 1]
            middle1[3] = first1
            middle2[3] = first2
        else:
            last1 = middle1[-1]
            last2 = middle2[-1]
            for i in range(3, 0, -1):
                middle1[i] = middle1[i - 1]
                middle2[i] = middle2[i - 1]
            middle1[0] = last1
            middle2[0] = last2

    if surface == "front":
        if clockwise == 0:
            first1 = front1[0]
            first2 = front2[0]
            for i in range 3:
                front1[i] = front1[i + 1]
                front2[i] = front2[i + 1]
            front1[3] = first1
            front2[3] = first2
        else:
            last1 = front1[-1]
            last2 = front2[-1]
            for i in range(3, 0, -1):
                front1[i] = front1[i - 1]
                front2[i] = front2[i - 1]
            front1[0] = last1
            front2[0] = last2

    if surface == "right":
        if clockwise == 0:
            first1 = right1[0]
            first2 = right2[0]
            for i in range(3):
                right1[i] = right1[i + 1]
                right2[i] = right2[i + 1]
            right1[3] = first1
            right2[3] = first2
        else:
            last1 = right1[-1]
            last2 = right2[-1]
            for i in range(3, 0, -1):
                right1[i] = right1[i - 1]
                right2[i] = right2[i - 1]
            right1[0] = last1
            right2[0] = last2


def



