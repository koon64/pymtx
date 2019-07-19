from lib.MatrixPhysicalAttributeNode import MatrixPhysicalAttributeNode
from unders import Underscore

_ = Underscore()


class MatrixHeightNode(MatrixPhysicalAttributeNode):
    def __init__(self, centimeters, datetime):
        super().__init__(centimeters, datetime, self.format_cm)

    def format_cm(self, centimeters):
        return _.convert.centimeters_to_feet_and_inches(centimeters)

