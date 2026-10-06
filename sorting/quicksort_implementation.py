def main():
	my_arr = [64, 32, 85, 7, 29, 10, 44, 16]
	quicksort(my_arr)
	print("Sorted array: ", my_arr)


def quicksort(input_arr, low=0, high=None):
	if high is None:
        high = len(input_arr) - 1

	if low < high:
		pivot_index = partition(arr, low, high)
		quicksort(input_arr, low, pivot_index-1)
		quicksort(input_arr, pivot_index+1, high)


def partition(arr, low, high):
	pivot = arr[high]
	i = low - 1

	for j in range(low, high):
		if arr[j] <= pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i+1], arr[high] = arr[high], arr[i+1]
	return i+1


if __name__ == '__main__':
	main()
