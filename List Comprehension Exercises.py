# https://www.reddit.com/r/learnpython/comments/4d2yl7/i_need_list_comprehension_exercises_to_drill/

# %%
## Find all of the numbers from 1-1000 that are divisible by 7

NumDiv = [num for num in range(1, 1001, 1) if num % 7 == 0]
print(NumDiv)





# %%
## Find all of the numbers from 1-1000 that have a 3 in them

Num3 = [num for num in range(1, 1001, 1) if str(3) in str(num)]
print(Num3)





# %%
## Count the number of spaces in a string

sentence = "The quick brown fox jumps over the lazy dog."
print(sentence.count(' '))  # For checking purposes

Spaces = [s for s in sentence if s == " "]
print(len(Spaces))





# %%
## Remove all of the vowels in a string

sentence = "The quick brown fox jumps over the lazy dog."
vowels = ['a', 'e', 'i', 'o', 'u']

Sentlis = [character for character in sentence if character.lower() not in vowels]

listToStr = ''.join([str(elem) for elem in Sentlis])


print(listToStr)





# %%
## *Find all of the words in a string that are less than 4 letters

sentence = "The quick brown fox jumps over the lazy dog."

Short = [w for w in sentence.split() if len(w) < 4]
Short





# %%
## *Use a dictionary comprehension to count the length of each word in a sentence.

sentence = "The quick brown fox jumps over the lazy dog."

results = {word:len(word) for word in sentence.split()}
results





# %%
## Change strings to list of integers

lis = ('9, 4, 5, 8, 10, 14')

lis = [int(s) for s in lis.split(',')]

print(lis)





# %%
## Obtain user input for multiple indexes. The extract from list.

lis = [9, 4, 5, 8, 10, 14]
select = input('Select files to concatenate using a number (count begins at 0). Please separate selections with comma:')

# selectindex = [int(num) for num in select.split(',')]

selectindex = map(int, select.split(','))

userlis = [lis[num] for num in selectindex]

print(userlis)





# %%
## *Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)


# [x for x in range(1, 1001, 1) if x % n in range(2, 10, 1) == 0]
# Div = [x for x in range(1, 1001, 1) if n for n in range(2, 10, 1) % n == 0]


# Divisible = [x for divisor in range(2, 10, 1) if x % divisor == True]

Div = [x for x in range(1, 1001, 1) if True in [True for divisor in range(2, 10, 1) if x % divisor == 0]]
Div





# %%
## *For all the numbers 1-1000, use a nested list/dictionary comprehension to find the highest 
# single digit any of the numbers is divisible by


# Highest Single Digit Divisible by 
# True for max(divisor) in range(2, 10, 1) if x % divisor == 0


# Div = [x for x in range(1, 1001, 1) if True in [True for divisor in range(2, 10, 1) if x % divisor == 0]]
# Div

# MaxDiv = {num:max(divisor) for num in range(1, 1001, 1) if True in [True for divisor in range(2, 10, 1) if num % divisor == 0]}


MaxDiv = {num:max([divisor for divisor in range(1, 10, 1) if num % divisor == 0]) for num in range(1, 1001, 1)}
print(MaxDiv)





# %%
## A list of all the capital letters (and not white space) in 'The Quick Brown Fox Jumped Over The Lazy Dog'





# %%
## A list of all square numbers formed by squaring the numbers from 1 to 1000.









# %%

# Return a list of the full path to items in a directory (hint, use os.listdir() and os.path.join())
# Now extend this same one to exclude directories (hint, use os.path.isdir())
# Now extend it further to filter to only files ending in .jpg and .png







