# 1. Write a fibonacci sequence that prints forever 

a = 0
b = 1

print(a)						# I think I can't do away with a print at this stage, otherwise the initial zero gets lost

while True:
	c = a + b
	a = b
	b = c

	print(a)


# Alternative

a=0
b=1

fibonacci_sequence = [a]

while True:
	c = a + b
	a = b
	b = c

	fibonacci_sequence.append(a)

	print(fibonacci_sequence)
