# KAUN BANEGA CROREPATI Game
# Create a program capable of displaying questions to the user like KBC.
# Use List data type to store the questions and their correct answers.
# Display the final amount the person is taking home after playing the game

questions = [
    [
        "Which language was used to create Facebook?", "Python", "C++", "JavaScript", "Php", 4
    ],
    [
        "The language of Lakshadweep, a Union Territory of India, is:", "Tamil", "Hindi", "Malayalam", "Telugu", 3
    ],
    [
        "According to QAir which capital city became the world's most polluted major city in August 2023?", "Beijing", "New Delhi",
        "Mexico City", "Jakarta", 4
    ],
    [
        "Which of these Grand slam tennis tournaments was not played in 2020?", "French Open", "US Open", "Wimbledon Championships",
        "Australian Open", 3
    ],
    [
        "Bleaching powder is a compound of which chemical element?", "Sodium", "Potassium", "Calcium", "Iron", 3
    ],
    [
        "Which of these states does not border Maharashtra?", "Gujarat", "Andhra Pradesh", "Chhattisgarh", "Karnataka", 2
    ],
    [
        "If the P in the Pincode of a place stands for Postal then what does the P in the PIN of ATM banking stand for?",
        "Population", "Personal", "Professional", "Permanent", 2
    ],
    [
        "Which of these planets does not have rings?", "Jupiter", "Saturn", "Neptune", "Venus", 4
    ],
    [
        "Which European football team won the 2019-2020 UEFA Champions League?", "Paris Saint Germain", "Liverpool",
        "Bayern Munich", "Manchester City", 3
    ],
    [
        "What type of rock is granite?", "Igneous", "Sedimentary", "Metamorphic", "Lunar", 1
    ],
    [
        "If someone is spending 1.5 hours reading in a day, how many hours is he reading in a week?", 7.5, 9, 10.5, 14, 3
    ],
    [
        "Which thread-like structure in our cells carries hereditary information?", "Carapace", "Carotid", "Carcinogen",
        "Chromosome", 4
    ],
    [
        "Which is currently the northernmost state of India?", "Himachal Pradesh", "Uttarakhand", "Punjab",
        "Jammu and Kashmir", 4
    ],
    [
        "Which of these is a domain name used by official Indian government websites?", "gov.in", "gov.com",
        "ind.in", "ind.com", 1
    ],
    [
        "Which of these is not a chemical element?", "Argon", "Nitrogen", "Salt", "Mercury", 3
    ],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000,
          160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]
money = 0
print("\n\nWELCOME TO KAUN BANEGA CROREPATI GAME!!!")
for i in range(0, len(questions)):

    question = questions[i]
    print(f"\nQuestion for Rs. {levels[i]} :\n", questions[i][0])
    print(f"1. {question[1]}")
    print(f"2. {question[2]}")
    print(f"3. {question[3]}")
    print(f"4. {question[4]}")
    reply = int(input("Enter your answer (1-4) or  0 to quit:\n"))
    if (reply == 0):
        money = levels[i-1]
        print("\nYou quit the game")
        break
    if (reply == question[-1]):
        print(f"Correct answer!! you have won Rs. {levels[i]}")
        if (i == 4):
            money = 10000
        elif (i == 9):
            money = 320000
        elif (i == 14):
            money = 10000000
    else:
        print("Wrong answer!!")
        break

print(f"Your take home money is {money}")
