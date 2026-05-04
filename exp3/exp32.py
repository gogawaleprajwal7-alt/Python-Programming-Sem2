- coding: utf-8 -*-
"""
Created on Mon May  4 10:50:11 2026

@author: User
"""

def calculate_simple_interest(principal, rate, time):
    # Simple Interest formula: SI = (P * R * T) / 100
    si = (principal * rate * time) / 100
    return si

# Taking input from user
p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time (in years): "))

# Function call
interest = calculate_simple_interest(p, r, t)

print("Simple Interest =", interest)# -*
