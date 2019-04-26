import logging
from lib.MatrixItem import MatrixItem
from lib.MatrixPhone import MatrixPhone
from lib.MatrixEmail import MatrixEmail
from lib.MatrixAddress import MatrixAddress
from lib.MatrixBirthdate import MatrixBirthdate
from lib.MatrixSchoolYear import MatrixSchoolYear
from lib.MatrixPersonName import MatrixPersonName
from lib.MatrixRelationship import MatrixRelationship
from lib.MatrixInstagramTag import MatrixInstagramTag
from lib.MatrixYoutubeVideo import MatrixYoutubeVideo
from lib.MatrixInstagramPost import MatrixInstagramPost
from lib.MatrixInstagramLike import MatrixInstagramLike
from lib.MatrixSchoolRotation import MatrixSchoolRotation
from lib.MatrixSchoolSchedule import MatrixSchoolSchedule
from lib.MatrixYoutubeAccount import MatrixYoutubeAccount
from lib.MatrixInstagramComment import MatrixInstagramComment
from lib.MatrixInstagramAccount import MatrixInstagramAccount
from lib.MatrixSchoolClass import MatrixSchoolClass, MatrixSchoolFree
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
            # sets up all the education objs
            self.school_years = []
            self.student = False
            self.math_level = None
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
                                                                    # attempts to get the obj from the main class
                                                                    class_obj = matrix_instance.get_class(period, class_dict['room'])
                                                                    if class_obj is None:
                                                                        # creates the class
                                                                        class_obj = MatrixSchoolClass(
                                                                            class_dict["name"],
                                                                            class_dict["teachers"],
                                                                            class_dict["room"],
                                                                            period)
                                                                        # adds it to the main class
                                                                        matrix_instance.classes.append(class_obj)
                                                                    # adds the student to the class object
                                                                    class_obj.add_student(self)
                                                                    # adds the class to the rotation class
                                                                    rotation_obj.add_class(class_obj)
                                                                    # sets the highest math level if set in the class
                                                                    if class_obj.math_level is not None:
                                                                        if self.math_level is None or class_obj.math_level > self.math_level:
                                                                            self.math_level = class_obj.math_level
                                                                else:
                                                                    rotation_obj.add_class(MatrixSchoolFree(period))
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
                    if matrix_instance.debug:
                        logging.error("something went wrong with" + str(self))
            # sets up social media accounts
            self.social_media_accounts = []
            # tests if there is the social_media in the item_dict
            if "social_media" in item_dict['data']['communication']:
                social_media_dict = item_dict['data']['communication']['social_media']
                # loops through each social media account a person has
                for social_media_type in social_media_dict:
                    social_media_account = social_media_dict[social_media_type]
                    cached = {
                        "name": None,
                        "profile_image": None,
                        "biography": None,
                        "private": None,
                        "followers": None,
                        "following": None
                    }
                    for i in social_media_account['cached']:
                        cached[i] = social_media_account['cached'][i]
                    if social_media_type == "instagram":
                        # sets up the instagram obj
                        self.social_media_accounts.append(MatrixInstagramAccount(social_media_account['user_id'],
                                                                                 cached['name'],
                                                                                 cached['profile_image'],
                                                                                 cached['biography'],
                                                                                 cached['username'],
                                                                                 cached['private'],
                                                                                 cached['followers'],
                                                                                 cached['following']))
                    elif social_media_type == "youtube":
                        # sets up the youtube obj
                        self.social_media_accounts.append(MatrixYoutubeAccount(social_media_account['user_id'],
                                                                               cached['name'],
                                                                               cached['profile_image']['url'],
                                                                               cached['description'],
                                                                               cached['subscribers'],
                                                                               cached['views'],
                                                                               cached['video_count']))
            self.social_history = []
            if "social_history" in item_dict['data']:
                social_history = item_dict['data']['social_history']
                for node_time in social_history:
                    node = social_history[node_time]
                    datetime = node_time
                    social_media_node = None
                    if node['from'] == "instagram":
                        if node['type'] == 'post':
                            social_media_node = MatrixInstagramPost(self, datetime, node['image_url'],
                                                                    node['caption'], node['like_count'],
                                                                    node['comment_count'])
                        elif node['type'] == 'comment':
                            if "post" in node:
                                social_media_node = MatrixInstagramComment(self, datetime, node['comment'],
                                                                           node['post']['image_url'])
                        elif node['type'] == 'tag':
                            if "post" in node:
                                social_media_node = MatrixInstagramTag(self, datetime, node['post']['image_url'])
                        elif node['type'] == 'like':
                            if "post" in node:
                                social_media_node = MatrixInstagramLike(self, datetime, node['post']['image_url'])
                    elif node['from'] == 'youtube':
                        if node['type'] == 'video':
                            video_id = _.between(node['thumbnail'], 'https://i.ytimg.com/vi/', '/mqdefault.jpg')
                            social_media_node = MatrixYoutubeVideo(self, datetime, video_id, node['title'],
                                                                   node['thumbnail'])
                    if social_media_node is not None:
                        self.social_history.append(social_media_node)
            # adds all the relationships
            self.relationships = []
            if "relationships" in item_dict['data']:
                relationships = item_dict['data']['relationships']
                for tag in relationships:
                    relationship = relationships[tag]
                    tag = tag.replace("people.", "person.")
                    if type(relationship) is not str:
                        relationship = relationship['type']
                    relationship_obj = MatrixRelationship(self, tag, relationship)
                    self.relationships.append(relationship_obj)

    def __str__(self):
        return "[ MTX PERSON <"+self.tag+"> " + str(self.name) + " ]"

    def get_phone(self, phone_type):
        for phone in self.phones:
            if phone.type == phone_type:
                return phone

    def get_email(self, email_type):
        for email in self.emails:
            if email.type == email_type:
                return email

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

    # returns a class from its subject
    def get_class_from_subject(self, subject):
        return [class_obj for class_obj in self.classes if class_obj.subject == subject]

    # returns social media accounts from a network
    def get_social_media_account(self, social_network):
        return [account for account in self.social_media_accounts if account.account_type == social_network]

    # returns all nodes from its node_type
    def social_history_from_type(self, node_type):
        return [node for node in self.social_history if node.node_type == node_type]

    # returns all the classes a student has
    @property
    def classes(self):
        if self.student:
            school_year = self.current_school_year
            if school_year is not None:
                if school_year.semesters[1].schedule is not None:
                    schedule = school_year.semesters[1].schedule
                elif school_year.semesters[0].schedule is not None:
                    schedule = school_year.semesters[0].schedule
                else:
                    return []
                classes = []
                class_names = []
                for rotation in schedule.rotations:
                    for class_obj in rotation.classes:
                        if not class_obj.is_free and class_obj.name not in class_names:
                            classes.append(class_obj)
                            class_names.append(class_obj.name)
                return classes
        return []

    # returns all the teachers a student has
    @property
    def teachers(self):
        if self.student:
            return [class_obj.teacher for class_obj in self.classes]
        return []

    # returns the current school year obj
    @property
    def current_school_year(self):
        now = _.time.now()
        month = now.month
        year = now.year
        for year_obj in self.school_years:
            year_parts = year_obj.year.split('-')
            beginning_year = int(year_parts[0])
            if 8 <= month:
                # beginning of year
                if beginning_year == year:
                    return year_obj
            else:
                if beginning_year + 1 == year:
                    return year_obj

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

    # returns first ig account that is in the social media accounts array
    @property
    def instagram(self):
        accounts = self.get_social_media_account("instagram")
        if len(accounts) > 0:
            return accounts[0]

    # returns first yt account that is in the social media accounts array
    @property
    def youtube(self):
        accounts = self.get_social_media_account("youtube")
        if len(accounts) > 0:
            return accounts[0]

    # returns all comment nodes from social_history
    @property
    def social_history_comments(self):
        return self.social_history_from_type("comment")

    # returns all post nodes from social_history
    @property
    def social_history_posts(self):
        return self.social_history_from_type("posts")

    # returns all like nodes from social_history
    @property
    def social_history_likes(self):
        return self.social_history_from_type("like")

    # returns all like nodes from social_history
    @property
    def social_history_tags(self):
        return self.social_history_from_type("tag")

    # returns a string of the math level
    @property
    def math_level_string(self):
        return "M{}".format(str(self.math_level + 1)) \
            if self.math_level != 0 else "S1" \
            if self.math_level is not None else ""
