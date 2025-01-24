# # Sample program to perform various operations and functions for the learning of lists in python...

# marks = [3, 5, 6, "Harry", True, 6, 7 , 2, 32, 345, 23]
# # print(marks)
# # print(type(marks))
# # print(marks[0])
# # print(marks[1])
# # print(marks[2])
# # print(marks[3])
# # print(marks[4])
# # print(marks[5])

# # print(marks[-3]) # Negative index
# # print(marks[len(marks)-3]) # Positive index
# # print(marks[5-3]) # Positive index
# # print(marks[2]) # Positive index

# # if "6" in marks:
# #   print("Yes")
# # else:
# #   print("No")

# # Same thing applies for strings as well!
# # if "Ha" in "Harry":
# #   print("Yes")

# # print(marks[0:7])
# # print(marks[1:9])
# # print(marks[1:9:3])

# lst = [i*i for i in range(10)]
# print(lst)
# lst = [i*i for i in range(10) if i%2==0]
# print(lst)


# l = [11, 45, 1, 2, 4, 6, 1, 1]
# print(l)
# # l.append(7)
# # l.sort(reverse=True)
# # l.reverse()
# # print(l.index(1))
# # print(l.count(1))
# # m = l.copy()
# # m[0] = 0
# # l.insert(1, 899)
# m = [900, 1000, 1100]
# k = l + m
# # print(k)
# # l.extend(m)
# print(l)

# animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "goat"]
# print(animals[::2])	#using positive indexes
# print(animals[-6:-1:2])	#using negative indexes

colors = ["voilet", "indigo", "blue"]
#           [0]        [1]      [2]

colors.insert(1, "green")   #inserts item at index 1
# updated list: colors = ["voilet", "green", "indigo", "blue"]
#       indexs              [0]       [1]       [2]      [3]

print(colors)