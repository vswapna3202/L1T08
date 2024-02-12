# This program reads the base and height and prints the area of a triangle

#compilation error as input statement has no parantheses for both base and height
# correct statement is as commented out
#base = input("Enter base of triangle: ")
#height = input("Enter height of triangle: ")

base = input "Enter base of triangle: " #compilation error: () missing
height = input "Enter height of triangle: " #compilation error: () missing

#runtime error as base and height are not converted to int before performing calculations on them
# can't multiply sequence by non-int of type 'str' error is thrown
# correct statement is commented out
#area = ( int(base) * int(height) ) / 2
area = ( base * height ) / 2    #runtime error: base and height are string & arithmetic ops are done

#syntax of print statement is incorrect and it will not print value of area it will just print 
#string {area}. As the intent is to display value of area and that is not output this is a logical
#error
print ("Area of triangle is: {area}")   #logical error: f is missing so value of area not printed
#print (f"Area of triangle is: {area}")