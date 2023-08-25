# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
score_max_student = 0
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

for a in student_scores:
  if a > score_max_student:
    score_max_student = a
print(f"The highest score in the class is: {score_max_student}")
