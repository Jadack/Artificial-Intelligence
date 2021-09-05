# Jack Pacheco - Individual Practice 01

# Python Imports
import sys
import datetime
import math

# Exercise 01:
def stringFormat():
  print('******************************')
  print('Exercise 01: ')
  print('******************************')
  print('Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!')
  print('')

# Exercise 02:
def getPythonVersion():
  print('******************************')
  print('Exercise 02: ')
  print('******************************')
  print('Python Version: ', sys.version)
  print('')

# Exercise 03
def getCurrentDate():
  print('******************************')
  print('Exercise 03: ')
  print('******************************')
  print('Current Date: ', datetime.date.today())
  print('Formated Datetime: ', datetime.datetime.now().strftime('%d/%m/%Y (%H:%M)'))
  print('')

# Exercise 04
def getCircleArea():
  print('******************************')
  print('Exercise 04: ')
  print('******************************')
  radio = float(input('Insert the circle radio: '))
  print('The area is: ', (math.pi * (math.pow(radio, 2))))
  print('')

# Exercise 05
def reverseFullName():
  print('******************************')
  print('Exercise 05: ')
  print('******************************')
  firstName = input('Write your First Name: ')
  lastName = input('Write your Last Name: ')
  print(f'Hello {lastName} {firstName}!')
  print('')

# Exercise 06
def generateTupleAndList():
  print('******************************')
  print('Exercise 06: ')
  print('******************************')
  numbers = input('Insert the numbers: ')
  numbersList = numbers.split(',')
  numbersTuple = tuple(numbersList)
  print('Numbers List: ', numbersList)
  print('Numbers Tuple: ', numbersTuple)
  print('')

# Exercise 07
def getFileExtension():
  print('******************************')
  print('Exercise 07: ')
  print('******************************')
  filename = input('Insert the file name: ')
  print('The extension is: ', filename.split('.')[1])
  print('')

# Exercise 08
def maxOfArrayNumbers():
  print('******************************')
  print('Exercise 08: ')
  print('******************************')
  numbersList = [0, 1, 1, 2, 3, 5, 8, 13]
  print('Numbers List: ', numbersList)
  print('The max is: ', max(numbersList))
  print('')

# Exercise 09
def fizz_buzz():
  print('******************************')
  print('Exercise 09: ')
  print('******************************')
  number = int(input('Insert the number: '))
  if number % 3 == 0 and number % 5 == 0:
    print('The result is: ', 'FizzBuzz')
  elif number % 3 == 0:
    print('The result is: ', 'Fizz')
  elif number % 5 == 0:
    print('The result is: ', 'Buzz')
  else:
    print('The result is: ', number)
  print('')

# Exercise 10
def speedChecking(speed):
  print('******************************')
  print('Exercise 10: ')
  print('******************************')
  demerit = 0
  if speed <= 70:
    print('Ok')
  elif speed > 70:
    demerit += int(((speed - 75) / 5) + 1)
    print(f'Speed: {speed} km/h')
    print('Demerit Points: ', demerit)
  if demerit >= 12:
    print('License Suspended')
  print('')

# Functions Execution
# stringFormat()
# getPythonVersion()
# getCurrentDate()
# getCircleArea()
# reverseFullName()
# generateTupleAndList()
# getFileExtension()
# maxOfArrayNumbers()
# fizz_buzz()
speedChecking(80)