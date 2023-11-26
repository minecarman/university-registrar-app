while True: # Works as long as user does not enter Exit value(10).
    option = input("""Enter what you want to do:
1) List all courses.
2) List all the course that have at least one student registered.
3) Add a new course.
4) Search a course by course code.
5) Search a course by name.
6) Register a student to a course.
7) List all the students and their registered courses.
8) List top 3 most crowded courses
9) List top 3 students with the most course registrations
10) Exit the program\n""")

    if option == "1":
        course = open("course.txt", "r")
        for lines in course:
            temp = lines.split(";") # Every line uses a temporary variable and gets printed.
            print("Course Code: {},  Course Name: {},  Course Instructor: {},  Student Number: {}".format(temp[0], temp[1], temp[2], temp[3].replace("\n", "")))
        input("Press enter to continue...")
        course.close()

    elif option == "2":
        course = open("course.txt", "r")
        for lines in course:
            temp = lines.split(";") # Every line uses a temporary variable and gets printed if the student number is higher than 0.
            if int(str(temp[-1]).replace("\n", "")) > 0:
                print("Course Code: {},  Course Name: {},  Course Instructor: {},  Student Number: {}".format(temp[0], temp[1], temp[2], temp[3].replace("\n", "")))
        input("Press enter to continue...")
        course.close()

    elif option == "3":
        course = open("course.txt", "a")
        newCourse = input("Enter the course you want to add like this: coursecode;coursename;instructorname")
        course.write(newCourse + ";0\n") # Writes to text file what the user enters.
        input("Press enter to continue...")
        course.close()

    elif option == "4":
        course = open("course.txt", "r")
        search = input("Enter the code you want to search: ").upper() # If user inputs ceng1007, program can show CENG1007.
        for lines in course:
            temp = lines.split(";")
            if temp[0] == search: # Searches the course code in every line
                print("Course Code: {},  Course Name: {},  Course Instructor: {},  Student Number: {}".format(temp[0], temp[1], temp[2], temp[3].replace("\n", "")))
                break
        else:
            print("There is no course with that code.")
        input("Press enter to continue...")
        course.close()

    elif option == "5":
        course = open("course.txt", "r")
        search = input("Enter the course name you want to search: ").lower()
        for lines in course:
            temp = lines.split(";")
            if search in temp[1].lower(): # Shows the course if searched item is in any line.
                print("Course Code: {},  Course Name: {},  Course Instructor: {},  Student Number: {}".format(temp[0], temp[1], temp[2], temp[3].replace("\n", "")))
        input("Press enter to continue...")
        course.close()

    elif option == "6":
        studentf = open("student.txt", "r")
        coursef = open("course.txt", "r")
        studentdata = studentf.readlines()
        coursedata = coursef.readlines()
        studentf.close()
        coursef.close()
        regStudent = input("Enter the student ID you want to register").strip()
        regCourse = input("Enter course code you want to register the student").strip().upper()

        for i in range(len(studentdata)):
            if regStudent in studentdata[i]: # Searches for the student that is wanted to be registered.
                if studentdata[i][-1] == ";": # Writes without putting a comma if there is no registered course for student.
                    studentdata[i] = studentdata[i].replace("\n", "") + regCourse + "\n"
                else:
                    studentdata[i] = studentdata[i].replace("\n", "") + "," + regCourse + "\n"
                break

        for j in range(len(coursedata)):
            if regCourse == coursedata[j].split(";")[0]: # Searches for the course that is wanted to be registered for the student.
                splitteddata = coursedata[j].split(";")
                coursedata[j] = splitteddata[0] + ";" + splitteddata[1] + ";" + splitteddata[2] + ";" + str(int(splitteddata[3].replace("\n", ""))+1) + "\n" # Only adds +1 to student count of course.
                break

        with open("student.txt", "w") as students:
            students.writelines(studentdata) # Overwrites new data over the text file.
            with open("course.txt", "w") as courses:
                courses.writelines(coursedata) # Overwrites new data over the text file.
        input("Press enter to continue...")

    elif option == "7":
        student = open("student.txt", "r")
        for stdnt in student:
            tempStudent = stdnt.split(";") # Gives a temporary value for every student line.
            tempCourses = tempStudent[2].replace("\n", "").split(",") # Gives a temporary value for every course.
            print(tempStudent[1], tempStudent[0], tempCourses)
        input("Press enter to continue...")
        student.close()

    elif option == "8":
        course = open("course.txt", "r")
        courseList = []
        for c in course:
            temp = c.split(";")
            courseList.append(temp[3].replace("\n", "") + " Students in the course  " + temp[0] + "  " + temp[1] + "  " + temp[2]) # Appends all courses to a list.
        sortedlist = sorted(courseList, reverse=True) # Makes a sorted list of all courses.
        print(sortedlist[:3]) # Prints the sorted list until fourth one.
        input("Press enter to continue...")
        course.close()

    elif option == "9":
        student = open("student.txt", "r")
        stdntCrsList = []
        for stdent in student:
            stdentTemp = stdent.split(";")
            courseTemp = str(len(stdentTemp[2].split(",")))
            stdntCrsList.append(courseTemp + " Courses  " + stdentTemp[1] + "  " + stdentTemp[0]) # Appends all students to a list.
        sortedlist = sorted(stdntCrsList, reverse=True) # Makes a sorted list of all students.
        print(sortedlist[:3]) # Prints the sorted list until fourth one.
        input("Press enter to continue...")
        student.close()

    elif option == "10":
        break

    else:
        print("Wrong entry")
        input("Press enter to continue...")