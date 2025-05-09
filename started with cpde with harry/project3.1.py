"""Write a python program to translate a message into secret code language.

Use the rules below to translate normal English into secret code language.
Coding:
  if the word contains atleast 3 characters, remove the first letter and append it at the end
  now append three random characters at the starting and the end
else:
  simply reverse the string

Decoding:
  if the word contains less than 3 characters, reverse it
else:
  remove 3 random characters from start and end. Now remove the last letter and append it to the beginning
Your program should ask whether you want to code or decode
"""

import random
import string


def get_random_letter(n):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters)for i in range(n))
    return result_str


def coding(st):
    words = st.split(" ")
    nwords = []
    for word in words:
        if (len(word) >= 3):
            r1 = get_random_letter(3)
            r2 = get_random_letter(3)
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print("The coded message is: ")
    print(" ".join(nwords))


def decoding(st):
    words = st.split(" ")
    nwords = []
    for word in words:
        if (len(word) >= 3):
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print("The decoded message is: ")
    print(" ".join(nwords))


print("\nWELCOME TO CODING AND DECODING PLATFORM!!!")
while True:
    code = input("Enter 1 to Code or 2 to Decode and 0 to quit: \n")

    if (code == "1"):
        st = input("Enter your message for coding: \n")
        coding(st)

    elif (code == "2"):
        st = input("Enter your message for decoding: \n")
        decoding(st)

    elif (code == "0"):
        print("You decided to quit!!!")
        break
    else:
        print("Wrong Input")