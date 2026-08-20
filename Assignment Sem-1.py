def main():

    print("1- Maximum of three numbers")
    print("2- Lists")
    print("3- Tuples")
    print("4- Triangle")
    program = input("Which program would you like to run? (enter the number) ").strip()

    if program == "1":
        maxwork()
    elif program == "2":
        listwork()
    elif program == "3":
        tuplework()
    elif program == "4":
        trianglework()
    else:
        print("Invalid input. Please select 1, 2, or 3.")


def tuplework():

    courses = ("Python", "Data Science", "Cloud Computing", "Cyber Security", "AI")

    print(f"The Second Course selected by the student is: {courses[1]}")

    print(f"The Last Two Courses Selected by the student are: {courses[-2:]}")

    if "Python" in courses:
        print("Python is in the list of courses")
    else:
        print("Python is not in the list of courses")

    print(f"Cloud Computing is on the {courses.index('Cloud Computing') + 1} position in the list of courses")

    print(f"The total number of courses selected are: {len(courses)}")

    list_courses = list(courses)
    list_courses.append("Machine Learning")
    list_courses.append("Web Development")
    print("Machine Learning and Web Development have been added to the list of courses")

    list_courses.remove('Cyber Security')
    print("Cyber Security has been removed from the list of courses")

    list_courses.sort()
    print("The courses have been sorted in alphabetical order")
    sorted_courses = tuple(list_courses)

    backup_courses = sorted_courses
    print("A backup of the courses list has been created")

    friend_courses = ("AI", "Blockchain", "Python")

    combined_courses = sorted_courses + friend_courses
    print("Courses selected by the student and their friend have been combined")

    print(f"Courses: {courses}")
    print(f"Sorted Courses: {sorted_courses}")
    print(f"Backup Courses: {backup_courses}")
    print(f"Combined Courses: {combined_courses}")


def maxwork():

    print("We will find the largest of three numbers")
    numbers = []

    #change the range to change the number of inputs
    for i in range(3):
        numbers.append(float(input(f"Enter {i + 1} number: ")))

    #considering that the first number is the largest
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    print(f"The greatest number is {largest}")


def listwork():

    students = ["Aarav", "Isha", "Rohan", "Sneha", "Kabir"]

    students[2] = "Rohan Patil"
    print (f"The third student's name is now: {students[2]}")

    students.append("Ananya")
    students.append("Vihaan")
    print ("Ananya and Vihaan have been added to the list")

    students.remove("Kabir")
    print ("Kabir has been removed from the list")

    print(f"Total number of registered students: {len(students)}")

    if "Isha" in students:
        print("Isha is registered")
    else:
        print("Isha is not in list")

    students.sort()
    print("Students have been sorted in alphabetical order")

    backup_students = students.copy()
    print("A backup of the students list has been created")

    hackathon = ["Meera", "Arjun", "Isha"]
    print("A list of hackathon participants has been created")

    all_participants = students + hackathon
    print("The students and hackathon participants have been combined into a single list")

    print(f"Students in the Tech Fest: {students}")

    print(f"Backup list: {backup_students}")

    print(f"Combined Participants List: {all_participants}")


def trianglework():
    
    s1= int(input("Enter the length of the first side: "))
    s2= int(input("Enter the length of the second side: "))
    s3= int(input("Enter the length of the third side: "))
    
    if s1 == s2 == s3:
        print ("It is an Equilateral Triangle")
    
    elif s1 == s2 or s2 == s3 or s1 == s3:
        print ("It is an Isosceles Triangle")
        
    else:
        print ("It is a Scalene Triangle")


main()
