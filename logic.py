# This program displays student_award as A* if 4 or more out of 5 grades are above 80, displays A if 3 out of 
# 5 grades are above 80 and displays B if 2 out of 5 grades are equal or above 80 and displays C if 1 out of 5 
# grades are above 80 and displays D if no grades are above 80

#Multiple logic errors added in this program. First for loop should read i in range(0,5)
#Second error if loop should be >= 80 not just >
#So instead of displaying A* which is correct result it displays B

student_grades = [80,60,90,89,80] #Set student_grades variable to hold 5 grades of student

grade_count = 0
for i in range(0,4):    #logical error loop should be 0, 5 as there are 5 elements    
    if (student_grades[i] > 80): #logical error the requirement is <= 80 <80 will be false if grade is 80
        grade_count += 1        
if grade_count >= 4:
    print ("Fantastic! You got an A*")
elif grade_count == 3:
    print("Well Done! You got an A")
elif grade_count == 2:
    print("Great effort! You got a B")
elif grade_count == 1:
    print("Better luck next time! You got a C")
elif grade_count == 0:
    print("You got a D")
