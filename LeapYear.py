# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇z
leapYear=False
if year%4==0:
    leapYear = True
if year%100==0:
    if year%400==0:
        leapYear = True
    else:
        leapYear = False
if leapYear == True:
    print("Leap year")
else:
    print("Not leap year")