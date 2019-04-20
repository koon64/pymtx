from lib.MatrixItem import MatrixItem
from lib.MatrixAddress import MatrixAddress
from lib.MatrixName import MatrixName


class MatrixSchool(MatrixItem):
    def __init__(self, tag, item, matrix_instance):
        # defines some meta data
        # inits the parent class
        super().__init__("thing", tag, item['meta']['groups'], matrix_instance, "school")
        # creates the name obj
        self.name = MatrixName(item['data']['label'])
        # school information
        self.logo = item['data']['icon']
        self.school_type = item['data']['school_information']['type']
        self.school_grades = item['data']['school_information']['grades']
        # creates the address obj
        location = item['data']['location']
        self.address = MatrixAddress("location", location['lat'], location['lng'], location['full_address'])

    def __str__(self):
        return "[ MTX SCHOOL <" + self.tag + "> " + str(self.name) + " ]"

