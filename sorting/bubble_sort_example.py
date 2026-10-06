def main():
	my_array_to_sort = [976, 846, 728, 198, 273, 609, 472, 341, 500]
	
	arr_length = len(my_array_to_sort)
	for i in range(arr_length-1):
		for j in range(arr_length-i-1):
			if my_array_to_sort[j] > my_array_to_sort[j+1]:
				my_array_to_sort[j], my_array_to_sort[j+1] = my_array_to_sort[j+1], my_array_to_sort[j]

	print("The sorted array is:", my_array_to_sort)


if __name__ == "__main__":
	main()
