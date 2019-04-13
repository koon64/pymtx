class MatrixItem:
    def __init__(self, item_type, tag, groups, matrix_instance):
        self.type = item_type
        self.tag = tag
        self.matrix_instance = matrix_instance
        self.groups = self.matrix_instance.add_groups(groups, self)

    def __str__(self):
        return "[ MTX "+self.type.upper()+" <" + self.tag + "> ]"
