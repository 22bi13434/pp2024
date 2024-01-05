import os

student_name_dic = {}
student_dob_dic = {}
course_name_dic = {}
student_mark_dic = {}  # Nested dic
student_id_list = []
course_id_list =[]

course_num = int(input("Input number of course: "))
for i in range (0,course_num):
    course_id = input(f"Input course {i+1}'s ID: ")
    course_name = input(f"Input course {i+1}'s name: ")
    course_name_dic[course_id]=course_name
    course_id_list.append(course_id)
    os.system('clear')


student_num =  int(input("Input number of students in a class: "))
for i in range (0,student_num):
    name=input(f"Enter student {i+1}'s name: ")
    id=input(f"Enter student {i+1}'s ID: ")
    dob=input(f"Enter student {i+1}'s DOB: ")
    student_name_dic[id]=name
    student_dob_dic[id]=dob
    student_id_list.append(id)
    os.system('clear')

def change_student_num():
    global student_num
    student_num_temp = int(input("Input new number of students in a class: "))
    if student_num_temp > len(student_name_dic):
        student_num =  student_num_temp
    else:
        print("New number of students must be bigger than the current capacity")

def add_more_students():
    if len(student_name_dic) < student_num:
        for i in range (len(student_name_dic),student_num):
            name=input(f"Enter student {i+1}'s name: ")
            id=input(f"Enter student {i+1}'s ID: ")
            dob=input(f"Enter student {i+1}'s DOB: ")
            student_name_dic[id]=name
            student_dob_dic[id]=dob
    else:
        print("Class full capacity")
        print("Change number of students in a class first")

def change_course_num():
    global course_num
    course_num_temp = int(input("Input number of courses: "))
    if course_num_temp > len(course_name_dic):
        course_num = course_num_temp
    else:
        print("New number of course must be bigger than the current one")
def add_more_course_info():
    print(f"Add more course: {len(course_name_dic)}/{course_num} courses have information")
    if len(course_name_dic) < course_num:
        for i in range (len(course_name_dic),course_num):
            course_name = input(f"Input course {i+1}'s name: ")
            course_id = input(f"Input course {i+1}'s ID: ")
            course_name_dic[course_id] = course_name
            course_id_list.append(course_id)
    else:
        print("Change number of courses to add more course")
def list_all_students():
    i=1
    print("No - Student Name - Student ID - Date of Birth")
    for key, value in student_name_dic.items():
        print(f"{i}. {key} - {value} - {student_dob_dic[key]}")
        i=i+1
def list_all_course():
    i=1
    print("No - Course ID -  Course Name")
    for key, value in course_name_dic.items():
        print(f"{i}. {key} - {value}")
        i=i+1
def input_student_mark():
    list_all_course()
    print("")
    course_id = input("Input course ID to mark: ")
    if course_id in course_id_list:
        student_id = input("Input student ID to mark: ")
        if student_id in student_id_list:
            mark = int(input("Enter mark: "))
            if student_id not in student_mark_dic:
                student_mark_dic[student_id]={}
            student_mark_dic[student_id][course_id]= mark
            print("Mark successfully")
        else:
            print(f"Student ID {student_id} not exist")
    else:
        print(f"Course {course_id} not exist")
def show_student_mark():
    for id in course_id_list:
        print(f"Mark of Course: {course_name_dic[id]} - {id}:")
        print("No - Student Name - Student ID - Date of Birth - Mark")
        i=1
        for student_id in student_id_list:
            if student_mark_dic.get(student_id, {}).get(id) is not None:
                mark = student_mark_dic[student_id][id]
            else:
                mark = "NULL"
            print(f"{i}. {student_name_dic[student_id]} - {student_id} - {student_dob_dic[student_id]} - {mark}")
            i=i+1
        print("")

while True:
    print("")
    print("Choices:")
    print("1. Change number of students in a class")
    print("2. Add more students")
    print("3. Change number of courses")
    print("4. Add more courses")
    print("5. List all students")
    print("6. List all courses")
    print("7. Input student's mark")
    print("8. Show student's mark")

    print("0. Exit")

    choice = int(input("Enter choice: "))
    if choice == 1:
        os.system("clear")
        print("Change number of students in a class:")
        change_student_num()
    if choice == 2:
        os.system("clear")
        print("Add more students:")
        add_more_students()
    if choice == 3:
        os.system("clear")
        print("Change number of courses:")
        change_course_num()
    if choice == 4:
        os.system("clear")
        add_more_course_info()
    if choice == 5:
        os.system("clear")
        print("All students:")
        list_all_students()
    if choice == 6:
        os.system("clear")
        print("List all courses:")
        list_all_course()
    if choice == 7:
        os.system("clear")
        print("Input student's mark:")  
        input_student_mark()
    if choice == 8:
        os.system("clear")
        print("Show student's mark:")
        show_student_mark()
    if choice == 0:
        os.system("clear")
        print("Exited")
        break
