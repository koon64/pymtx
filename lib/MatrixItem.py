class MatrixItem:
    def __init__(self, item_type, tag, groups, matrix_instance, thing_type=None):
        self.type = item_type
        self.tag = tag
        self.matrix_instance = matrix_instance
        self.groups = self.matrix_instance.add_groups(groups, self)
        self.thing_type = thing_type

    def __str__(self):
        return "[ MTX "+self.type.upper()+" <" + self.tag + "> ]"
