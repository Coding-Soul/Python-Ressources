# Sometimes you want a Input from a user, that is used as an integer in the code
# For this specific Case, we can use the type-casting function.

value1 = input("Enter first Number: ")
value2 = input("Enter second Number: ")

result = int(value1) + int(value2) # Defining result
print(result)

# The output of an userinput is a string by default
# If we use int(value1) we change it to an integer