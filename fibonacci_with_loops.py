"""
Basic algorithm to generate the first 20 Finacci numbers is as follows:
1) Start with the two first Fibonacci numbers 0 and 1.
	a.Add the two previous numbers together to create a new Fibonacci number.
	b.Update the value of the two previous numbers.
2) Do point a and b above 18 times.
"""

def main():
	prev_number2 = 0
	prev_number1 = 1

	print(prev_number2)
	print(prev_number1)
	for fibo in range(18):
		# 18 because the first two numbers we are already printing, and we need 18 more entries (0th - 17th iteration)
		# to find the remaining numbers
		newFibo = prev_number1 + prev_number2
		print(newFibo)
		prev_number2 = prev_number1
		prev_number1 = newFibo


if __name__ == '__main__':
	main()
