#
### Count the number of unique letters in a string
#

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def unique_english_letters(word):
  unique_letters = 0
  for letter in letters:
    if letter in word:
      unique_letters += 1
  return unique_letters


# Test the function:
print(unique_english_letters("mississippi"))
# Prints 4
print(unique_english_letters("Apples and Oranges and Pinapples"))
# Prints 13

#
## Count the number of times a letter is found in a string
#

def count_char_x(word, x):
  letter_count = 0
  for letter in word:
    if x == letter:
      letter_count += 1
  return letter_count


# Test the function:
print(count_char_x("mississippi", "s"))
# Prints 4
print(count_char_x("mississippi", "m"))
# Prints 1
print(count_char_x("mississippi", "p"))
# Prints 2

#
## Count the number of times a substring is found in a string
#

def count_multi_char_x(word, x):
  str_counter = word.split(x)
  return(len(str_counter)-1)

# Test the function
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1
print(count_multi_char_x("Pizza and Jazz", "zz"))
# should print 1

#
### See if a certain name is in a sentence
#

# Define the Function
def check_for_name(sentence, name):
  return name.lower() in sentence.lower()

# Test the function
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False

#
### Get every other letter from a string
#

#  Define function
def every_other_letter(word):
  every_other = ""
  for i in range(0, len(word), 2):
    every_other += word[i]
  return every_other

# Test the function
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print 

#
### Print a string in reverse
#

#  Define the function

def reverse_string(word):
  reversed_str = ""
  for i in range(len(word)-1, -1, -1):
    reversed_str += word[i]
  return print(reversed_str)


# Test the function
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print