class MatrixSchoolQuarter:
    def __init__(self, quarter):
        self.quarter = quarter
        self.honors = None
        self.high_honors = None

    def __str__(self):
        return "Q{}".format(self.quarter + 1)
    
    def __int__(self):
        return self.quarter

    # sets honors role
    def set_honors(self, regular, high=False):
        self.honors = regular
        self.high_honors = high

    
