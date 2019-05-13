
#arr = [1, 4, 2, 5, 7, 8, 1, 5, 43, 12, 76]
# def quickSort(low, high):
#     if low == high:
#         return
#     preLow = low
#     preHigh = high
#     key = low
#     value = arr[key]
#     while low < high:
#         while arr[high] >= value and high > low:
#             high -= 1
#         arr[low] = arr[high]
#
#         while arr[low] < value and low < high:
#             low += 1
#         arr[high] = arr[low]
#     arr[low] = value
#     quickSort(preLow, key)
#     quickSort(key+1, preHigh)
#     return arr
#
# # 如果key不是第一个
# def quickSort1(low, high):
#     if low >= high:
#         return
#     preLow = low
#     preHigh = high
#     key = (low + high)//2
#     print(key)
#     value = arr[key]
#     coverValue = arr[low]
#     while low < high:
#
#         while arr[high] >= value and high > low:
#             high -= 1
#         arr[low] = arr[high]
#
#         while arr[low] < value and low < high:
#             low += 1
#         arr[high] = arr[low]
#     if low < key and coverValue > value or low > key and coverValue < value:
#         arr[low], arr[key] = value, coverValue
#     else:
#         arr[low], arr[key] = coverValue, value
#     quickSort1(preLow, low)
#     quickSort1(low+1, preHigh)
#     return arr
# print(quickSort(0, len(arr)-1))


'''
time complexity, worst: n^2, average: nlogn
space: logn, because of recursive calls
'''

def quicksort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quicksort(arr, low, p - 1)
        quicksort(arr, p + 1, high)
    return arr

def partition(arr, low, high):
    pv = arr[low]
    buck = low
    while low < high:
        while high > low and arr[high] > pv:
            high -= 1
        arr[buck] = arr[high]
        buck = high
        while high > low and arr[low] <= pv:
            low += 1
        arr[buck] = arr[low]
        buck = low
    arr[buck] = pv
    return buck


def quicksorti(arr):
    s = [(0, len(arr) - 1)]
    while s:
        low, high = s.pop()
        if low < high:
            p = partition(arr, low, high)
            s.append((low, p - 1))
            s.append((p + 1, high))
    print(arr)
    return arr


a = [1, 4, 2, 5, 7, 8, 1, 5, 43, 12, 76]
# l = len(a) - 1
# res = quicksort(a, 0, l)
# print(res)
quicksorti(a)