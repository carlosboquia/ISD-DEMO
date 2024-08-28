# 1. Import as necessary.
from course.course import Course
from department.department import Department


def main():
    # 1. Create an instance of the Course class with valid inputs.
    #    Print the instance.
    #    If an exception occurs, print the exception instance.
    try:
        intermediate_software_development = Course("Intermediate Software Development", Department.COMPUTER_SCIENCE, 6)
        print(intermediate_software_development)
    except ValueError as e:
        print(e)

    try:
        invalid_department = Course("Invalid Course", "Invalid Department",6 )
        print(invalid_department)
    except ValueError as e:
        print(e)

    




    # 2. Create an instance of the Course class with invalid inputs.
    # Print the instance.
    # If an exception occurs, print the exception instance.


if __name__ == "__main__":
    main()
    
    
    