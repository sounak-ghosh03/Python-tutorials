# # Smaple program to perform various operations and functions for the learning of sets in python...

# s = {2, 4, 2, 6}
# print(s)

# info = {"Carla", 19, False, 5.9, 19}
# print(info)

# harry = set()
# print(type(harry))

# for value in info:
#   print(value)

# info = {"Carla", 19, False, 5.9}
# if "Carla" in info:
#     print("Carla is present.")
# else:
#     print("Carla is absent.")

# # cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# # cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# # cities3 = cities.union(cities2)
# # print(cities3)

# # cities.update(cities2)
# # print(cities)

# # cities3 = cities.intersection(cities2)
# # print(cities3)

# # cities.intersection_update(cities2)
# # print(cities)

# # cities3 = cities.symmetric_difference(cities2)
# # print(cities3)

# # cities.symmetric_difference_update(cities2)
# # print(cities)

# # cities3 = cities.difference(cities2)
# # print(cities3)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Seoul", "Kabul", "Delhi"}
# print(cities.difference(cities2))

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# print(cities.isdisjoint(cities2))

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Seoul", "Kabul"}
# print(cities.issuperset(cities2))
# cities3 = {"Seoul", "Madrid","Kabul"}
# print(cities.issuperset(cities3))

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Delhi", "Madrid"}
# print(cities2.issubset(cities))

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.add("Helsinki")
# print(cities)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Helsinki", "Warsaw", "Seoul"}
# cities.update(cities2)
# print(cities)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.remove("Tokyo")
# print(cities)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.discard("Seoul")
# print(cities)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# item = cities.pop()
# print(cities)
# print(item)

# # cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# # del cities
# # print(cities)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.clear()
# print(cities)

# info = {"Carla", 19, False, 5.9}
# if "Carla" in info:
#     print("Carla is present.")
# else:
#     print("Carla is absent.")
