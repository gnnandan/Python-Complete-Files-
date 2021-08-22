student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)


least_score = student_scores[0]
for score in student_scores:
    if score < least_score:
        least_score = score
print(f"The least score in the class is: {least_score}")