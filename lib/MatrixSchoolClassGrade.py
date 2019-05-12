class MatrixSchoolClassGrade:
    def __init__(self, name, final_grade, assignments):
        self.name = name
        self.grade = float(final_grade) if final_grade is not None else None
        self.assignments = assignments
        self.has_linked_class = False
        self.linked_class = None

    def link_class(self, class_obj):
        self.linked_class = class_obj
        self.has_linked_class = True

