def mergeSort(inputArr):
	# As merge sort repeatedly splits the array down into smaller parts, there will be a case
	# where a recursive call to this function will contain an array with a single element. In
	# this case, as there is no further splitting to be done, we will simply return the array.
	if len(inputArr) <= 1:
		return inputArr

	middle = len(inputArr) // 2
	leftHalf = inputArr[:middle]
	rightHalf = inputArr[middle:]

	sortedLeft = mergeSort(leftHalf)
	sortedRight = mergeSort(rightHalf)
	return merge(sortedLeft, sortedRight)


def merge(left, right):
	result = []
	i = j = 0

	while i < len(left) and j < len(right):
		if left[i] < right [j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1

	result.extend(left[i:])
	result.extend(right[:j])

	return result


def main():
	unsorted_arr = [2, 6, 8, -11, 17, 23.5, 52, -14]
	sorted_arr = mergeSort(unsorted_arr)
	print("Sorted array: ", sorted_arr)


if __name__ == '__main__':
	main()
	
