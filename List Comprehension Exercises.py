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
## Find all of the words in a string that are less than 4 letters





# %%
## *Use a dictionary comprehension to count the length of each word in a sentence.





# %%
## *Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)





# %%
## *For all the numbers 1-1000, use a nested list/dictionary comprehension to find the highest single digit any of the numbers is divisible by





# %%
## A list of all the capital letters (and not white space) in 'The Quick Brown Fox Jumped Over The Lazy Dog'





# %%
## A list of all square numbers formed by squaring the numbers from 1 to 1000.





