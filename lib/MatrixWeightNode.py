from lib.MatrixPhysicalAttributeNode import MatrixPhysicalAttributeNode


class MatrixWeightNode(MatrixPhysicalAttributeNode):
    def __init__(self, kilograms, datetime):
        super().__init__(kilograms, datetime, self.to_pounds)

    def to_pounds(self, kilograms):
        return str(round(kilograms * 2.20462)) + "lbs"
