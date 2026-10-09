def student_inf(name, id, age):
    return {
        "name": name,
        "student_id": id,
        "age": age,
    }

def add_student(student_list, new_student):
    student_list.append(new_student)
    return student_list