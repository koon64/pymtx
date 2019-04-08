class MatrixGroup:
    def __init__(self, group_name):
        self.name = group_name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

