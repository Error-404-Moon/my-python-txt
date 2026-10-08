file = "C:/Users/Home/Estudents.txt"
def add_student():
    name = input("نام دانش‌آموز را وارد کنید: ")

    try:
        grade = int(input("نمره دانش‌آموز را به عدد وارد کنید: "))
        with open(file, "a", encoding="utf-8") as f:
            f.write(f"{name},{grade}\n")
        print("دانش‌آموز با موفقیت اضافه شد.")
    except ValueError:
        print("خطا: نمره باید عدد باشد.")


def show_students():
    try:
        with open(file, "r", encoding="utf-8") as f:
            students = f.readlines()
        if len(students) == 0:
            print("هیچ دانش‌آموزی ثبت نشده است.")
            return

        print("\n===== لیست دانش‌آموزان =====")
        for student in students:
            student = student.strip()
            name, grade = student.split(",")
            print(f"نام: {name} | نمره: {grade}")

    except FileNotFoundError:
        print("خطا: فایل students.txt وجود ندارد.")

def menu():
    while True:
        print("\n===== مدیریت نمرات دانش‌آموزان =====")
        print("1. افزودن دانش‌آموز")
        print("2. نمایش همه دانش‌آموزان")
        print("3. خروج")
        choice = input("انتخاب گزینه: ")
        match choice:            
            case "1":
                add_student()
            case "2":
                show_students()
            case"3":
                print("از برنامه خارج شدید.")
                break
            case _:
                print("گزینه نامعتبر است. دوباره تلاش کنید.")


menu()