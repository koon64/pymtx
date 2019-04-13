from unders import Underscore
from lib.MatrixGroup import MatrixGroup
from lib.MatrixPerson import MatrixPerson
from lib.MatrixSchool import MatrixSchool

# Creates the underscore variable
# if you dont know what this is, go to: https://github.com/koon64/underscore
_ = Underscore()


class Matrix:
    def __init__(self):
        # defines all the variables
        self.db_set = False
        self.local = False
        self.path = None
        self.url = None
        self.object_from_json = None
        self.api_version = 1
        self.db_oldest_supported_version = 2
        self.db_created = None
        self.db_updated = None
        self.items = []
        self.groups = []

    # loads a database from a file
    def load_from_file(self, path):
        # makes sure the file exists
        if _.file_exists(path):
            self.db_set = True
            self.local = True
            self.path = path
            # loads the obj from the json file
            self.object_from_json = _.ja(path)
            # makes sure the version is not old
            if float(self.db_oldest_supported_version) <= float(self.object_from_json['info']['version']):
                # sets the created and updated vars
                self.db_created = _.time.parse_date(self.object_from_json['info']['created'])  # converts to date objs
                self.db_updated = _.time.parse_date(self.object_from_json['info']['updated'])  # converts to date objs
                self.items = []
                for tag in self.object_from_json['items']:
                    item = self.object_from_json['items'][tag]
                    item_type = item['type']
                    matrix_item = None
                    if item_type == "person":
                        matrix_item = MatrixPerson(tag, item, self)
                    elif item_type == "school":
                        matrix_item = MatrixSchool(tag, item, self)
                    if matrix_item is not None:
                        self.items.append(matrix_item)
                    else:
                        raise Exception('"' + item_type + '" is an invalid item type')
            else:
                raise Exception("database version is outdated")
        else:
            raise Exception('"'+path+'" does not exist')

    # loads a database from a url by storing it as cache then loads that local file
    def load_from_url(self, url, refresh_cache=False):
        pass

    # searches for an item from its username (very basic, will update later with a query system)
    def search(self, query):
        return [item for item in self.items
                if item.type == "person" and item.name.username.lower().replace(".", " ").startswith(query.lower())]

    # adds groups to an item and creates the group objs
    def add_groups(self, groups_array, item):
        added_groups = []
        for group in groups_array:
            group_match = self.get_group(group)
            if group_match is None:
                group_match = MatrixGroup(group)
                self.groups.append(group_match)
            group_match.add_item(item)
            added_groups.append(group_match)
        return added_groups

    # gets a group obj from its name
    def get_group(self, group_name):
        for group in self.groups:
            if group.name == group_name:
                return group
        return None
