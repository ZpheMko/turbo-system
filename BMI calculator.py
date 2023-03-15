#login
name = input("what is your name? ")
surname = input("what is your surname? ")
gender = input('M/F? ')
print ('''welcome to our Body Mass Index calculator
       please note that our calculator does not take bone density or muscle
       mass into consideration ''')
#weight
weight = input('weight: ')
weight_unit = input('kg or lb:')
if weight_unit == 'lb':
    weight_kg = float(weight) * 2.205
else:
    weight_kg = float(weight) * 1
W = weight_kg
#height
height = input('height: ')
height_unit = input('m / cm / ft?: ')
#weight in cm
if height_unit == 'cm':
    height_m = float(height) / 100
#weight in ft
if height_unit == 'ft':
    height_m = float(height) / 3.302
if height_unit == 'm':
    height_m = float(height) * 1
H = float(height_m)**2
#calculation
BMI = W/H
print(BMI)
#underweight
if BMI < 18.7:
    print('your BMI is :' + str(BMI))
    print('underweight')
#healthyweight
if 18.7 < BMI < 26.7 :
    print('your BMI is :' + str(BMI))
    print('healthy weight')
#overweight
if BMI > 26.7:
    print('your BMI is :' + str(BMI))
    print('overweight')