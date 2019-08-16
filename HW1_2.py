#2. Print only the first ten elements of the fibonacci sequence 

a = 0
b = 1

print(a)						

count = 1						# So then I reflect that first print here

while True:
	c = a + b
	a = b
	b = c

	print(a)

	count = count + 1

	if count > 9:				
		break


# Alternative

a=0
b=1

fibonacci_sequence = [a]

count = 1

while True:
	c = a + b
	a = b
	b = c

	fibonacci_sequence.append(a)

	count = count + 1

	if count > 9:
		break

print(fibonacci_sequence)
