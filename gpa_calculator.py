# asks for 8 class grades in the form of intergers
#tell py to add them
# tell py to divide them
#display average as a float
# display letter grade

print("Welcome to my gpa calculator! This is built for a course load of 8 with no multipliers")
grade_list = []
for x in range(8):
    grade=int(input(f"Please enter your grade {x+1}:"))
    grade_list.append(grade)

average=float(sum(grade_list)/8)

print(f" This is your average {average}")
if average >= 90:
    print("You have earned an A !")
elif average >= 80:
    print("You earned a B!")
elif average >= 70:
    print("You earned a C!")
else:
    print("You failed... better luck next semester!")

print("Thank You for using my gpa calculator!!!!!!!")