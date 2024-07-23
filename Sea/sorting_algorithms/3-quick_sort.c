#include "sort.h"
#include <stdio.h>

/**
 * swap - Swap two integers.
 * @x: Pointer to the first integer.
 * @y: Pointer to the second integer.
 */
void swap(int *x, int *y)
{
	int temp = *x;
	*x = *y;
	*y = temp;
}

/**
 * lomuto_partition - Partition the array for quicksort using Lomuto scheme.
 * @array: Array to be partitioned.
 * @low: Starting index.
 * @high: Ending index.
 *
 * Return: Index of the pivot element.
 */
int lomuto_partition(int *array, int low, int high)
{
	int pivot = array[high];
	int i = low - 1;

	for (int j = low; j < high; j++)
	{
		if (array[j] <= pivot)
		{
			i++;
			swap(&array[i], &array[j]);
		}
	}

	swap(&array[i + 1], &array[high]);
	return (i + 1);
}

/**
 * quick_sort_recursive - Recursively sort the array using quicksort.
 * @array: Array to be sorted.
 * @low: Starting index.
 * @high: Ending index.
 */
void quick_sort_recursive(int *array, int low, int high)
{
	if (low < high)
	{
		int pivot_index = lomuto_partition(array, low, high);

		printf("Partition: ");
		for (int i = low; i <= high; i++)
		{
			if (i == pivot_index)
				printf(" [%d] ", array[i]);
			else
				printf("%d ", array[i]);
		}
		printf("\n");

		quick_sort_recursive(array, low, pivot_index - 1);
		quick_sort_recursive(array, pivot_index + 1, high);
	}
}

/**
 * quick_sort - Sort an array using quicksort algorithm.
 * @array: Array to be sorted.
 * @size: Size of the array.
 */
void quick_sort(int *array, size_t size)
{
	if (array == NULL || size <= 1)
		return;

	quick_sort_recursive(array, 0, (int)size - 1);
}
