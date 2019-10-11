'''
Created by Vedant Christian
Created on 11 / 10 / 2019
'''

UserInput = int(input("Upto what number do you want the Fibonacci sequence. "))

def Fibonacci(n):
     a, b = 0, 1
     while a < n:
         print(a)
         a, b = b, a+b
     print()
     
Fibonacci(UserInput)
