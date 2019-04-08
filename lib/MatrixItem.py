from lib.MatrixPhone import MatrixPhone
from lib.MatrixEmail import MatrixEmail
from lib.MatrixName import MatrixName
from lib.MatrixAddress import MatrixAddress
from lib.MatrixBirthdate import MatrixBirthdate
from unders import Underscore

_ = Underscore()


# instance for each item in the db
class MatrixItem:
    def __init__(self, item_tag, item_dict, matrix_instance):
        # defines some meta data
        self.tag = item_tag
        self.type = item_dict['meta']['type']
        self.groups = matrix_instance.add_groups(item_dict['meta']['groups'])
        if self.type == "person":
            # sets the name object
            self.name = MatrixName(item_dict['data']['name'])  # uses the MatrixName class
            # sets all the phone objs
            self.has_mobile = item_dict['data']['communication']['phone']['has_phone']
            # creates all the phone objects
            self.phones = [MatrixPhone(number, item_dict['data']['communication']['phone']['phones'][number]['type'],
                                       item_dict['data']['communication']['phone']['phones'][number]['label'],
                                       item_dict['data']['communication']['phone']['phones'][number]['carrier'],
                                       item_dict['data']['communication']['phone']['phones'][number]['location'])
                           for number in item_dict['data']['communication']['phone']['phones']]
            self.mobile = [phone for phone in self.phones if phone.type == "mobile"][0] if self.has_mobile else None
            # sets all the email objects
            self.has_email = item_dict['data']['communication']['email']['has_email']
            self.emails = [MatrixEmail(email, item_dict['data']['communication']['email']['emails'][email]['type'],
                                       item_dict['data']['communication']['email']['emails'][email]['label'],
                                       item_dict['data']['communication']['email']['emails'][email]['username'],
                                       item_dict['data']['communication']['email']['emails'][email]['domain'])
                           for email in item_dict['data']['communication']['email']['emails']]
            # sets the main email if there is one
            self.email = [email for email in self.emails if email.type == "personal"][0] if self.has_email else None
            # sets the address
            self.address = MatrixAddress()

            # birthday
            self.has_birthdate = item_dict['data']['birthdate']['date'] is not None
            if self.has_birthdate:
                self.birthdate = MatrixBirthdate(item_dict['data']['birthdate']['date'],
                                                 item_dict['data']['birthdate']['dow'],
                                                 item_dict['data']['birthdate']['timestamp'],
                                                 item_dict['data']['birthdate']['birthdate_formated'],
                                                 item_dict['data']['birthdate']['birthdate_formated_year'],
                                                 item_dict['data']['birthdate']['zodiac'],
                                                 item_dict['data']['birthdate']['zodiac_emoji'])

        if item_tag == "student.max_aderholtkoon":
            print(item_dict)

    def __str__(self):
        return "[ MTX ITEM <"+self.tag+"> " + str(self.name) + " ]"

    def get_phone(self, phone_type):
        return next(phone for phone in self.phones if phone.type == phone_type)

    def get_email(self, email_type):
        return next(email for email in self.emails if email.type == email_type)

    @property
    def age(self):
        if self.has_birthdate:
            return _.get_age(self.birthdate.date_string)
