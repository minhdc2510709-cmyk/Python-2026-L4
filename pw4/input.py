import math
import numpy as np
from domain.student import student_inf, add_student
from domain.course import courses_inf, add_course
from domain.mark import courses_state, student_mark
from output import display_mark_results

def input_students():
    all_students = []
    number_students = int(input("Số lượng hs: "))
    for i in range(number_students):
        print(f"hs thứ {i+1}")
        name = input("tên: ")
        id = input("id hs: ")
        age = int(input("tuổi: "))

        st = student_inf(name, id, age)
        add_student(all_students, st)
    return all_students

def input_courses():
    all_courses = []
    number_courses = int(input("Số lượng khóa: "))
    for j in range(number_courses):
        print(f"khóa học thứ {j + 1}")
        name = input("tên khóa: ")
        number = int(input("số buổi hc: "))
        id = input("Id khóa: ")

        cou = courses_inf(name, number, id)
        add_course(all_courses, cou)
    return all_courses

def input_marks():
    table_mark = []
    num_marks = int(input("Nhập số lượng bảng điểm muốn thêm: "))
    for i in range(num_marks):
        print(f"Bảng điểm thứ {i+1}:")
        id = input("Nhập mã học sinh (id): ")
        c_name = input("Nhập tên môn học: ")
        raw_points = input("Nhập mảng điểm (cách nhau bởi dấu cách, vd: 7 8 9 10): ")
        points_list = raw_points.split()

        converted_point_list = []
        for p in points_list:
            decimal = math.floor(float(p)*10)/10
            converted_point_list.append(decimal)

        s_avg = np.mean(converted_point_list)
        s_mark = courses_state(id, c_name, converted_point_list)
        s_sorted = sorted(converted_point_list, reverse=True)
        
        student_mark(table_mark, s_mark)

        # Gọi hàm xuất kết quả sau mỗi lần nhập điểm
        display_mark_results(table_mark, s_avg, s_sorted)
        
    return table_mark