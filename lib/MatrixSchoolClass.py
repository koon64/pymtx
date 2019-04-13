class MatrixSchoolClass:
    def __init__(self, class_name, teacher, room, period):
        self.name = class_name
        self.teacher = teacher
        self.room = room
        self.period = period
        self.is_free = False


class MatrixSchoolFree:
    def __init__(self):
        self.is_free = True


