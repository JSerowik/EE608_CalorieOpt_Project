from cvxpy import *
import numpy

# Ask user for inputs to determine ideal Daily Calorie Intake (DCI)
std = input('Do you use the Metric system or Imperial? (M or I) ')
if(std == "M"):
	weight = float(input('What is you weight in kilograms? '))
	height = float(input('What is you height in meters? '))
elif(std == "I"):
	wlb = float(input('What is you weight in pounds? '))
	weight = wlb/2.2046226218
	print('Input your height: ')
	h_ft = int(input('Feet: '))
	h_inch = int(input('Inches: '))
	h_inch += h_ft * 12
	height = (h_inch * 2.54)/100
age = float(input("How old are you? "))
sex = input('What is your sex? (M or F) ')
if(sex == "M"):
	DCI = 864 - 9.72 * age + (14.2 * weight + 503 * height)
elif(sex == "F"):
	DCI = 387 - 7.31 * age + (10.9 * weight + 660.7 * height)
print("Metric weight is: " +str(round(weight,2)) + " kg")
print('Metric height is: ' +str(round(height,2)) + ' m')
print("Daily Caloric intake: "+str(round(DCI,2))+" calories")

# Problem data.
prot = 4
carb = 4
fat = 9

# Construct the problem.
p = Variable()
c = Variable()
f = Variable()

objective = Minimize((4*p)+(4*c)+(9*f))
constraints = [p > 0, c > 0, f > 0, (4*p)+(4*c)+(9*f) >= DCI]
prob = Problem(objective, constraints)

# The optimal objective is returned by prob.solve().
result = prob.solve()
print("{}: {} calories daily".format("Minimized intake", result))
print("{}: {} grams".format("Protein", round(p.value,2)))
print("{}: {} grams".format("Carbs", round(c.value,2)))
print("{}: {} grams".format("Fat", round(f.value,2)))
# The optimal Lagrange multiplier for a constraint
# is stored in constraint.dual_value.
#print(constraints[0].dual_value)
#print(p.value/(p.value+c.value+f.value))