# This piece of code shows how one can implement Radix Sort using another stable algorithm.
# The algorithm being used here is bubble sort, but any other stable sorting algorithm 
# such as counting sort, can also be used to implement Radix Sort.

def bubble_sort(arr):
	n = len(arr)
	for i in range(n):
		for j in range(0, n - i - 1):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]


def radixSortWithBubbleSort(in_arr):
	max_val = max(in_arr)
	exp = 1

	while max_val // exp > 0:
		radix_array = [[], [], [], [], [], [], [], [], [], []]

		for num in in_arr:
			radixIndex = (num // exp) % 10
			radix_array[radixIndex].append(num)

		for bucket in radix_array:
			bubble_sort(bucket)

		i = 0
		for bucket in radix_array:
			for num in bucket:
				in_arr[i] = num
				i += 1

		exp *= 10


def main():
	my_array = [170, 65, 85, 97, 843, 28, 2, 45]
	print("Original array: ", my_array)
	radixSortWithBubbleSort(my_array)
	print("\nSorted array: ", my_array)


if __name__ == '__main__':
	main()
	
