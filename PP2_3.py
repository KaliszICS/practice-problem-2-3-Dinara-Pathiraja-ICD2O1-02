'''
    Lesson: Else if
    Author: Dinara Pathiraja
    Date Created: Oct 16, 2024
    Date Last Modified: Oct 16, 2024
'''

def q1(): 
  word= input("In: ")
  if (word[-1:]=="-y"):
    print("ies")
  elif(word[-2:]=="-ey"): 
    print("eys")
  elif(word[-1:]=="-ife"):
    print("-ives")
  else:
    print("-s")
  
def q2(): 
  num= input ("Input an integer: ")
  num = int(num)
  if(num>0):
    print(f"{num} is positive")
  elif (num<0):
    print(f"{num} is negative")
  else: 
    print()
def q3():
  side1 = input("Input a number: ")
  side1= float(side1)
  side2 = input("Input a number: ")
  side2= float(side2)
  side3 = input("Input a number: ")
  side3= float(side3)
  if(side1==side2==side3):
    print("Equilateral")
  elif((side1 == side2 != side3) or (side1 == side3 != side2)or (side2 == side3 != side1)):
    print ("Isosceles")
  elif((side1!=side2!=side3)):
    print("Scalene")
  else:
    print("No Triangle")


#Do not alter the following code
#Comment out the following code when running your tests

q1()
q2()
q3()