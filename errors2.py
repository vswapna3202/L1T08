# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

#FIX: Lion should be a string so added it within "". It otherwise  causes compilation error as since
# Lion is not within quotes compiler assumes it is a variable and looks for it and doesn't find it
animal = "Lion"
animal_type = "cub"
number_of_teeth = 16

#FIX: Added f before the String as otherwise the values held by variables animal, number_of_teeth and 
# animal_type will not be printed. Also changed the message to show it has 16 teeth instead of it is 
# a 16. This is a logical error missing f will print the sentence within quotes as just a string
full_spec = f"This is a {animal}. It has {number_of_teeth} teeth and it has {animal_type} teeth"

#FIX: print statement missing parantheses added it. Compilation error as paranthesis is missing
print(full_spec)

