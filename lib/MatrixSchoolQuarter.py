from lib.MatrixSchoolClassGrade import MatrixSchoolClassGrade
from lib.MatrixAssignment import MatrixAssignment


class MatrixSchoolQuarter:
    def __init__(self, quarter):
        self.quarter = quarter
        self.honors = None
        self.high_honors = None
        self.class_grades = []

    def __str__(self):
        return "Q{}".format(self.quarter + 1)
    
    def __int__(self):
        return self.quarter

    # sets honors role
    def set_honors(self, regular, high=False):
        self.honors = regular
        self.high_honors = high

    # sets a grade to a class in a quarter
    def add_class_grade(self, class_name, class_dict):
        if type(class_dict) is dict:
            assignments = []
            if "assignments" in class_dict:
                for assignment in class_dict['assignments']:
                    assignments.append(MatrixAssignment(assignment['name'], assignment['category'], assignment['score'],
                                                        assignment['total'], assignment['description']))
            class_grade = class_dict['final_grade'] if "final_grade" in class_dict else None
            self.class_grades.append(MatrixSchoolClassGrade(class_name, class_grade, assignments))

    @property
    def gpa(self):
        grades = []
        for class_grade in self.class_grades:
            if class_grade.grade is not None:
                grades.append(class_grade.grade)
        return sum(grades) / len(grades)
