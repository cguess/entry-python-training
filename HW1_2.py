# Much better than before. See my notes on the first example though, they apply here as well.

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

        # This could also be < 10, which *could* be more readable.
        # This is good though if somehow the user could reset "count"
        # since it'll stop it from every going above 9.
        # Basically both are good, but consider the use case.
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
