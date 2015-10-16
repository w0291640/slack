__author__ = 'w0291640'

"""user enters hours worked and wage
calculate amount made for week
if hours > 40 inclue OT
ot = 1.5x wage x hours over 40
"""
overTimePay = 0.0
overTimeHours = 0
hours = float(input("Enter the hours worked: "))
wage = float(input("Enter your hourly rate of pay: $"))
overTime = 40 # variable as this can change based on province or negotiated contract
overTimeMultiplier = 1.5
def weekly(hoursFunc,overTimeFunc,overTimeHoursFunc,overTimePayFunc,wageFunc):
    if hoursFunc > overTimeFunc:
        overTimeHoursFunc = hoursFunc-overTimeFunc
        overTimePayFunc = overTimeHoursFunc * (wageFunc*1.5)
        hoursFunc -= overTimeHoursFunc
    pay = hoursFunc*wageFunc
    pay = pay + overTimePayFunc
    return pay
print("You worked {0:.0f} hours at ${1:.2f} hourly".format(hours + overTimeHours, wage))
print("Your pay is ${:.2f}".format(weekly(hours,overTime,overTimeHours,overTimePay,wage)))
