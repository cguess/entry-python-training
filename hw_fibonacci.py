#1. Write a fibonacci sequence that prints forever 

a=0
b=1

while True:
	c = a + b
	a = b
	b = c

	fibonacci_sequence = [a, b, c]

	print(fibonacci_sequence) 


# alternative w/append

a=0
b=1

fibonacci_sequence = [a, b]

while True:
	c = a + b
	a = b
	b = c

	fibonacci_sequence.append(c)

	print(fibonacci_sequence)



#2. Print only the first ten elements of the fibonacci sequence 

a=0
b=1

print (a)

print (b)

count = 0

while True:
	c = a + b
	a = b
	b = c

	print (c)

	count = count + 1

	if count > 7:
		break


# alternative w/append

a=0
b=1

fibonacci_sequence = [a, b]

count = 0

while True:
	c = a + b
	a = b
	b = c

	fibonacci_sequence.append(c)

	count = count + 1

	if count > 7:
		break

print(fibonacci_sequence)



#3. Print the first ten elements of the fibonacci sequence all at once (from an array)

a=0
b=1

print (a)

print (b)

count = 0

while count < 8: 
	
	c = a + b
	a = b
	b = c

	count = count + 1
	
	print (c)

# alternative w/append

a=0
b=1

fibonacci_sequence = [a, b]

count = 0

while count < 8: 
	
	c = a + b
	a = b
	b = c
	
	fibonacci_sequence.append(c)

	count = count + 1

print(fibonacci_sequence)
