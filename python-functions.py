# 1. Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n
def sum_to(n):
  sum = 0
  for i in range(n+1):
    sum += i
  return sum

# 2. Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.
def largest(nums):
  return max(nums)

# 3. Write a function named `occurrences` that takes two string arguments as input and counts the number of occurrences of the second string inside the first string.
def occurrences(str1, str2):  
  return str1.count(str2)

# 4. Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product. 
def product(*args):
  product = 1
  for arg in args:
    product *= arg
  return(product)

