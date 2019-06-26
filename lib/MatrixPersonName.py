from lib.MatrixName import MatrixName


class MatrixPersonName(MatrixName):
    def __init__(self, name_dict):

        # all the basic names
        self.given = name_dict['given']
        self.middle = name_dict['middle']
        self.surname = name_dict['surname']
        self.prefix = name_dict['prefix']
        self.suffix = name_dict['suffix']
        self.proffered_first = name_dict['proffered_first']
        self.nicknames = name_dict['nicknames']
        self.initials = name_dict['initials']
        self.username = name_dict['username']

        # inits the parent class
        super().__init__(self.full)

    def __str__(self):
        return self.full_formatted

    # displays the full name ex: "Johnathan William Smith"
    @property
    def full(self):
        return "{} {} {}".format(self.given, self.middle, self.surname)

    # displays the full name surname first: "Smith, Johnathan William"
    @property
    def full_formatted(self):
        return "{}, {} {}".format(self.surname, self.given, self.middle)

    # displays the first and last name
    @property
    def simple(self):
        return "{} {}".format(self.given, self.surname)

    # displays a friendly name with a proffered first name: "John Smith"
    # if the proffered_first is set to something different than the given
    @property
    def display(self):
        prefix = self.prefix + " " if str(self.prefix) != "None" else ""
        suffix = " " + self.suffix if str(self.suffix) != "None" else ""
        return "{}{} {}{}".format(prefix, self.proffered_first, self.surname, suffix)
