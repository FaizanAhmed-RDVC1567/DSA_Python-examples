def main():
	my_arr = [64, 32, 85, 7, 29, 10, 44, 16]

	arr_len = len(my_arr)
	for i in range(1, arr_len):
		insert_index = i
		current_value = my_arr.pop(i)
		for j in range(i-1, -1, -1):
			if my_arr[j] > current_value:
				insert_index = j
		my_arr.insert(insert_index, current_value)

	print("Sorted array: ", my_arr)


if __name__ == '__main__':
	main()
