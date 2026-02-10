# program to find out leap year 
"""
Created on Tue Feb 10 12:15:32 2026

@author: prajwal gogawale
"""
year = int(input("Enter year."))

if(year%400 == 0)or(year%4 == 0 and year%100!=0):
    print("Leap year")
else:
# %%
    print("Not leap year")
