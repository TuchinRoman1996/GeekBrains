def sum_max(a, b, c):
    arr = [a, b, c]
    arr.remove(min(arr))
    res = arr[0] + arr[1]
    return res


print(sum_max(23, 2, 3))
