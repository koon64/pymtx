class MatrixName:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    @property
    def full(self):
        return self.name

    @property
    def display(self):
        return self.name
