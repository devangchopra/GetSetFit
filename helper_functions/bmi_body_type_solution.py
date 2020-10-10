def bmi(weight,height):
    '''
    Fution is created to find the bmi , tell the status and solution
    
    Input :: Weight , Height
    
    Output :: 
    BMI -- weight/(height*height)
    Status -- (Under-weight, Normal , Over-Weight ,Obese)
    Solution -- (Increase(Calorie Surplus),Maintain, Decrease(Clorie-Defficiet))
    
    '''
    #- This function is used to calculate bmi of user
    
    bmi=weight/(height*height)
    #print("Hello",name)
    #print("Your BMI is ",x)
    #-------------------------
    #to get the body situation
    #print("\n")
    #print(name,"your body situation is")
    if(bmi<=18.5):
        status="Under Weight"
    elif(bmi>18.5 and bmi<=24.9):
        status="Normal Weight"
    elif(bmi>=25 and bmi<29.9):
        status="Over Weight"
    elif(bmi>=29):
        status="Obese"
    #--------------------------
    #to get solution
    #print("\n")
    #print(name,"Your Goal Should Be")
    if (bmi <= 18.5):
        solution="High need to increase calories"
    elif (bmi > 18.5 and bmi <= 24.9):
        solution="Mainatain you calories"
    elif (bmi >= 25 and bmi < 29.9):
        solution="Decrease your calories"
    elif (bmi >= 29):
        solution="High need to be calorie deficiet"
        
    return bmi,status,solution
'''
print("Enter Name")
name=input()
print("Enter Age")
age=int(input())
print("Enter Height in metres")
height=float(input())
print("Enter Weight in kilograms")
weight=float(input())
print("Enter Gender")
gender=input()
bmi(name,weight,height)
'''

print(bmi(100,1.8))