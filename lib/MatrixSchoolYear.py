from lib.MatrixSchoolQuarter import MatrixSchoolQuarter
from lib.MatrixSchoolSemester import MatrixSchoolSemester


class MatrixSchoolYear:
    def __init__(self, year):
        self.year = year
        self.quarters = [MatrixSchoolQuarter(quarter) for quarter in range(0, 4)]
        self.semesters = [MatrixSchoolSemester(semester) for semester in range(0, 2)]
        self.music = None
        self.sports = []

    def __str__(self):
        return self.year

    @property
    def gpa(self):
        gpa = 0
        valid_quarters = 0
        for quarter in self.quarters:
            if quarter.gpa > 0:
                gpa += quarter.gpa
                valid_quarters += 1
        return gpa / valid_quarters
