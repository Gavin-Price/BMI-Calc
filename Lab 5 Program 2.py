import math


weight = int(float(input('Enter your weight in pounds:')))
height = int(float(input('Enter your height in inches:')))
   


def getBMI(height, weight):
    bmi = round(weight/(height**2) * 703 ,1)

    if bmi < 18.5:
        print('A BMI of' ,bmi ,'puts you in the "Underweight" category.')
        
    elif bmi >= 18.8 and bmi <25:
        print('A BMI of' ,bmi ,'puts you in the "Normal Weight" category.')
        
    elif bmi >= 25 and bmi < 30:
        print('A BMI of' ,bmi ,'puts you in the "Overweight" category.')
        
    else:
        print('A BMI of' ,bmi ,'puts you in the "Obese" category.')
        
getBMI(height,weight)

    
    



