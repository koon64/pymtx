from unders import Underscore
from lib.MatrixAttributeTester import MatrixAttributeTester
from lib.MatrixGroup import MatrixGroup
from lib.MatrixPerson import MatrixPerson
from lib.MatrixSchool import MatrixSchool

# Creates the underscore variable
# if you dont know what this is, go to: https://github.com/koon64/underscore
_ = Underscore()


class Matrix:
    def __init__(self, debug=False):
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
        self.debug = debug

        # for querying
        self.attribute_tester = MatrixAttributeTester(self)

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
                    item_type = item['meta']['type']
                    matrix_item = None
                    if item_type == "person":
                        matrix_item = MatrixPerson(tag, item, self)
                    elif item_type == "thing":
                        if item['meta']['thing_type'] == "school":
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

    # searches from a persons full name
    def simple_search(self, name):
        return self.select_items_from_query_array({
            "selectors": [
                {
                    "attribute": "name",
                    "operator": "starts_with",
                    "value": name,
                    "case_sensitive": False
                }
            ]
        })

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

    # queries items from a string similar to SQL
    def query(self, query_string):
        query_array = self.parse_query_string(query_string)
        items = self.select_items_from_query_array(query_array)
        return items

    def parse_query_string(self, query_string):
        return query_string
        attribute_tree = {
            "age": {
                "type": "int",
                "sub_attributes": {
                    "seconds": {
                        "type": "int"
                    }
                }
            }
        }
        limit = query_string.split(' limit ')
        query = limit[0]
        order = query.split(' order ')
        query = order[0]
        words = query.split()
        query_array = {}
        after_command = query.split(words[0])[1]
        words[0] = words[0].lower()
        if words[0] == "select":
            query_array['command'] = "select"
        elif words[0] == "update":
            query_array['command'] = "update"
        elif words[0] == "insert":
            query_array['command'] = "insert"
        else:
            raise Exception(words[0] + " is an invalid command")
        selector_array = {
            'all': False,
            'all_with_exceptions': False,
            'positive': [],
            'negative': [],
            'type': {
                'all': False,
                'all_with_exceptions': False,
                'positive': [],
                'negative': [],
            }
        }

        if query_array['command'] == 'select':
            selector = after_command.split("from")[0].strip()
            if selector == '*':
                selector_array['all'] = True
            else:
                select_parts = selector.split(',')
                for select_part in select_parts:
                    if select_part[0] != '-':
                        if select_part != '*':
                            selector_array['positive'].append(select_part)
                        else:
                            selector_array['all'] = True
                            selector_array['all_with_exceptions'] = True
                    else:
                        selector_array['negative'].append(select_part.replace("-", ""))
            groups = query.split("from")[1]
            groups = groups.split("where")[0].strip()
        elif query_array['command'] == 'update':
            pass
            # groups = after_command.split('set')
            # if len(groups) != 1:
            #     groups = groups[0].strip()
            #     set_string = query.split('set')
            #     if len(set_string) > 1:
            #         pass


        return query_array

    def select_items_from_query_array(self, query_array):
        selectors = query_array['selectors']
        return [item for item in self.items if self.valid_item_from_selectors(item, selectors)]

    def valid_item_from_selectors(self, item, selectors):
        valid_item = True
        for selector in selectors:
            test_result = self.valid_item_from_selector(item, selector)
            if not test_result:
                valid_item = False
        return valid_item

    def valid_item_from_selector(self, item, selector):
        attributes = {
            "groups": {
                "function": self.attribute_tester.item_in_group,
                "valid_ops": [
                    "in",
                    "not_in"
                ]
            },
            "age": {
                "function": self.attribute_tester.age_value,
                "valid_ops": [
                    "equals",
                    "not_equals",
                    "gtr",
                    "less",
                    "gtr_equ",
                    "less_equ"
                ]
            },
            "age_seconds": {
                "function": self.attribute_tester.age_seconds_value,
                "valid_ops": [
                    "equals",
                    "not_equals",
                    "gtr",
                    "less",
                    "gtr_equ",
                    "less_equ"
                ]
            },
            "type": {
                "function": self.attribute_tester.type_value,
                "valid_ops": [
                    "equals",
                    "not_equals"
                ]
            },
            "thing_type": {
                "function": self.attribute_tester.thing_type,
                "valid_ops": [
                    "equals",
                    "not_equals"
                ]
            },
            "birthdate": {
                "function": self.attribute_tester.birthdate_val,
                "valid_ops": [
                    "equals",
                    "not_equals"
                ]
            },
            "birthdate_year": {
                "function": self.attribute_tester.birthdate_val_year,
                "valid_ops": [
                    "equals",
                    "not_equals",
                    "gtr",
                    "less",
                    "gtr_equ",
                    "less_equ"
                ]
            },
            "birthdate_month": {
                "function": self.attribute_tester.birthdate_val_month,
                "valid_ops": [
                    "equals",
                    "not_equals",
                    "gtr",
                    "less",
                    "gtr_equ",
                    "less_equ"
                ]
            },
            "birthdate_day": {
                "function": self.attribute_tester.birthdate_val_day,
                "valid_ops": [
                    "equals",
                    "not_equals",
                    "gtr",
                    "less",
                    "gtr_equ",
                    "less_equ"
                ]
            },
            "birthdate_dow": {
                "function": self.attribute_tester.birthdate_val_dow,
                "valid_ops": [
                    "equals"
                    "not_equals"
                ]
            },
            "name": {
                "function": self.attribute_tester.name_value,
                "valid_ops": [
                    "equals",
                    "not_equals",
                    "starts_with",
                    "ends_with"
                ]
            },
            "name_given": {
                "function": self.attribute_tester.name_value_given,
                "valid_ops": [
                    "equals",
                    "not_equals",
                    "starts_with",
                    "ends_with"
                ]
            },
            "name_middle": {
                "function": self.attribute_tester.name_value_middle,
                "valid_ops": [
                    "equals",
                    "not_equals",
                    "starts_with",
                    "ends_with"
                ]
            },
            "name_surname": {
                "function": self.attribute_tester.name_value_surname,
                "valid_ops": [
                    "equals",
                    "not_equals",
                    "starts_with",
                    "ends_with"
                ]
            }
        }
        if selector['attribute'] in attributes:
            attribute = attributes[selector['attribute']]
            if selector['operator'] in attribute['valid_ops']:
                case_sensitive = "case_sensitive" not in selector or selector['case_sensitive']
                if not case_sensitive:
                    selector['value'] = selector['value'].lower()
                operator = selector['operator']
                if operator == "in":
                    return attribute['function'](item, selector['value'])
                elif operator == "not_in":
                    return not attribute['function'](item, selector['value'])
                elif operator == "equals":
                    return attribute['function'](item) is not None and self.lower_if_true(attribute['function'](item), case_sensitive) == selector['value']
                elif operator == "not_equals":
                    return self.lower_if_true(attribute['function'](item), case_sensitive) != selector['value']
                elif operator == "gtr":
                    return attribute['function'](item) is not None and attribute['function'](item) > selector['value']
                elif operator == "less":
                    return attribute['function'](item) is not None and attribute['function'](item) < selector['value']
                elif operator == "gtr_equ":
                    return attribute['function'](item) is not None and attribute['function'](item) >= selector['value']
                elif operator == "less_equ":
                    return attribute['function'](item) is not None and attribute['function'](item) <= selector['value']
                elif operator == "starts_with":
                    return attribute['function'](item) is not None and self.lower_if_true(str(attribute['function'](item)), case_sensitive).startswith(selector['value'])
                elif operator == "ends_with":
                    return attribute['function'](item) is not None and self.lower_if_true(str(attribute['function'](item)), case_sensitive).endswith(selector['value'])
            raise Exception(selector['operator'] + " is an invalid operator")
        raise Exception(selector['attribute'] + " is an invalid attribute")

    def lower_if_true(self, text, lower):
        return text.lower() if lower else text

