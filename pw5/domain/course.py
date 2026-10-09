def courses_inf(name, num_of_lessons, course_id):
    return {
        "name": name,
        "num_of_lessons": num_of_lessons,
        "course_id": course_id,
    }

def add_course(course_list, new_course):
    course_list.append(new_course)
    return course_list