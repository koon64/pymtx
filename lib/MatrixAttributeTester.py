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

    # returns a student's yog
    def yog(self, item):
        if type(item) is MatrixPerson and item.student:
            return item.yog

    # returns the zodiac sign string
    def zodiac(self, item):
        if type(item) is MatrixPerson and item.has_birthdate:
            return item.zodiac

    # returns a person's sex
    def get_sex(self, item):
        if type(item) is MatrixPerson:
            return item.sex

    # returns a main phone number
    def main_phone(self, item):
        if type(item) is MatrixPerson and item.has_mobile:
            return str(item.mobile.number)

    # returns a phone number from its type
    def phone_number(self, item, phone_type):
        if type(item) is MatrixPerson:
            phone = item.get_phone(phone_type)
            if phone is not None:
                return str(phone.number)

    # returns all phone numbers in an array
    def get_phones(self, item):
        if type(item) is MatrixPerson:
            return [str(phone.number) for phone in item.phones]

    # returns the main email
    def main_email(self, item):
        if type(item) is MatrixPerson and item.has_email:
            return item.email

    # returns an email address from its type
    def email_address(self, item, email_type):
        if type(item) is MatrixPerson:
            email = item.get_email(email_type)
            if email is not None:
                return email.email

    # returns all emails
    def get_emails(self, item):
        if type(item) is MatrixPerson:
            return [email.email for email in item.emails]


