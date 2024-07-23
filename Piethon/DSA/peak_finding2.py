def find_peak_2d(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    def binary_search(row):
        low, high = 0, cols - 1

        while low <= high:
            mid = (low + high) // 2
            curr = matrix[row][mid]

            if (mid == 0 or curr >= matrix[row][mid - 1]) and (mid == cols - 1 or curr >= matrix[row][mid + 1]):
                return curr
            elif mid > 0 and curr < matrix[row][mid - 1]:
                high = mid - 1
            else:
                low = mid + 1

        return None

    def find_peak_recursive(start_row, end_row):
        if start_row == end_row:
            return binary_search(start_row)

        mid_row = (start_row + end_row) // 2
        max_value = max(matrix[mid_row])
        max_index = matrix[mid_row].index(max_value)

        if (mid_row == 0 or max_value >= matrix[mid_row - 1][max_index]) and (mid_row == rows - 1 or max_value >= matrix[mid_row + 1][max_index]):
            return max_value
        elif mid_row > 0 and max_value < matrix[mid_row - 1][max_index]:
            return find_peak_recursive(start_row, mid_row - 1)
        else:
            return find_peak_recursive(mid_row + 1, end_row)

    return find_peak_recursive(0, rows - 1)

matrix = [
    [1, 3, 2],
    [4, 6, 5],
    [7, 9, 8]
]
peak = find_peak_2d(matrix)
print("Peak element:", peak)
