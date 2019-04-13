from lib.MatrixItem import MatrixItem
from lib.MatrixAddress import MatrixAddress
from lib.MatrixName import MatrixName


class MatrixSchool(MatrixItem):
    def __init__(self, tag, item, matrix_instance):
        # defines some meta data
        # inits the parent class
        super().__init__("school", tag, item['meta']['groups'], matrix_instance)

    def __str__(self):
        return self.tag

