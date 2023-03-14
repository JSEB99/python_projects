# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

name1_lower_case = name1.upper()
name2_lower_case = name2.upper()

counter = 0
counter2 = 0

counter += name1_lower_case.count("T")
counter += name1_lower_case.count("R")
counter += name1_lower_case.count("U")
counter += name1_lower_case.count("E")
counter += name2_lower_case.count("T")
counter += name2_lower_case.count("R")
counter += name2_lower_case.count("U")
counter += name2_lower_case.count("E")

counter2 += name1_lower_case.count("L")
counter2 += name1_lower_case.count("O")
counter2 += name1_lower_case.count("V")
counter2 += name1_lower_case.count("E")
counter2 += name2_lower_case.count("L")
counter2 += name2_lower_case.count("O")
counter2 += name2_lower_case.count("V")
counter2 += name2_lower_case.count("E")

love_score = int(str(counter) + str(counter2))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go"
          " together like coke and mentos.")
elif 40 < love_score < 50:
    print(f"Your score is {love_score}, you are"
          " alright together.")
else:
    print(f"Your score is {love_score}.")
