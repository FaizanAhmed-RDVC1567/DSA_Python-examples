# Code for counting sort in Python


def countingSort(arr_to_sort):
	if not arr_to_sort:
		return arr_to_sort

	max_value = max(arr_to_sort)
	count = [0] * (max_value + 1)

	for num in arr_to_sort:
		count[num] += 1

	arr_to_sort[:] = []

	for num, freq in enumerate(count):
		arr_to_sort.extend([num] * freq)

	return arr_to_sort


def main():
	unsortedArr = [1, 2, 2, 4, 4, 4, 5, 5, 3, 3, 3, 6]
	sortedArr = countingSort(unsortedArr)
	print("Sorted array: ", sortedArr)


if __name__ == '__main__':
	main()
