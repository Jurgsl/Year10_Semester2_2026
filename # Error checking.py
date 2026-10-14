# Error checking
# Winnie Dong
# 25 Sept 2026

# Code that tests whether a valid input was given (v1)
done = True # Boolean variable set to True
while not done:
    num = int(input("Please enter your value as an interger:"))
    done = False
print(f"The number you entered is {num}")

# Using a try and except method to check for valid input.
# Use try and except method to catch errors
done = True
while done:
    try: # This method tries for a valid input
        num = float(input("Please enter a number: "))
        done = True
        
    except ValueError:
        print("That is not a valid float number. \nUse a fullstop as decimal indicator. \n")
        
print(f"The number you entered is {num}")

# Check for valid input and recyling code with a function (V1.2)
# Create a function to call every time I ask the user 
# for a number. A function is a chunl of code that does 
# something.
# Functions can be used over and over again
# To use a function (call it), write out its name
# parenthesis at the end
# To create a function, start with the word def
def input_check():
    while True
    try:
        num = float(input("Please enter a number: "))
        break
    except ValueError:
        print("That is not a valid float number.\n")
        
    print(f"The number")
    
# Main routine
input_check() #This call the function to be used.

# V1.3 Valid input checker
# Use parameters in the function
# more Pythonic
def input_check(question): # 'question' is a placeholder
    while True:
        error = "That is not a valid number."
        print(question)
        try:
            num = float(input())
        except ValueError:
            print(error)
            
    return(num) # Gives back the value of the num
                # so that I can use it outside of
                # The function.
    
    

# Main routine
num1 = input_check("Please enter your first number:")
print(f"The number you stored is {num1}")

num2 = input_check("Please enter the second number:")
print(f"The number you stored is {num2}")

sum = num1 + num2
print(f"Your numbers added together results is {sum}")