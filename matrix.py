from unders import Underscore
from lib.MatrixItem import MatrixItem

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
                self.items = [MatrixItem(item, self.object_from_json['items'][item], self) for item in self.object_from_json['items']]
            else:
                raise Exception("database version is outdated")
        else:
            raise Exception('"'+path+'" does not exist')

    # loads a database from a url by storing it as cache then loads that local file
    def load_from_url(self, url, refresh_cache=False):
        pass

    def search(self, query):
        return [item for item in self.items if item.type == "person" and item.name.username.lower().replace(".", " ").startswith(query.lower())]

    def add_groups(self, groups_array):
        pass
