student_answer = input("Are you a student? Type Y or N: ")
age = int(input("Enter your age: "))
membership_answer = input("Do you have a membership card? ")

is_student = student_answer == "Y"
has_membership_card = membership_answer == "Y"
is_student_or_senior = is_student or age >= 65

if is_student_or_senior and has_membership_card:
	print("You are eligible for a discount.")
else:
	print("You are not eligible for a discount.")

#This program is more complex than the previous ones because it uses multiple confusing conditions.
#Firstly, it asks if the user is a student, their age, and if they have a membership card.
#Next, it checks if the user is a student or a senior and if they have a membership card.
#Finally, it prints if the user is eligible for a discount or not.