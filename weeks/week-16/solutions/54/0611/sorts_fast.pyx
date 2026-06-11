def bubble_sort(data):
    cdef int i, j, n
    cdef list result = list(data)
    n = len(result)
    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


def quick_sort(data):
    cdef int n = len(data)
    if n < 2:
        return list(data)
    cdef int pivot = data[0]
    cdef list left = [x for x in data[1:] if x <= pivot]
    cdef list right = [x for x in data[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


def merge_sort(data):
    cdef int n = len(data)
    if n < 2:
        return list(data)
    cdef int mid = n // 2
    return _merge(merge_sort(data[:mid]), merge_sort(data[mid:]))


cdef list _merge(list left, list right):
    cdef list result = []
    cdef int i = 0, j = 0
    cdef int nL = len(left), nR = len(right)
    while i < nL and j < nR:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
