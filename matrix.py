from unders import Underscore
from lib.MatrixAttributeTester import MatrixAttributeTester
from lib.MatrixAttributeModifier import MatrixAttributeModifier
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
        self.classes = []
        self.class_names = []
        self.groups = []
        self.social_nodes = []
        self.debug = debug

        # for querying
        self.attribute_tester = MatrixAttributeTester(self)
        self.attribute_tree = {
            "age": {
                "function": self.attribute_tester.age_value,
                "valid_ops": [
                    "equals",
                    "not_equals",
                    "gtr",
                    "less",
                    "gtr_equ",
                    "less_equ"
                ],
                "type": "int",
                "parent": True,
                "sub_attributes": {
                    "seconds": {
                        "type": "int",
                        "function": self.attribute_tester.age_seconds_value,
                        "valid_ops": [
                            "equals",
                            "not_equals",
                            "gtr",
                            "less",
                            "gtr_equ",
                            "less_equ"
                        ]
                    }
                }
            },
            "birthdate": {
                "type": "string",
                "parent": True,
                "function": self.attribute_tester.birthdate_val,
                "valid_ops": [
                    "equals",
                    "not_equals"
                ],
                "sub_attributes": {
                    "dow": {
                        "type": "string",
                        "function": self.attribute_tester.birthdate_val_dow,
                        "valid_ops": [
                            "equals",
                            "not_equals"
                        ]
                    },
                    "day": {
                        "type": "int",
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
                    "month": {
                        "type": "int",
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
                    "year": {
                        "type": "int",
                        "function": self.attribute_tester.birthdate_val_year,
                        "valid_ops": [
                            "equals",
                            "not_equals",
                            "gtr",
                            "less",
                            "gtr_equ",
                            "less_equ"
                        ]
                    }
                }
            },
            "name": {
                "type": "string",
                "parent": True,
                "function": self.attribute_tester.name_value,
                "valid_ops": [
                    "equals",
                    "not_equals",
                    "starts_with",
                    "ends_with"
                ],
                "sub_attributes": {
                    "given": {
                        "type": "string",
                        "function": self.attribute_tester.name_value_given,
                        "valid_ops": [
                            "equals",
                            "not_equals",
                            "starts_with",
                            "ends_with"
                        ]
                    },
                    "middle": {
                        "type": "string",
                        "function": self.attribute_tester.name_value_middle,
                        "valid_ops": [
                            "equals",
                            "not_equals",
                            "starts_with",
                            "ends_with"
                        ]
                    },
                    "surname": {
                        "type": "string",
                        "function": self.attribute_tester.name_value_surname,
                        "valid_ops": [
                            "equals",
                            "not_equals",
                            "starts_with",
                            "ends_with"
                        ]
                    }
                }
            },
            "type": {
                "type": "string",
                "function": self.attribute_tester.type_value,
                "valid_ops": [
                    "equals",
                    "not_equals"
                ],
                "sub_attributes": {
                    "type": {  # this is thing type
                        "type": "string",
                        "function": self.attribute_tester.thing_type,
                        "valid_ops": [
                            "equals",
                            "not_equals"
                        ]
                    }
                }
            },
            "tag": {
                "type": "string",
                "function": self.attribute_tester.item_tag,
                "valid_ops": [
                    "equals",
                    "not_equals",
                    "starts_with",
                    "ends_with"
                ]
            },
            "address": {
                "type": "string",
                "parent": True,
                "function": self.attribute_tester.address_string,
                "valid_ops": [
                    "equals",
                    "not_equals",
                    "starts_with",
                    "ends_with"
                ],
                "sub_attributes": {
                    "country": {
                        "type": "string",
                        "function": self.attribute_tester.address_country,
                        "valid_ops": [
                            "equals",
                            "not_equals",
                            "starts_with",
                            "ends_with"
                        ]
                    },
                    "cid": {
                        "type": "string",
                        "function": self.attribute_tester.address_country_id,
                        "valid_ops": [
                            "equals",
                            "not_equals",
                            "starts_with",
                            "ends_with"
                        ]
                    },
                    "state": {
                        "type": "string",
                        "function": self.attribute_tester.address_state,
                        "valid_ops": [
                            "equals",
                            "not_equals",
                            "starts_with",
                            "ends_with"
                        ]
                    },
                    "sid": {
                        "type": "string",
                        "function": self.attribute_tester.address_state_id,
                        "valid_ops": [
                            "equals",
                            "not_equals",
                            "starts_with",
                            "ends_with"
                        ]
                    },
                    "locality": {
                        "type": "string",
                        "function": self.attribute_tester.address_locality,
                        "valid_ops": [
                            "equals",
                            "not_equals",
                            "starts_with",
                            "ends_with"
                        ]
                    },
                    "street": {
                        "type": "string",
                        "function": self.attribute_tester.address_street,
                        "valid_ops": [
                            "equals",
                            "not_equals",
                            "starts_with",
                            "ends_with"
                        ]
                    },
                    "number": {
                        "type": "int",
                        "function": self.attribute_tester.address_number,
                        "valid_ops": [
                            "equals",
                            "not_equals",
                            "starts_with",
                            "ends_with"
                        ]
                    },
                    "format": {
                        "type": "container",
                        "parent": True,
                        "sub_attributes": {
                            "street": {
                                "type": "string",
                                "function": self.attribute_tester.address_street_format
                            }
                        }
                    }
                }
            },
            "grade": {
                "type": "int",
                "function": self.attribute_tester.grade_value,
                "valid_ops": [
                    "equals",
                    "not_equals",
                    "gtr",
                    "less",
                    "gtr_equ",
                    "less_equ"
                ]
            },
            "yog": {
                "type": "int",
                "function": self.attribute_tester.yog,
                "valid_ops": [
                    "equals",
                    "not_equals",
                    "gtr",
                    "less",
                    "gtr_equ",
                    "less_equ"
                ]
            },
            "zodiac": {
                "type": "string",
                "function": self.attribute_tester.zodiac,
                "valid_ops": [
                    "equals",
                    "not_equals"
                ]
            },
            "sex": {
                "type": "string",
                "function": self.attribute_tester.get_sex,
                "valid_ops": [
                    "equals",
                    "not_equals"
                ]
            },
            "phone": {
                "type": "string",
                "function": self.attribute_tester.main_phone,
                "valid_ops": [
                    "equals",
                    "not_equals",
                    "starts_with",
                    "ends_with"
                ],
                "sub_main_function": self.attribute_tester.phone_number
            },
            "phones": {
                "type": "array",
                "function": self.attribute_tester.get_phones,
                "valid_ops": [
                    "in",
                    "not_in"
                ]
            },
            "email": {
                "type": "string",
                "function": self.attribute_tester.main_email,
                "valid_ops": [
                    "equals",
                    "not_equals",
                    "starts_with",
                    "ends_with"
                ],
                "sub_main_function": self.attribute_tester.email_address
            },
            "emails": {
                "type": "array",
                "function": self.attribute_tester.get_emails,
                "valid_ops": [
                    "in",
                    "not_in"
                ]
            },
            "teachers": {
                "type": "array",
                "function": self.attribute_tester.get_teachers,
                "valid_ops": [
                    "in",
                    "not_in"
                ]
            },
            "classes": {
                "type": "array",
                "function": self.attribute_tester.get_classes,
                "valid_ops": [
                    "in",
                    "not_in"
                ],
                "sub_main_function": self.attribute_tester.get_class_from_subject
            }
        }
        self.attribute_modifier = MatrixAttributeModifier()
        self.attribute_modifiers = {
            "words": {
                "valid_types": [
                    "string"
                ],
                "valid_ops": [
                    "in",
                    "not_in"
                ],
                "function": self.attribute_modifier.words
            },
            "lower": {
                "valid_types": [
                    "string",
                    "array"
                ],
                "valid_ops": [
                    "equals",
                    "not_equals",
                    "starts_with",
                    "ends_with",
                    "in",
                    "not_in"
                ],
                "function": self.attribute_modifier.lower
            },
            "upper": {
                "valid_types": [
                    "string",
                    "array"
                ],
                "valid_ops": [
                    "equals",
                    "not_equals",
                    "starts_with",
                    "ends_with",
                    "in",
                    "not_in"
                ],
                "function": self.attribute_modifier.upper
            },
            "len": {
                "valid_types": [
                    "array",
                    "string"
                ],
                "valid_ops": [
                    "equals",
                    "not_equals",
                    "gtr",
                    "less",
                    "gtr_equ",
                    "less_equ"
                ],
                "function": self.attribute_modifier.count
            }
        }

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
                # connects all the the items together after they are created
                for node in self.social_nodes:
                    if node.social_network == "instagram":
                        post = self.get_ig_post_from_url(node.image_url)
                        if post is not None:
                            if node.node_type == "comment":
                                node.connect_post(post)
                            elif node.node_type == "tag":
                                node.connect_post(post)
                            elif node.node_type == "like":
                                node.connect_post(post)
                    print(node)


            else:
                raise Exception("database version is outdated")
        else:
            raise Exception('"'+path+'" does not exist')

    # returns an instagram post from its image url
    def get_ig_post_from_url(self, image_url):
        for node in self.social_nodes:
            if node.social_network == "instagram" and node.node_type == "post":
                if node.image_url == image_url:
                    return node

    # loads a database from a url by storing it as cache then loads that local file
    def load_from_url(self, url, refresh_cache=False):
        pass

    # searches from a persons full name
    def simple_search(self, name):
        return self.select_items_from_query_array({
            "conditions": [
                {
                    "attribute": "name.lower",
                    "operator": "starts_with",
                    "value": name
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

    # gets a class from its name
    def get_class(self, period, room):
        for class_obj in self.classes:
            if class_obj.period == period and class_obj.room == room:
                return class_obj

    # queries items from a string similar to SQL
    def query(self, query_string):
        query_array = self.parse_query_string(query_string)
        items = self.select_items_from_query_array(query_array)
        return items

    # converts a sql like string to a query_array
    def parse_query_string(self, query_string):
        # return query_string
        limit = query_string.split(' limit ')
        query = limit[0]
        order = query.split(' order ')
        query = order[0]
        words = query.split()
        query_array = {
            "command": "",
            "conditions": []
        }
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
        groups = ''

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
            # TODO: make the other commands
            pass
            groups = after_command.split('set')
            if len(groups) != 1:
                groups = groups[0].strip()
                set_string = query.split('set')
                if len(set_string) > 1:
                    pass

        if groups == "*":
            selector_array['type']['all'] = True
        else:
            select_parts = groups.split(",")
            for select_part in select_parts:
                if select_part[0] != "-":
                    if select_part != "*":
                        selector_array['type']['positive'].append(select_part)
                    else:
                        selector_array['type']['all'] = True
                        selector_array['type']['all_with_exeptions'] = True
                else:
                    selector_array['type']['negative'].append(select_part.replace('-', ''))
        conditions = query.split('where')
        conditions_array = []
        if len(conditions) != 1:
            conditions = conditions[1].strip().split('and')
            i = 0
            for condition in conditions:
                condition_equals = condition.split('==')
                condition_not_equals = condition.split('!=')
                condition_starts_with = condition.split(':=')
                condition_ends_with = condition.split('=:')
                condition_in = condition.split('<-')
                condition_not_in = condition.split('->')
                condition_gtr_eq = condition.split('>=')
                condition_less_eq = condition.split('<=')
                condition_gtr = condition.split('>')
                condition_less = condition.split('<')
                if len(condition_equals) != 1:
                    conditions_array.append({
                        "attribute": condition_equals[0].strip(),
                        "operator": 'equals',
                        "value": condition_equals[1].strip()
                    })
                elif len(condition_not_equals) != 1:
                    conditions_array.append({
                        "attribute": condition_not_equals[0].strip(),
                        "operator": 'not_equals',
                        "value": condition_not_equals[1].strip()
                    })
                elif len(condition_starts_with) != 1:
                    conditions_array.append({
                        "attribute": condition_starts_with[0].strip(),
                        "operator": 'starts_with',
                        "value": condition_starts_with[1].strip()
                    })
                elif len(condition_ends_with) != 1:
                    conditions_array.append({
                        "attribute": condition_ends_with[0].strip(),
                        "operator": 'ends_with',
                        "value": condition_ends_with[1].strip()
                    })
                elif len(condition_gtr_eq) != 1:
                    conditions_array.append({
                        "attribute": condition_gtr_eq[0].strip(),
                        "operator": 'gtr_equ',
                        "value": condition_gtr_eq[1].strip()
                    })
                elif len(condition_in) != 1:
                    conditions_array.append({
                        "attribute": condition_in[0].strip(),
                        "operator": 'in',
                        "value": condition_in[1].strip()
                    })
                elif len(condition_not_in) != 1:
                    conditions_array.append({
                        "attribute": condition_not_in[0].strip(),
                        "operator": "not_in",
                        "value": condition_not_in[1].strip()
                    })
                elif len(condition_less_eq) != 1:
                    conditions_array.append({
                        "attribute": condition_less_eq[0].strip(),
                        "operator": 'less_equ',
                        "value": condition_less_eq[1].strip()
                    })
                elif len(condition_gtr) != 1:
                    conditions_array.append({
                        "attribute": condition_gtr[0].strip(),
                        "operator": 'gtr',
                        "value": condition_gtr[1].strip()
                    })
                elif len(condition_less) != 1:
                    conditions_array.append({
                        "attribute": condition_less[0].strip(),
                        "operator": 'less',
                        "value": condition_less[1].strip()
                    })
                else:
                    if condition[0] != '!':
                        conditions_array.append({
                            "attribute": condition_equals[0].strip(),
                            "operator": 'equals',
                            "value": 'true'
                        })
                    else:
                        conditions_array.append({
                            "attribute": condition_equals[0].strip(),
                            "operator": 'equals',
                            "value": 'false'
                        })
                recent_condition = conditions_array[i]
                recent_condition['case_sensitive'] = recent_condition['attribute'][-1] != '*'
                recent_condition['attribute'] = recent_condition['attribute'][:-1] \
                    if not recent_condition['case_sensitive'] else recent_condition['attribute']
                conditions_array[i] = recent_condition
                i += 1
        else:
            pass
        query_array['conditions'] = conditions_array
        return query_array

    # returns items that match all the query conditions
    def select_items_from_query_array(self, query_array):
        conditions = query_array['conditions']
        return [item for item in self.items if self.valid_item_from_conditions(item, conditions)]

    # tests if all conditions match
    def valid_item_from_conditions(self, item, conditions):
        valid_item = True
        for condition in conditions:
            test_result = self.valid_item_from_condition(item, condition)
            if not test_result:
                valid_item = False
        return valid_item

    # tests if a value can be a type of var
    def valid_value_from_type(self, value, test_type):
        if test_type == "int":
            try:
                int(value)
                return True
            except:
                return False
        elif test_type == "string" or test_type == "array":
            return True
        else:
            raise Exception(test_type + " is an invalid type")

    def valid_item_from_condition(self, item, condition):
        value = condition['attribute']
        value_parts = value.split('.')

        # gets all the modifiers and puts them into an array then removes them from the value_parts var
        modifiers = []
        new_value_parts = []
        for value_part in value_parts:
            if value_part not in self.attribute_modifiers:
                new_value_parts.append(value_part)
            else:
                modifiers.append(value_part)
        value_parts = new_value_parts

        current_tree = self.attribute_tree
        part_count = 0
        for value_part in value_parts:
            if value_part in current_tree or value_part in self.attribute_modifiers:
                if "parent" in current_tree[value_part] and len(value_parts) > part_count + 1:
                    current_tree = current_tree[value_part]['sub_attributes']
                else:
                    attribute = current_tree[value_part]

                    for modifier in modifiers:
                        current_type = attribute['type']
                        modifier_info = self.attribute_modifiers[modifier]
                        if current_type in modifier_info['valid_types']:
                            attribute['valid_ops'] = modifier_info['valid_ops']
                        else:
                            raise Exception(current_type + ' is not a supported input for the ' + modifier + ' modifier')

                    if condition['operator'] in attribute['valid_ops']:
                        if self.valid_value_from_type(condition['value'], attribute['type']):
                            case_sensitive = "case_sensitive" not in condition or condition['case_sensitive']
                            if not case_sensitive:
                                condition['value'] = condition['value'].lower()

                            # gets the returned value from the functions
                            if "sub_main_function" in attribute and len(value_parts) > part_count + 1:
                                function_return_value = attribute['sub_main_function'](item, value_parts[part_count + 1])
                            else:
                                function_return_value = attribute['function'](item)

                            for modifier in modifiers:
                                modifier_function = self.attribute_modifiers[modifier]['function']
                                function_return_value = modifier_function(function_return_value)

                            operator = condition['operator']
                            if operator == "in":
                                return function_return_value is not None and condition['value'] in function_return_value
                            elif operator == "not_in":
                                return function_return_value is None or condition['value'] not in function_return_value
                            elif operator == "equals":
                                return function_return_value is not None and self.lower_if_false(
                                    function_return_value, case_sensitive) == condition['value']
                            elif operator == "not_equals":
                                return self.lower_if_false(function_return_value, case_sensitive) != condition['value']
                            elif operator == "gtr":
                                return function_return_value is not None and function_return_value > \
                                       int(condition['value'])
                            elif operator == "less":
                                return function_return_value is not None and function_return_value < \
                                       int(condition['value'])
                            elif operator == "gtr_equ":
                                return function_return_value is not None and function_return_value >= \
                                       int(condition['value'])
                            elif operator == "less_equ":
                                return function_return_value is not None and function_return_value <= \
                                       int(condition['value'])
                            elif operator == "starts_with":
                                return function_return_value is not None and self.lower_if_false(
                                    str(function_return_value), case_sensitive).startswith(condition['value'])
                            elif operator == "ends_with":
                                return function_return_value is not None and self.lower_if_false(
                                    str(function_return_value), case_sensitive).endswith(condition['value'])
                        raise Exception("INVALID DATATYPE " + condition['value'] + " can not be a " + attribute['type'])
                    raise Exception(condition['operator'] + " is an invalid operator for " + condition['attribute'])
            else:
                raise Exception(value_part + ' is an invalid attribute')
            part_count += 1

    def lower_if_false(self, text, lower):
        text = str(text)
        return text.lower() if not lower else text

