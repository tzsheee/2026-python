def linear_search(data: list, target) -> int:
    for index, value in enumerate(data):
        if value == target:
            return index
    return -1


def binary_search(data: list, target) -> int:
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
