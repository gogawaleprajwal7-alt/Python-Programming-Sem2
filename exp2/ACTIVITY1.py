# -*- coding: utf-8 -*-
"""
Created on Mon May 11 10:42:17 2026

@author: Prajwal Gogawale
"""

class MovieTicket:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Check eligibility
    def check_eligibility(self):
        if self.age >= 18:
            return "Eligible for movie ticket 🎟️"
        else:
            return "Not eligible (Age must be 18 or above) ❌"

    # Display details
    def display(self):
        print("\nMovie Ticket Details")
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")
        print(self.check_eligibility())


# Main program
name = input("Enter your name: ")

try:
    age = int(input("Enter your age: "))

    person = MovieTicket(name, age)
    person.display()

except ValueError:
    print("Invalid input! Please enter a valid age.")
