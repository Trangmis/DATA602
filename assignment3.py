# -*- coding: utf-8 -*-
"""Assignment3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T6JHh2JIyGG_lzqsNBPaDgaIbgVAGVFm

Trang Do - Assignment 3

Q1: Write a program that prompts the user for a meal: breakfast, lunch, or dinner. Then using if
statements and else statements print the user a message recommending a meal. For example,
if the meal was breakfast, you could say something like, “How about some bacon and eggs?”
The user may enter something else in, but you only have to respond to breakfast, lunch, or
dinner.
"""

def meal():
  meal = input('What is your choice? breakfast, lunch or dinner? : ' )

  if (meal == 'breakfast'):
      choice = input('How about some egg and cheese? (yes/no)')
      if (choice == 'yes'):
        print('You have breakfast with some egg and cheese')
      else:
        print('You have breakfast without egg and cheese')
  elif (meal == 'lunch'):
    print('Enjoy your lunch')
  elif (meal == 'dinner'):
    print('Bon appetit!')  
  else:
    print('Sorry! There is no option in the menu')  

meal()

"""Q2: The mailroom has asked you to design a simple payroll program that calculates a student
employee’s gross pay, including any overtime wages. If any employee works over 20 hours in a
week, the mailroom pays them 1.5 times their regular hourly pay rate for all hours over 20.
You should take in the user’s input for the number of hours worked, and their rate of pay.
"""

def payroll():
  hrs = float(input('Working Hours : '))
  payrate = float(input('hourly pay rate : '))
  if (hrs < 0):
    print('Input Error')
  elif (hrs < 20):  
    total = hrs 
    print('Total Pay:', payrate*total)
  else:
    total = hrs + (hrs - 20)*1.5
    print('Total Pay:', payrate*total)

payroll()

"""Q3: Write a function named times_ten. The function should accept an argument and display the
product of its argument multiplied times 10.
"""

def times_ten(input_number):
  try:
    input_var = float(input_number) 
    return (input_var*10)
  except: 
    print ('Invalid input')

times_ten('hhhh')    
times_ten('8.6')

"""Q4: Find the errors, debug the program, and then execute to show the output.

def main()
Calories1 = input( "How many calories are in the first food?")
Calories2 = input( "How many calories are in the first food?")

showCalories(calories1, calories2)

def showCalories()
print(“The total calories you ate today”, format(calories1 + calories2,.2f))

Errors:
1. main() is missing :
2. def showCalories() is missing :
3. showCalories(calories1, calories2) is passing undefined variables.
4. Missing 
  if __main__() =='__main__':
      main()  
5. The value from input command is a string so it has to convert to number to run operation + 
6. the format function is incorrect syntax.
     
"""

def showCalories(calories1, calories2):
  txt = 'The total calories you ate today {calories:.2f}'
  print(txt.format(calories = float(calories1) + float(calories2)))

def main():
  Calories1 = input( "How many calories are in the first food? ")
  Calories2 = input( "How many calories are in the second food? ")
  showCalories( Calories1,  Calories2)

if __name__ =='__main__':
  main()

"""Q5: Write a program that uses any loop (while or for) that calculates the total of the
following series of numbers:
1/30 + 2/29 + 3/28 .............29/30 + 30/1
"""

import numpy as np

def series_sum(input_number):
  var_input = int(input_number)
  result = 0
  if  var_input > 0 :
      for i in range(1,var_input ):
        result = result + i/(var_input - i)
      return result
  else:
    return False   

series_sum(30)

"""Q6: Write a function that computes the area of a triangle given its base and height.
The formula for an area of a triangle is:
AREA = 1/2 * BASE * HEIGHT
"""

import numpy as np

def triangle_area(base,height):
    return (float(base)*float(height))/2

triangle_area(5, 4)