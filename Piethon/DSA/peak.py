def find_peak(list_of_integers):
    """
    Finds the peak element in a 1D list_of_integersay.

    Args:
        list_of_integers: The unsorted list_of_integersay to search.

    Returns:
        The peak element.
    """

    if not list_of_integers:
        return None

    n = len(list_of_integers)
    low, high = 0, n - 1

    while low < high:
        mid = (low + high) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return (list_of_integers[low])
