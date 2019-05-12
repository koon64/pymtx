class MatrixAssignment:
    def __init__(self, name, category, score, total, description=None):
        self.name = name
        self.category = category
        self.description = description
        try:
            self.score = float(score)
            self.total = float(total)
            self.percent = self.score / self.total if self.total != 0 else 0
            self.valid_grade = True
        except:
            self.valid_grade = False
            self.score = None
            self.total = None
            self.percent = None

