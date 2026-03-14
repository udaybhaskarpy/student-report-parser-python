#2
#Name 86:78:98,Name 67:20:94


Total_students=int(input())
Student_info=input()
info_list=Student_info.split(",")     #Name and marks both but of one student (Name 86:78:98) 

print("Number of students :",Total_students)

names=[]
marks=[]
info_dicti={}

for i in info_list:
    Name,Mark=i.strip().split()
    info_dicti[Name]=Mark
    names.append(Name)
    marks.append(Mark)

Maths_marks=[]
Science_marks=[]
English_marks=[]

for i in marks:
    Maths,Science,English=i.strip().split(":")
    Maths_marks.append(int(Maths))
    Science_marks.append(int(Science))
    English_marks.append(int(English))

marks2=[]
for i in marks:
    Mark1,Mark2,Mark3=i.strip().split(":")
    marks2.append(int(Mark1))
    marks2.append(int(Mark2))
    marks2.append(int(Mark3))

Student_marks=[]

for i in range (0,len(marks2),3):
    student_marks=marks2[i:i+3]
    Student_marks.append(student_marks)
    

for i in range(len(names)):
    print(names[i],":",Student_marks[i])
 
def student_report (marks2,Student_marks,names):
    Average_list=[]
    for i in Student_marks:
        Total=sum(i)
        Addends=len(i)
        Average=Total/Addends
        Average_list.append(Average)
    for i in range(len(Average_list)):
        if Average_list[i]>=90:
            print(names[i],":",Average_list[i],":","A")
        elif Average_list[i]>75 and Average_list[i]<89:
            print(names[i],":",Average_list[i],":","B")
        elif Average_list[i]>60 and Average_list[i]<74:
            print(names[i],":",Average_list[i],":","C")
        elif Average_list[i]<60:
            print(names[i],":",Average_list[i],":","D")
    Class_total=sum(marks2)
    Class_addends=len(marks2)
    Class_average=Class_total/Class_addends
    print("Class average :",Class_average)  
    Class_topper_average=max(Average_list)
    position=Average_list.index(Class_topper_average)                                                                                                          
    Class_topper=names[position]
    print("Topper :",Class_topper,"(",Class_topper_average,")")



    Passed_students=[]
    Failed_students=[]
    for i in Average_list:
        if i >=40:
            Passed_students=+1
        else:
            Failed_students=+1
            
    print("Number of passed students :",Passed_students)
    print("Number of failed students :",Failed_students)



            

student_report(marks2,Student_marks,names)
