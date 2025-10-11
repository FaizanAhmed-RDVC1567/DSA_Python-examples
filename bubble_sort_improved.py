def main():
	my_arr = [46, 30, 59, 68, 71, 82]

	arr_len = len(my_arr)
	for i in range(arr_len - 1):
		swapped_item = False
		for j in range(arr_len - i - 1):
			if my_arr[j] > my_arr[j+1]:
				my_arr[j], my_arr[j+1] = my_arr[j+1], my_arr[j]
				swapped = True
		if not swapped:
			break
			# The intention of the above is to prevent the bubble sort from running for longer than it is
			# supposed to when no elements are swapped after the first iteration. If this check is not
			# present, then the loop will continue checking the order of elements even if the array
			# is already sorted. This will save resources.


if __name__ == '__main__':
	main()
	
