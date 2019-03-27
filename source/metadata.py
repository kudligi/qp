import os


#print(courses)

def get_course_list():
    courses = os.listdir('./data')
    return courses

def get_departments_list(course):
    courses = get_course_list()
    if course not in courses:
        return "Invalid course input"
    departments = os.listdir('./data/' + course)
    return departments

def get_papers_list(course, department):
    departments = get_departments_list(course)
    if departments == "Invalid course input":
        return "Invalid course input"
    if department not in departments:
        return "Invalid department input"

    papar_list = os.listdir('./data/' + course + '/' + department)
    return papar_list


#print(get_course_list())
#print(get_departments_list('apple'))
#print(get_departments_list('UG'))
print(get_papers_list('UG','community_medicine_1'))