#add double the index of a list
def double_index(lst, index):
  if index >= len(lst):
    return lst
  else:
    new_lst = lst[0:index]
    new_lst.append(lst[index] * 2)
    return new_lst + lst[index+1:]

#Test the function
print(double_index([3, 8, -10, 12], 2))





#return every 3 numbers in a range as a list
def every_three_nums(start):
  return list(range(start, 101, 3))

#Test the function
print(every_three_nums(101))





#Check how many numbers are divisible by ten
def divisible_by_ten(nums):
  total_nums = 0
  for num in nums:
    if(num % 10 == 0):
      total_nums += 1
  return total_nums

#Test the function
print(divisible_by_ten([20, 25, 30, 35, 40]))






#Add greeting to a list of names, then list names with greeting
def add_greetings(names):
  list_greetings = []
  for name in names:
    list_greetings.append("Hello, " + name)
  return list_greetings


#Test the function
print(add_greetings(["Owen", "Max", "Sophie"]))
# Output: ['Hello, Owen', 'Hello, Max', 'Hello, Sophie']







#Remove even first numbers
def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  return lst

#Test the function
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))
#Output:
#[11, 12, 15]
#[]





#Raise base to the exponent add to list
def exponents(bases, powers):
  both_listed = []
  for base in bases:
    for power in powers:
      both_listed.append(base ** power)
  return both_listed

#Test the function
print(exponents([2, 3, 4], [1, 2, 3]))






#Find the list with the larger sum
def larger_sum(lst1, lst2):
  lst1_sum = 0
  lst2_sum = 0
  for num in lst1:
    lst1_sum += num
  for num in lst2:
    lst2_sum += num
  if lst1_sum >= lst2_sum:
    return lst1
  else:
    return lst2

#Test the function
print(larger_sum([1, 9, 5], [2, 3, 7]))
#Output: [1, 9, 5]





#Add list until over 9000
def over_nine_thousand(lst):
  lst_sum = 0
  for num in lst:
    lst_sum += num
    if lst_sum > 9000:
      break
  return lst_sum


#Test the function
print(over_nine_thousand([8000, 900, 120, 5000]))
#Output: 9020






#Return the maximum number of a list
def max_num(nums):
  max_number = nums[0]
  for num in nums:
    if max_number < num:
      max_number = num
  return max_number

#Test the function
print(max_num([50, -10, 0, 75, 20]))
#Output: 75





#Check for matching indices
def same_values(lst1, lst2):
  comb_lst = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      comb_lst.append(index)
  return comb_lst


#Test the function
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
# Output: [0, 2, 3]




# Raise to the 10th power
def tenth_power(num):
  return num ** 10

# Test the function
print(tenth_power(1))
# 1 to the 10th power is 1
print(tenth_power(0))
# 0 to the 10th power is 0
print(tenth_power(2))
# 2 to the 10th power is 1024






# SQRT of a number
def square_root(num):
  return num ** .5

# Test the function
print(int(square_root(16)))
# should print 4
print(int(square_root(100)))
# should print 10






# Percentage of wins and loses
def win_percentage(wins, losses):
  totalGames = wins + losses
  ratio_won = wins / totalGames
  return ratio_won * 100
  
# Test the function
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100






# Write your average function here:
def average(num1, num2):
  return (num1 + num2) / 2   #dont forget PEMDAS...

# Uncomment these function calls to test your average function:
print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0






# Remainder of two modified nums
def remainder(num1, num2):
  return ((num1 * 2) % (num2 / 2))

# Test function
print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0





# Calculate tip
def tip(total, percentage):
  return (total * percentage) / 100

#  Test the function
print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0






# James Bond-ifier
def introduction(first_name, last_name):
  return last_name + ", " + first_name + " " + last_name

# Test the function
print(introduction("James", "Bond"))
# should print Bond, James Bond
print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou






# Dog age calculator
def dog_years(name, age):
  dog_age = age * 7
  return name + ", you are " + str(dog_age) + " years old in dog years"

# OR
#def dog_years(name, age):
#  return name+", you are "+str(age * 7)+" years old in dog years"

#  Test the function
print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"





# Operations with several parameters
def lots_of_math(a, b, c, d):
  first = a + b
  second = c - d
  third = first * second
  fourth = third % a
  print(first)
  print(second)
  print(third)
  return fourth


# Test the function
print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0