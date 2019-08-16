a=0
b=1

fibonacci_sequence = [a]

while True:
	c = a + b
	a = b
	b = c

	fibonacci_sequence.append(a)

	print(fibonacci_sequence)
