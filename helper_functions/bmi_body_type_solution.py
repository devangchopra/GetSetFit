def bmi(name,weight,height):
    #- This function is used to calculate bmi of user
    # x=bmi
    x=weight/(height*height)
    print("Hello",name)
    print("Your BMI is ",x)
    #-------------------------
    #to get the body situation
    print("\n")
    print(name,"your body situation is")
    if(x<=18.5):
        print("Under-Weight")
    elif(x>18.5 and x<=24.9):
        print("Normal Weight")
    elif(x>=25 and x<29.9):
        print("Over-Weight")
    elif(x>=29):
        print("Obese")
    #--------------------------
    #to get solution
    print("\n")
    print(name,"Your Goal Should Be")
    if (x <= 18.5):
        print("High need to increase calories")
    elif (x > 18.5 and x <= 24.9):
        print("Mainatain you calories")
    elif (x >= 25 and x < 29.9):
        print("Decrease your calories")
    elif (x >= 29):
        print("High need to be calorie deficiet")


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

