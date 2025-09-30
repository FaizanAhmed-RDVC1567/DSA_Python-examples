def main():
	my_array = [7, 12, 9, 4, 11]
	lowest_val = my_array[0]

	for i in my_array:
		if i < lowest_val:
			lowest_val = i

	print("Lowest value: ",lowest_val)


if __name__ == '__main__':
	main()
