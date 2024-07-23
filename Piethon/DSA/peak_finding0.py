def find_peak(arr):
    n = len(arr)
    low, high = 0, n - 1

    while low <= high:
        mid = (low + high) // 2

        if (mid == 0 or arr[mid] >= arr[mid - 1]) and (mid == n - 1 or arr[mid] >= arr[mid + 1]):
            return arr[mid]
        elif mid > 0 and arr[mid] < arr[mid - 1]:
            high = mid - 1
        else:
            low = mid + 1

    return None

array = [1, 3, 5, 4, 2]
peak = find_peak(array)
print("Peak element:", peak)
