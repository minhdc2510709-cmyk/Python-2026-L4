def student_inf(name, std_id, age):
    return{
        "name": name,
        "student_id": std_id,
        "age": age,
    }
def courses_inf(name, num_of_lessons, course_id):
    return{
        "name": name,
        "num_of_lessons": num_of_lessons,
        "course_id": course_id,
    }
def courses_state(std_name,course_name, point):
    return{
        "std_id": std_name,
        "course_name": course_name,
        "point" : point
    }
st1 = student_inf("An", 2333, 17)
st2 = student_inf("Minh", 2442, 17)

all_students = []
def add_student(student_list, new_student):
    student_list.append(new_student)
    return student_list

add_student(all_students, st1)
add_student(all_students, st2)
print("students: " , all_students)

all_course = []
def add_course(course_list, new_course):
    course_list.append(new_course)
    return course_list

c1 = courses_inf("maths", 12, 101)
c2 = courses_inf("art", 3, 202)

add_course(all_course, c1)
add_course(all_course, c2)
print("course: " , all_course)

table_mark = []
def student_mark(table, student_mark):
    table.append(student_mark)
    return table

s1 = courses_state(2333, "Maths", 7)
s2= courses_state(2442, "Maths", 9)

student_mark(table_mark, s1)
student_mark(table_mark, s2)

print("mark: ", table_mark)
    

