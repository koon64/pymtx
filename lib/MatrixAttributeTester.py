from lib.MatrixPerson import MatrixPerson


class MatrixAttributeTester:
    def __init__(self, matrix_instance):
        self.matrix_instance = matrix_instance

    def item_in_group(self, item, group):
        group = self.matrix_instance.get_group(group)
        return group in item.groups

    def age_value(self, item):
        if type(item) is MatrixPerson:
            return item.age

    def age_seconds_value(self, item):
        if type(item) is MatrixPerson:
            return item.age_seconds

    def type_value(self, item):
        return item.type

    def thing_type(self, item):
        if item.type == "thing":
            return item.thing_type

    def birthdate_val(self, item):
        if type(item) is MatrixPerson and item.has_birthdate:
            return item.birthdate.date_string

    def birthdate_val_month(self, item):
        if type(item) is MatrixPerson and item.has_birthdate:
            return int(item.birthdate.month)

    def birthdate_val_day(self, item):
        if type(item) is MatrixPerson and item.has_birthdate:
            return int(item.birthdate.day)

    def birthdate_val_year(self, item):
        if type(item) is MatrixPerson and item.has_birthdate:
            return int(item.birthdate.year)

    def birthdate_val_dow(self, item):
        if type(item) is MatrixPerson and item.has_birthdate:
            return item.birthdate.dow

    def name_value(self, item):
        if type(item) is MatrixPerson:
            return item.name.full

    def name_value_given(self, item):
        if type(item) is MatrixPerson:
            return item.name.given

    def name_value_middle(self, item):
        if type(item) is MatrixPerson:
            return item.name.middle

    def name_value_surname(self, item):
        if type(item) is MatrixPerson:
            return item.name.surname

