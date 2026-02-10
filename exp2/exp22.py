# program to find factorial number 
"""
Created on Tue Feb 10 12:41:26 2026

@author: prajwal gogawale
"""

n=int(input("Enter number."))

fact = 1

for i in range(1,n + 1):
       
    fact = fact*i
     
print("Factorial:",fact)
