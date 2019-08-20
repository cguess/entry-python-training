# So you did both here, the first one doesn't print from an array, but it does in the second.
# You clearly get the solution, but might be missing a bit on the problem description.
# Let me know if this doesn't make sense.

# The same comments as before also apply here though.

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
