# # MAP FILTER and REDUCE functions in python

# # MAP 
# # def cube(x):
# #   return x * x * x


# # print(cube(2))

# # l = [1, 2, 4, 6, 4, 3]
# # newl = []
# # for item in l:
# #   newl.append(cube(item))

# # newl = list(map(lambda x: x*x*x, l))
# # print(newl)

# # # FILTER
# # def filter_function(a):
# #   return a>2
  
# # newnewl = list(filter(filter_function, l))
# # print(newnewl)

# List of numbers
# numbers = [1, 2, 3, 4, 5]

# # Get only the even numbers using the filter function
# evens = filter(lambda x: x % 2 == 0, numbers)

# # Print the even numbers
# print(list(evens))

from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5] 
# # Calculate the sum of the numbers using the reduce function
sum=reduce(lambda x, y: x+y ,numbers)
print(sum)
