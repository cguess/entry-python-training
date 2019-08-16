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
