lists = []

def buildHeap():
    length = len(lists)

    start = (length + 1) // 2 - 1
    while start >= 0:
        print('start', start)
        adjust(start)
        start -= 1
        # for j in range(0, length):
        #     print(lists[j].val)
    return


def adjust(i):
    length = len(lists)

    if not length or lists[i] is None:
        return

    # have 2 children
    if 2 * i + 2 < length:
        if lists[2 * i + 1].val <= lists[i].val and lists[2 * i + 1].val <= lists[2 * i + 2].val:
            lists[2 * i + 1], lists[i] = lists[i], lists[2 * i + 1]
            adjust(2 * i + 1)
        elif lists[2 * i + 2].val <= lists[i].val and lists[2 * i + 2].val <= lists[2 * i + 1].val:
            lists[2 * i + 2], lists[i] = lists[i], lists[2 * i + 2]
            adjust(2 * i + 2)
        return

    # have one child
    elif 2 * i + 1 < length:
        if lists[i].val > lists[2 * i + 1].val:
            lists[i], lists[2 * i + 1] = lists[2 * i + 1], lists[i]
            adjust(2 * i + 1)
        return

    else:
        return


def getMin():
    minNode = lists[0]
    lists[0] = lists[-1]
    del lists[-1]

    adjust(0)

    return minNode