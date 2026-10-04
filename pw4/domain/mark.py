import math

def courses_state(name, course_name, point):
    round_point = []
    if isinstance(point, list):
        for p in point:
            decimal = math.floor(p * 10) / 10
            round_point.append(decimal)
    return {
        "id": name,
        "course_name": course_name,
        "point": round_point
    }

def student_mark(table, s_mark):
    table.append(s_mark)
    return table