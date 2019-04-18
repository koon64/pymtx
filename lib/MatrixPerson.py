import logging
from lib.MatrixItem import MatrixItem
from lib.MatrixPhone import MatrixPhone
from lib.MatrixEmail import MatrixEmail
from lib.MatrixPersonName import MatrixPersonName
from lib.MatrixAddress import MatrixAddress
from lib.MatrixBirthdate import MatrixBirthdate
from lib.MatrixSchoolYear import MatrixSchoolYear
from lib.MatrixSchoolRotation import MatrixSchoolRotation
from lib.MatrixSchoolClass import MatrixSchoolClass, MatrixSchoolFree
from lib.MatrixSchoolSchedule import MatrixSchoolSchedule
from unders import Underscore

_ = Underscore()


# instance for each item in the db
class MatrixPerson(MatrixItem):
    def __init__(self, item_tag, item_dict, matrix_instance):
        # defines some meta data
        # inits the parent class
        super().__init__("person", item_tag, item_dict['meta']['groups'], matrix_instance)
        if self.type == "person":
            # sets the name object
            self.name = MatrixPersonName(item_dict['data']['name'])  # uses the MatrixName class
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
            address = item_dict['data']['address']['addresses']
            self.has_address = address
            if address:
                self.address = MatrixAddress(address['type'], address['lat'], address['lng'], address['full_address'],
                                             self.matrix_instance.debug)
            # sets the birthday
            self.has_birthdate = item_dict['data']['birthdate']['date'] is not None
            if self.has_birthdate:
                self.birthdate = MatrixBirthdate(item_dict['data']['birthdate']['date'],
                                                 item_dict['data']['birthdate']['dow'],
                                                 item_dict['data']['birthdate']['timestamp'],
                                                 item_dict['data']['birthdate']['birthdate_formated'],
                                                 item_dict['data']['birthdate']['birthdate_formated_year'],
                                                 item_dict['data']['birthdate']['zodiac'],
                                                 item_dict['data']['birthdate']['zodiac_emoji'])
            # sets the gender
            self.sex = item_dict['data']['sex']
            # education
            self.school_years = []
            self.student = False
            if item_dict['data']['education'] and "yog" in item_dict['data']['education']:
                if item_dict['data']['education']['yog'] != "":
                    self.yog = int(item_dict['data']['education']['yog'])
                    self.student = True
                    for school_type in item_dict['data']['education']:
                        if school_type != "yog":
                            school = item_dict['data']['education'][school_type]
                            if "yog" in school:
                                if "years" in school:
                                    for year in school['years']:
                                        year_dict = school['years'][year]
                                        year_obj = MatrixSchoolYear(year)
                                        if "quarters" in year_dict:
                                            q_num = 0
                                            for quarter_dict in year_dict["quarters"]:
                                                if type(quarter_dict) is dict:
                                                    if quarter_dict["honors_role"]:
                                                        year_obj.quarters[q_num].set_honors(True,
                                                                                            quarter_dict["high_honors"])
                                                q_num += 1
                                        if "semesters" in year_dict:
                                            s_num = 0
                                            for semester in year_dict["semesters"]:
                                                if "schedule" in semester:
                                                    schedule_obj = MatrixSchoolSchedule()
                                                    r_num = 0
                                                    for rotation in semester["schedule"]:
                                                        rotation_obj = MatrixSchoolRotation(r_num)
                                                        rotation_period = 0
                                                        if len(rotation) <= 7:
                                                            for class_dict in rotation:
                                                                period = self.period_match("{}{}".format(r_num,
                                                                                                         rotation_period))
                                                                if class_dict["name"] != "free":
                                                                    rotation_obj.add_class(MatrixSchoolClass(
                                                                        class_dict["name"],
                                                                        class_dict["teachers"],
                                                                        class_dict["room"],
                                                                        period))
                                                                else:
                                                                    rotation_obj.add_class(MatrixSchoolFree())
                                                                rotation_period += 1
                                                        else:
                                                            if matrix_instance.debug:
                                                                logging.error("Parsing " + _.format.possession(str(self.name)) + " schedule")
                                                        schedule_obj.add_rotation(rotation_obj)
                                                        r_num += 1
                                                    year_obj.semesters[s_num].set_schedule(schedule_obj)
                                                s_num += 1
                                        self.school_years.append(year_obj)
                else:
                    print(item_dict['data']['education']['yog'])

    def __str__(self):
        return "[ MTX PERSON <"+self.tag+"> " + str(self.name) + " ]"

    def get_phone(self, phone_type):
        return next(phone for phone in self.phones if phone.type == phone_type)

    def get_email(self, email_type):
        return next(email for email in self.emails if email.type == email_type)

    def period_match(self, rotation_period):
        period_match = {
            "00": 0,
            "01": 1,
            "02": 2,
            "03": 3,
            "04": 4,
            "05": 5,
            "06": 6,
            "10": 3,
            "11": 0,
            "12": 1,
            "13": 2,
            "14": 7,
            "15": 4,
            "16": 5,
            "20": 2,
            "21": 3,
            "22": 0,
            "23": 1,
            "24": 6,
            "25": 7,
            "26": 4,
            "30": 1,
            "31": 2,
            "32": 3,
            "33": 0,
            "34": 5,
            "35": 6,
            "36": 7,
            "40": 0,
            "41": 1,
            "42": 2,
            "43": 7,
            "44": 4,
            "45": 5,
            "46": 6,
            "50": 3,
            "51": 0,
            "52": 1,
            "53": 6,
            "54": 7,
            "55": 4,
            "56": 5,
            "60": 2,
            "61": 3,
            "62": 0,
            "63": 5,
            "64": 6,
            "65": 7,
            "66": 4,
            "70": 1,
            "71": 2,
            "72": 3,
            "73": 4,
            "74": 5,
            "75": 6,
            "76": 7
        }
        return period_match[rotation_period]

    # returns the age if the birthdate is set
    @property
    def age(self):
        if self.has_birthdate:
            try:
                return _.get_age(self.birthdate.date_string)
            except:
                return None

    @property
    def age_seconds(self):
        if self.has_birthdate:
            return self.birthdate.timestamp

    @property
    def zodiac(self):
        if self.has_birthdate:
            return self.birthdate.zodiac

    @property
    def zodiac_emoji(self):
        if self.has_birthdate:
            return self.birthdate.zodiac_emoji

    # gets the current grade
    @property
    def grade(self):
        if self.student:
            return _.get_grade(self.yog)
        if self.matrix_instance.debug:
            logging.warning(str(self) + " is not a student, therefore can not get the grade")

