class MatrixPhysicalAttributeNode:
    def __init__(self, metric_amount, datetime, convert_function):
        self.amount = metric_amount
        self.datetime = datetime
        self.convert_function = convert_function

    def __str__(self):
        return self.customary_format

    @property
    def customary_format(self):
        return self.convert_function(self.amount)
