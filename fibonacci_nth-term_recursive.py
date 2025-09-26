def main():
	print(fibonacci(19))


def fibonacci(n):
	"""
	To find the nth Fibonacci number we can write code based on the mathematic formula for Fibonacci number n:

			F(n) = F(n - 1) + F(n - 2)
			
	This just means that for example the 10th Fibonacci number is the sum of the 9th and 8th Fibonacci numbers.
	Note that This formula uses a 0-based index. This means that to generate the 20th Fibonacci number, we must write F(19).
	When using this concept with recursion, we can let the function call itself as long as n is less than, or equal to, 1.
	If n is less than or equal to 1, it means that the code execution has reached one of the first two Fibonacci numbers 1 or 0.
  	"""
	if n <= 1:
		return n
	else:
		return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
	main()
