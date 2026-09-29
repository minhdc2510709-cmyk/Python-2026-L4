import math
import numpy as np
def student_inf(name, id, age):
    return{
        "name": name,
        "student_id": id,
        "age": age,
    }
def courses_inf(name, num_of_lessons, course_id):
    return{
        "name": name,
        "num_of_lessons": num_of_lessons,
        "course_id": course_id,
    }
def courses_state(name,course_name, point):
    if isinstance(point, list):
        round_point = []
        for p in point:
            decimal = math.floor(p * 10) / 10
            round_point.append(decimal)
    return{
        "id": name,
        "course_name": course_name,
        "point" : round_point
    }
def add_student(student_list, new_student):
    student_list.append(new_student)
    return student_list
def add_course(course_list, new_course):
    course_list.append(new_course)
    return course_list
def student_mark(table, student_mark):
    table.append(student_mark)
    return table

all_students = []
number_students = int(input("Số lượng hs: "))
for i in range(number_students):
    print(f"hs thứ {i+1: }")
    name = input("tên: ")
    id = input("id hs: ")
    age = int(input("tuổi: "))

    st = student_inf(name, id, age)
    add_student(all_students, st)

all_courses = []
number_courses = int(input("Số lượng khóa: "))
for j in range(number_courses):
    print(f"khóa học thứ {i + 1}")
    name = input("tên khóa: ")
    number = int(input("số buổi hc: "))
    id = input("Id khóa: ")

    cou = courses_inf(name, number, id)
    add_course(all_courses, cou)

table_mark = []
num_marks = int(input("Nhập số lượng bảng điểm muốn thêm: "))
for i in range(num_marks):
    print(f"Bảng điểm thứ {i+1}:")
    id = int(input("Nhập mã học sinh (id): "))
    c_name = input("Nhập tên môn học: ")
    raw_points = input("Nhập mảng điểm (cách nhau bởi dấu cách, vd: 7 8 9 10): ")
    points_list = raw_points.split()

    converted_point_list = []
    for p in points_list:
        decimal = math.floor(int(p)*10)/10
        converted_point_list.append(decimal)

    
    s_avg = np.mean(converted_point_list)
    s_mark = courses_state(id, c_name, converted_point_list)

    s_sorted = converted_point_list.sort(reverse=True)
    student_mark(table_mark, s_mark)

print("Điểm", table_mark)
print("Điểm tb", s_avg)
print("điểm theo thứ tự giảm dần", s_sorted)
   


