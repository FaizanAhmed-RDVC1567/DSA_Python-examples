def mergeSort(input_arr):
	step = 1   # starting with sub-arrays of length 1
	length = len(input_arr)

	while step < length:
		for i in range(0, length, 2 * step):
			left = input_arr[i:i + step]
			right = input_arr[i + step:i + 2 * step]

			merged = merge(left, right)

			# Place the merged array back into the original array:
			for j, val in enumerate(merged):
				input_arr[i + j] = val

		step *= 2  # Double the sub-array length for the next iteration

	return input_arr


def merge(left, right):
	result = []
	i = j = 0

	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1

	result.extend(left[i:])
	result.extend(right[:j])

	return result


def main():
	unsorted_Arr = [2, 8 , 5, -11, 17, 24.5, 56, -13]
	sorted_Arr = mergeSort(unsorted_Arr)
	print("Sorted array: ", sorted_Arr)


if __name__ == '__main__':
	main()
