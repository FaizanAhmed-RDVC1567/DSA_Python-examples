def main():
	"""
	Every time the lowest value in the array is encountered, it is removed from its' position
	and re-inserted at the front of the list. When this happens, the rest of the array is still
	un-sorted. The outer loop controls how many times the inner loop runs by using the length
	of the unsorted array as a guide. For an array of some size n, the outer loop will run a
	total of n-1 times.

	The inner loop runs through the entire array, finding the lowest value and then moving it to
	the front of the array. This loop will loop through one less value at each iteration (as the
	elements are gradually sorted into their proper positions.
	"""
	my_arr = [64, 32, 85, 7, 29, 10, 44, 16]

  	arr_len = len(my_arr)
	for i in range(arr_len - 1):
		min_index = i
		for j in range(i+1, arr_len):
			if my_arr[j] < my_arr[min_index]:
				min_index = j
		min_value = my_arr.pop(min_index)
		my_arr.insert(i, min_value)

	print("Sorted array: ", my_arr)


if __name__ == '__main__':
  	main()
