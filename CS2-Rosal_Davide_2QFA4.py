num_stu = int(input("Enter number of students:"))
num_sub = int(input("Enter number of subjects:"))
total_stu_score = 0
total_stu_num = 0
for student in range(1,num_stu + 1):
    print("\nStudent " + str(student))
    total_stu = 0
    for subject in range(1,num_sub + 1):
        score = float(input("Enter score " + str(subject) + ": "))
        total_stu += score
    student_ave = total_stu/num_sub
    print ("Average for student " + str(student) + " = " + str(student_ave))
    total_stu_score += total_stu
    total_stu_num += num_sub
class_average = total_stu_score/total_stu_num
print("\nClass Average = " + str(class_average))


              
              