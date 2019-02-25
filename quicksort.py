
arr = [1, 4, 2, 5, 7, 8, 34, 5, 43, 12, 76]


def quickSort(low, high):
    if low == high:
        return
    preLow = low
    preHigh = high
    key = low
    value = arr[key]
    while low < high:

        while arr[high] >= value and high > low:
            high -= 1
        arr[low] = arr[high]

        while arr[low] < value and low < high:
            low += 1
        arr[high] = arr[low]
    arr[low] = value
    quickSort(preLow, key)
    quickSort(key+1, preHigh)
    return arr

# 如果key不是第一个
def quickSort1(low, high):
    if low >= high:
        return
    preLow = low
    preHigh = high
    key = (low + high)//2
    print(key)
    value = arr[key]
    coverValue = arr[low]
    while low < high:

        while arr[high] >= value and high > low:
            high -= 1
        arr[low] = arr[high]

        while arr[low] < value and low < high:
            low += 1
        arr[high] = arr[low]
    if low < key and coverValue > value or low > key and coverValue < value:
        arr[low], arr[key] = value, coverValue
    else:
        arr[low], arr[key] = coverValue, value
    quickSort1(preLow, low)
    quickSort1(low+1, preHigh)
    return arr


print(quickSort1(0, len(arr)-1))