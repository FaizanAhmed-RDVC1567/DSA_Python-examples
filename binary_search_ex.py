def binarySearch(arr, targetVal):
	left = 0
	right = len(arr) - 1
	
	while left <= right:
        mid = (left + right) // 2

        if arr[mid] == targetVal:
            return mid
        
        if arr[mid] < targetVal:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def main():
	myArray = [41, 43, 45, 47, 49, 51, 53, 55, 57, 59]
	myTarget = 49

	result = binarySearch(myArray, myTarget)

	if result != -1:
		# This return value means that the desired value was found, so show appropriate result
    	print("Value",myTarget,"found at index", result)
	else:
		# When return value is -1, that means that the desired value was not found, so show appropriate message.
    	print("Target not found in array.")


if __name__ == '__main__':
	# The Binary Search algorithm searches through an array and returns the index of the value it searches for.
	main()
