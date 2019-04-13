from lib.MatrixSchoolClass import MatrixSchoolClass, MatrixSchoolFree
from unders import Underscore

_ = Underscore()


class MatrixSchoolRotation:
    def __init__(self, rotation):
        self.rotation = rotation
        self.classes = []

    def __str__(self):
        return _.assign_letter(self.rotation)

    def add_class(self, class_obj):
        if type(class_obj) is MatrixSchoolClass or MatrixSchoolFree:
            self.classes.append(class_obj)
        else:
            raise Exception("Class must be a MatrixSchoolClass or a MatrixSchoolFree")
