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

    def item_tag(self, item):
        return item.tag

    # returns the full address string
    def address_string(self, item):
        if type(item) is MatrixPerson and item.has_address:
            return str(item.address)

    # returns the address country
    def address_country(self, item):
        if type(item) is MatrixPerson and item.has_address:
            return item.address.country

    # returns the address country_id
    def address_country_id(self, item):
        if type(item) is MatrixPerson and item.has_address:
            return item.address.cid

    # returns the address state
    def address_state(self, item):
        if type(item) is MatrixPerson and item.has_address:
            return item.address.state

    # returns the address state_id
    def address_state_id(self, item):
        if type(item) is MatrixPerson and item.has_address:
            return item.address.sid

    # returns the address locality
    def address_locality(self, item):
        if type(item) is MatrixPerson and item.has_address:
            return item.address.locality

    # returns the address street
    def address_street(self, item):
        if type(item) is MatrixPerson and item.has_address:
            return item.address.street_name

    # returns the address number
    def address_number(self, item):
        if type(item) is MatrixPerson and item.has_address:
            return item.address.number

    # returns the address street_format
    def address_street_format(self, item):
        if type(item) is MatrixPerson and item.has_address:
            return item.address.street_format

    # returns a student's grade level
    def grade_value(self, item):
        if type(item) is MatrixPerson and item.student:
            return item.grade

