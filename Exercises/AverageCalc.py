__author__ = 'Alex'

#1. Welcome Message
print("HI! I'm here to help you find the average of any THREE numbers you wish")

#2. Prompt User for their number choices and confirm
numberOne =input("Please enter your first number: ")
numberTwo =input("Now for your second number: ")
numberThree =input("And finally your third: ")
print("You have entered: " + str(numberOne) + ", " + str(numberTwo) + ", " + str(numberThree) + ", ")
#3 Calculate

average = (float(numberOne) + float(numberTwo) + float(numberThree)) / 3

#4 Display rounded average

print("The average of your numbers is : " + str(round(average, 2)))

