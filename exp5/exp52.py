# Library Dictionary Program

# Step 1: Create dictionary
library = {
    "Python Basics": 300,
    "Data Structures": 450,
    "AI Fundamentals": 600
}

# Step 2: Display current books and prices
print("Library Books and Prices:")
for book, price in library.items():
    print(book, ":", price)

# Step 3: Take input from user
book_name = input("\nEnter the book name to update price: ")

# Step 4: Check and update price
if book_name in library:
    new_price = float(input("Enter new price: "))
    library[book_name] = new_price
    print("\nPrice updated successfully!")
else:
    print("\nBook not found in library.")

# Step 5: Display updated dictionary
print("\nUpdated Library:")
for book, price in library.items():
    print(book, ":", price)
