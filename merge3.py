def split(arr):
    nums = [[] for i in range(3)]
    if len(arr) <= 3:
        for i in range(len(arr)):
            nums[i % 3].append(arr[i])
        a1, a2, a3 = nums
    else:
        for i in range(len(arr)):
            nums[i % 3].append(arr[i])
        a1, a2, a3 = split(nums[0]), split(nums[1]), split(nums[2])
    ret = merge3(a1, a2, a3)
    return ret


def merge2(a1, a2):
    i = j = 0
    arr = []
    while i < len(a1) and j < len(a2):
        if a1[i] <= a2[j]:
            arr.append(a1[i])
            i += 1
        else:
            arr.append(a2[j])
            j += 1
    arr += a1[i:] or a2[j:]
    return arr


def merge3(a1, a2, a3):
    # print(a1, a2, a3)
    i = j = k = 0
    arr = []
    while i < len(a1) and j < len(a2) and k < len(a3):
        if a1[i] <= a2[j] and a1[i] <= a3[k]:
            arr.append(a1[i])
            i += 1
        elif a2[j] <= a1[i] and a2[j] <= a3[k]:
            arr.append(a2[j])
            j += 1
        else:
            arr.append(a3[k])
            k += 1
    if not a1[i:]:
        arr += merge2(a2[j:], a3[k:])
    elif not a2[j:]:
        arr += merge2(a1[i:], a3[k:])
    else:
        arr += merge2(a1[i:], a2[j:])
    return arr

print(split([5,4,3,4,8,5,3,21,3,4,543,52,3]))