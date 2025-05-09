# Create a python program using time module capable of greeting you with Good Morning, Good Afternoon, Good Evening and Good Night.

# https://docs.python.org/3/library/time.html#time.strftime

import time
timestamp = time.strftime('%H:%M:%S')
print("The current time is", timestamp)
# timestamp = time.strftime('%H')
# print(timestamp,"Hours")
# timestamp = time.strftime('%M')
# print(timestamp,"Minutes")
# timestamp = time.strftime('%S')
# print(timestamp,"Seconds")

a = time.strftime ("%H")
b= int(a)
name=input("Enter your name: ")
if(b>=1 and b<12):
    print("GOOD MORNING",name)
elif(b>=12 and b<=17):
    print("GOOD AFTERNOON",name)
elif(b>17 and b<=19):
    print("GOOD EVENING",name)
elif(b>19 and b<=24):
    print("Good night",name)
else:
    print("Time not found")
    