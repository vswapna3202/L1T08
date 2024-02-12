# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

# FIX: Fixing brackets for the print statement below which is missing and causing compilation error
print("Welcome to the error program")

# FIX: Fixing the brackets for the print statement below which is missing and also indenting it correctly
# which is cauing compilation error
print("\n")

# Variables declaring the user's age, casting the str to an int, and printing the result
#FIX: Fixing age_Str as it is indented incorrectly as this causes compilation error 
# and also the == which is for comparison changing it to = which is assignment. This causes runtime error

age_Str = "24 years old"

#FIX: Fixed the intendation which causes compilation error. Fixed age to have only numeric part of age_Str
#otherwise it gives runtime error as converting a string which has alphabets to integer is not allowed

age = int(age_Str[0:2]) 

#FIX: int age cannot be conctenated with String and printed. Gives runtime error so changed this to
#reflect by using f in print statement
print(f"I'm  {age} years old.")

# Variables declaring additional years and printing the total years of age
#FIX: Incorrect indentation fixed it to correct indentation which causes compilation error. 
# Also casting years_from_now to int so addition operation can be performed which otherwise causes
# runtime error as its string
years_from_now = "3"
total_years = age + int(years_from_now)

#FIX: Added parantheses to the print statement which was missing which causes compilation error
# and changed "answer_years" to total_years variable as this needs printing logical error as there is no 
# variable as answer_years and displaying it inside quotes will treat it as a string
print(f"The total number of years: {total_years}")

# Variable to calculate the total amount of months from the total amount of years and printing the result
#FIX: Changed total which does not exist to total_years variable. This causes compilation error as 
# total is not defined.
total_months = total_years * 12

#FIX: Added parantheses to print statement which was missing and added the formatting which causes compilation error. 
# Also added 6 to total_months as it is 3 years and 6 months from now only 3 years was converted to 
# months this is a logical error and fixed this
# Runtime error is caused as total_months is a int and concatenated to String in print statement
# either convert this to string or use f or .format in print statement
print(f"In 3 years and 6 months, I'll be {total_months+6} months old")

#HINT, 330 months is the correct answer

