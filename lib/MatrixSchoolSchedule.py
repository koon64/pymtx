from lib.MatrixSchoolRotation import MatrixSchoolRotation


class MatrixSchoolSchedule:
    def __init__(self):
        self.rotations = []

    def add_rotation(self, rotation_obj):
        if type(rotation_obj) is MatrixSchoolRotation:
            self.rotations.append(rotation_obj)

    def set_rotation(self, rotation_obj, rotation):
        if type(rotation_obj) is MatrixSchoolRotation:
            self.rotations[rotation] = rotation_obj
