# Introduction to Python

## Part 2: Basics

### Variables

In Python, and most programming languages, we use variables to store information. These can be then
reread, rewritten, added to, etc.

#### Naming Variables

##### Small Rant
I'm going to put this at the top because so many new (and old) programmers straight up suck at naming
variables. Rule #1 is that variable names should be self-descriptive. Their name should indicate what
information it's holding. For example, `a`, `x`, `temp`, `no_clue` are all bad names while
`name_count`, `last_name`, `atomic_weight_of_oxygen` are all good names.

There are a lot of old habits still laying around in old code and the habits of older coders that
program like it's the 1980's. Back then you were limited in the amount of memory your program could
take up, and shorter variable names saved memory and were easier to fit on screens that were only 80
characters across. However, that was 30+ years ago, and the times have changed.

A good addage from the early 90's holds up today
> "Always code as if the guy who ends up maintaining your code will be a violent psychopath
who knows where you live."

That person will, more than likely be you, in six months, long after you forgot what the variable `xyz`
meant at 2:30AM. Save your headache and hairline, choose good variable names.

(In the examples I use single letters sometimes, this is just for brevity in examples. Do as I say,
not as I do.)

##### Python Naming Conventions
Variables can be named anything (well almost, there are about 20 words that are reserved by the
programming lanugage, but don't worry about that right now). In python, the standard is to name
variables in "snake case" which_mean_it_looks_like_this (no capitals, spaces are underscores).

The only restriction is that a variable cannot start with a number. I.e. `1variable = "test"` will
produce an error but `variable1 = "test"` will not. However, these are also terrible variable names.
Don't use them.

#### Usage Examples

An example that assigns the string "hello world!" to a variable called hello_world:
```
hello_world = "hello world!"
```

We could also give it a number:
```
a_number = 42
```

We can then also print variables out:
```
hello_world = "hello world!"
print(hello_world)

> "hello world!"
```

Going on we can then reassign variables:
```
hello_world = "hello world!"
print(hello_world)

> "hello world!"

hello_world = "goodbye world!"
print(hello_world)

> "goodbye world!"
```

## Types

### Introduction

Python, like most programming languages, has the concept of "types." These are the basic types
of data that are available to be saved and used. Everything you put in, or take out of your program
is reprsented by a fundemental data type, or a combination of them.

In python there are a few different types, the most basic being:
- Number
- String
- Boolean

There are three more as well that allow us to make groups of the other three. We'll get to them
in a minute, but for reference they're here:
- List
- Tuple
- Dictionary

#### Number

A number is... well, pretty self-explanatory. It's a number and it's created without quotation marks.
```
x = 1
x = 1.2
```

Numbers can be added together
```
x = 1
y = 1 + 2
print(y)

> 3

xy = x + y
print(xy)

> 4
```

Numbers can be subtracted
```
x = 10
y = 10 - 5
print(y)

> 5

xy = x - y
print(xy)

> 5
```

Numbers can be multiplied
```
x = 2
y = 2 * 2
print(y)

> 4

xy = 2 * y
print(xy)

> 8
```


Numbers can be divided
```
x = 10
y = 10 / 2
print(y)

> 5

xy = 15 / y
print(xy)

> 3
```

There are other functions as well (modulous, square roots, powers, etc. but those will be brought up later)


#### Strings

Strings are used to store a series of characters. What those characters mean are of little consequence,
The programming language sees them as data, not instructions.

A string is indicated by wrapping the text you want to store in quotation marks.
```
x = "I'm a string!"
print(x)

> I'm a string!
```

You can also join strings, though there are a bunch of different ways in Python, we'll go with the
simplest for the moment.
```
x = "I'm a"
y = "string!"
z = x + y
print(z)

> I'm a string!
```

Adding strings and numbers however, won't work, since they're different types. To convert a number
to a string we pass it to a method called `str()`

```
x = "Number of counts: " # A string
counts = 2 # A number
string_counts = str(counts) # Now a string

z = x + counts
# Error!

z = x + string_counts
print(z)

> Number of counts: 2
```

#### Booleans

There are two types of booleans "True" and "False" (if you're used to other programming languages
please take note the capital first letter). These can be very powerful, and are used all the time,
but for now just take a look at the following examples:

(Notice that here we introduce the `==`, which is the "equality" operator, and returns a True if
both variables are equal, and False if they are not).
```
x = True
y = True
z = False

print(x == y)
> True

print(y == x)
> True

print(x == z)
> False
```

### Collections

Now that we have an understanding of Numbers, Strings and Booleans let's take a look at grouping them.
There's a couple of way that Python let's us form collections of other types, but we'll start with
a basic and very useful (maybe the most useful) one.

#### Lists

A list (sometimes called an array in other programming languages), is an ordered collection of elements.

```
a_list = ["one", "two", "three", "four"]
print(a_list)

> ['one', 'two', 'three', 'four']
```

```
a_number_list = [1.2, 4, 7, 10]
print(a_number_list)

>[1.2, 4, 7, 10]
```

```
a_mixed_array = ["hello", 12, True]
print(a_mixed_array)

> ['hello', 12, True]
```

To Refer:
Remember that Python is zero-index
```
a_list = ["one", "two", "three", "four"]
first_element = a_list[0]
print(first_element)

> 'one'
```

To add an element we `append()` it

```
a_list = ["one", "two", "three", "four"]
a_list.append("five")
print(a_list)

> ['one', 'two', 'three', 'four', 'five']
```

To remove an element by index we can `pop()`

```
a_list = ["one", "two", "three", "four"]
a_list.pop(0)

> 'one'

print(a_list)

> ['two', 'three', 'four']
```

To remove a value that you're not sure where it is we `remove()`

```
a_list = ["one", "two", "three", "four"]
a_list.remove("two")

> 'two'

print(a_list)

> ['one', 'three', 'four']
```

Loops:

Just loop!

```
while True:
    # something!
```

Loop through each element and do something!

```
a_list = ["one", "two", "three", "four"]

for this_number in a_list:
    print(this_number)

print(a_list)

> 'one'
> 'two'
> 'three'
> 'four'
```

```
count = 5
count = count + 1

print(count)
> 6
```

how to kill a program
ctrl-c


0, 1, 1, 2, 3, 5, 8, 13, 21, 34


```
count = 0
while count < 10:
    print("hello!")
    count = count + 1

print(count)

> 'hello!'
> 'hello!'
> 'hello!'
> 'hello!'
> 'hello!'
> 'hello!'
> 'hello!'
> 'hello!'
> 'hello!'
> 'hello!'
> 10
```


1.) Write a fibonnaci sequence that prints forever (ctrl-c) to stop the program
2.) Print only the first ten elements of the fibonnaci sequence
3.) Print the first ten elements of the fibonnaci sequence all at once (from an array)









