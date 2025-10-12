def main():
	"""
	The basic selection sort algorithm has a problem that can be addressed to make it better. In the code
	of 'insertion_sort_base.py', the lowest element value is found, removed and then stored in front of the
	array. Each time this happens, all the following elements must be shifted one place down (i.e. to the next
	index position than they were currently at) to make up for the removal.

	This shifting operation des take some time (it is quite noticeable for large lists), and the whole array hasn't
	even been sorted completely when the elements are shifted in the array for the first time! For an array that
	contains the following values: 
	
	74, 44, 35, 7, 24, 10, 68, 19

	When 7 is removed from the list, the elements after it will all shift one position upward (to the preceding
	index position), and when 7 is inserted at the starting position of the array, all the other remaining
	elements will shift one position down (to the next index position) to make space for the new value. These
	shifting operations won't be seen on a high-level programming language like Python or Java, but they are
	still taking place in the background. Such shifting operations require extra performance from the
	computer to do, which poses a problem. A solution is to swap values from the first index position to the
	index position the smallest value element in an iteration was found. The swapped value in the new index
	position will eventually get sorted.
	"""
	my_arr = [74, 44, 35, 7, 24, 10, 68, 19]

	arr_len = len(my_arr)
	for i in range(arr_len):
		min_index = i
		for j in range(i+1, arr_len):
			if my_arr[j] < my_arr[min_index]
				min_index = j
		my_arr[i], my_arr[min_index] = my_arr[min_index], my_arr[i]

	print("Sorted array: ", my_arr)


if __name__ == '__main__':
	main()
