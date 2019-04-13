from lib.MatrixSchoolQuarter import MatrixSchoolQuarter
from lib.MatrixSchoolSemester import MatrixSchoolSemester


class MatrixSchoolYear:
    def __init__(self, year):
        self.year = year
        self.quarters = [MatrixSchoolQuarter(quarter) for quarter in range(0, 4)]
        self.semesters = [MatrixSchoolSemester(semester) for semester in range(0, 2)]

    def __str__(self):
        return self.year


