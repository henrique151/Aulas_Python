student_heights = input("Input a list of student heights ").split()
quati_students = 0
total_students = 0
final_result = 0 

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# 🚨 Não altere o código acima 👆

# Escreva o seu código abaixo desta linha 👇
for a in student_heights:
    quati_students += 1
    total_students += a
    final_result = round(total_students / quati_students)
print(final_result)