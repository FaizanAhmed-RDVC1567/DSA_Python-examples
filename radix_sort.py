def main():
	input_arr = [188, 87, 16, 292, 435, 99, 6, 70]
	print("Original array: ", input_arr)

	radix_arr = [[], [], [], [], [], [], [], []]
	max_val = max(input_arr)
	exp = 1

	while max_val // exp > 0:
		while len(input_arr) > 0:
			val = input_arr.pop()
			radix_index = (val // exp) % 10
			radix_arr[radix_index].append(val)

		for bucket in radix_arr:
			while len(bucket) > 0:
				val = bucket.pop()
				input_arr.append(val)

		exp *= 10

	print("Sorted array: ", input_arr)


if __name__ == '__main__':
	main()
	
