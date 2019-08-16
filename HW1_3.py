#3. Print the first ten elements of the fibonacci sequence all at once (from an array)

a = 0
b = 1

print (a)						

count = 1						

while count < 10: 
	
	c = a + b
	a = b
	b = c

	count = count + 1
	
	print (a)


# Alternative 

a=0
b=1

fibonacci_sequence = [a]

count = 1

while count < 10: 
	
	c = a + b
	a = b
	b = c
	
	fibonacci_sequence.append(a)

	count = count + 1

print(fibonacci_sequence)
