from lib.MatrixSchoolSchedule import MatrixSchoolSchedule


class MatrixSchoolSemester:
    def __init__(self, semester):
        self.semester = semester
        self.schedule = None

    def __int__(self):
        return self.semester

    def __str__(self):
        return str(self.semester + 1)

    def set_schedule(self, schedule_obj):
        if type(schedule_obj) is MatrixSchoolSchedule:
            self.schedule = schedule_obj
            return True
        raise Exception("The schedule must be the MatrixSchoolSchedule obj")
