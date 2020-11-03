#list comprehension, examples:

#ex1:
even_numbers = [x for x in range(1,101) if x % 2 == 0]

even_numbers = [x    #this, variable - x, stands for what's going to be stored in the list
                for x in range(1,101)  #this says the varibale - x will loop through the range of 1 to 100
                #meaning x = 1,2,3,4,5,6,7...to 100 (not including 101, 101 is where it stops)
                if x % 2 ==0  #states we only keep x, only when x is divisble by 2 (==0 aka. true)
                ]

odd_numbers = [x for x in range(1,101) if x % 2 != 0]

#ex2:

# -- variable with iterables - aka. list
words = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

# -- creating the loop
answer = [[w.upper(), w.lower(), len(w)] for w in words]
#"w" is the iterable that exists in words that will be looped one at a time: the, quick, etc.

# what we're going to store in the the list of this loop is ANOTHER  list which cotainns:
# - w.upper() - the upper case version of the word
# - l.lower() - the lower case version of the word
# - len(w) - the length of the word

## this is when  u realize that the assignments are not literal, but rather you need to understand how things stand for each other.

## when you have a list, you can feed that into another loop.
