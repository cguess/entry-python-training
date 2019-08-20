# Good job! This works for both, but there are some issues to consider I've highlighted below.
# 1. Write a fibonacci sequence that prints forever 

a = 0
b = 1

print(a) # I think I can't do away with a print at this stage, otherwise the initial zero gets lost
# Yes, that works, but see below to another possible way of doing it.

while True:
  # What about putting print(a) here instead?
        
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

        # This will print the *entire* sequence, every time. Probably not what you want.
	print(fibonacci_sequence)

# Note that, here, is the same as above. Good job initialie the List with the first element,
# and it'll work fine. However, you could remove a line and simplify it if you instead move
# the append() to the first line of the loop.
