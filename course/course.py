from department.department import Department

class Course():
    """
    Represents template for a course
    """

    def __init__(self, name:str, department:Department, credit_hours:int):
        

        if len(name.strip())>8:
            self.__name = name
        else:
            raise ValueError("Name cannot be blank")
        
        if isinstance(department, Department):
            self.__department = department
        else:
            raise ValueError ("Department must be one of predefined Departments.")
        if isinstance (credit_hours,int):

            self.__credit_hours = credit_hours
        else:
            raise ValueError ("Credit hours must be a whole number.")
        

    #Accessors

    @property
    def name(self) -> str:
        return self.__name
    @property
    def department(self) -> Department:
        return self.__department
    @property
    def credit_hours(self) -> int:
        return self.__credit_hours


    def __str__(self) -> str:
        return (f"Course: {self.__name}"
        + f"\nDepartment: {self.__department.name.replace('_',' ').title()}"
        + f"\nCredit Hours: {self.__credit_hours}")