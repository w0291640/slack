__author__ = 'w0291640'

"""max amt weight 50lbs
25$ added for greater than 50lbs
"""
weight = float(input("Enter the weight of your luggage: "))
surcharge = 25.00
weightThreshold = 50
if weight > weightThreshold:
    print("Your luggage is over {0}lbs and you will be charged a ${1:.2f} surcharge".format(weightThreshold,surcharge))
else:
    print("your luggage is under {0}lbs no surcharge will be added".format(weightThreshold))