from input import input_students, input_courses, input_marks
import os
import zipfile
DATA_FILE = "students.dat"
FILES_TO_COMPRESS = ["students.txt", "courses.txt", "mark.txt"]

def main():
    # 1. Kiểm tra và giải nén ngay khi khởi động
    if os.path.exists(DATA_FILE):
        print(f"Phát hiện {DATA_FILE}, đang giải nén dữ liệu...")
        if os.path.exists(DATA_FILE):
            print(f"Phát hiện {DATA_FILE}, đang giải nén dữ liệu...")
            zipf = zipfile.ZipFile(DATA_FILE, 'r')
            zipf.extractall(".")
            zipf.close()
    print("--- QUẢN LÝ HỌC SINH ---")
    students = input_students()

    print("\n--- QUẢN LÝ KHÓA HỌC ---")
    courses = input_courses()

    print("\n--- QUẢN LÝ BẢNG ĐIỂM ---")
    marks = input_marks()

    print("\nĐang nén dữ liệu vào students.dat...")
    zipf = zipfile.ZipFile(DATA_FILE, 'w', zipfile.ZIP_DEFLATED)
    for file in FILES_TO_COMPRESS:
        if os.path.exists(file):
            zipf.write(file)
    zipf.close()
    print("Hoàn tất!")


if __name__ == "__main__":
    main()