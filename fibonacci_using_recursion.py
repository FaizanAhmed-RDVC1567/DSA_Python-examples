count = 2
def main():
	print(0)
	print(1)
	fibonacci(0, 1)


def fibonacci(prevNum1, prevNum2):
	global count
	if count <= 19:
		newFibo = prevNum1 + prevNum2
		print(newFibo)
        prevNum2 = prevNum1
        prevNum1 = newFibo
        count += 1
        fibonacci(prevNum1, prevNum2)
	else:
		return


if __name__ == '__main__':
	main()
