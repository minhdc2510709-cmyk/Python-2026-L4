from input import input_students, input_courses, input_marks

def main():
    print("--- QUẢN LÝ HỌC SINH ---")
    students = input_students()

    print("\n--- QUẢN LÝ KHÓA HỌC ---")
    courses = input_courses()

    print("\n--- QUẢN LÝ BẢNG ĐIỂM ---")
    marks = input_marks()

if __name__ == "__main__":
    main()