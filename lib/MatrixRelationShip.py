relationships = {
    "siblings": {
        "brother": "Brother",
        "sister": "Sister"
    },
    "parents": {
        "father": "Father",
        "mother": "Mother"
    },
    "step_parents": {
        "step_father": "Step-Father",
        "step_mother": "Step-Mother"
    },
    "children": {
        "son": "Son",
        "daughter": "Daughter"
    },
    "step_children": {
        "step_son": "Step-Son",
        "step_daughter": "Step-Daughter"
    },
    "spouse": {
        "husband": "Husband",
        "wife": "Wife"
    },
    "ex_spouse": {
        "ex_husband": "Ex-Husband",
        "ex_wife": "Ex-Wife"
    }
}


def get_relationship_group(relationship):
    for relationship_group_name in relationships:
        relationship_group = relationships[relationship_group_name]
        if relationship in relationship_group.keys():
            return relationship_group_name


class MatrixRelationship:
    def __init__(self, item1, item2, relationship):
        if get_relationship_group(relationship) is not None:
            self.item1 = item1
            self.item2 = item2
            self.item2_is_person = False
            self.relationship = relationship
            self.relationship_group = get_relationship_group(relationship)
            self.relationship_string = relationships[self.relationship_group][relationship]
        else:
            raise Exception('"{}" is an invalid relationship'.format(relationship))

    def __str__(self):
        item1 = self.item1.tag
        if self.item2_is_person:
            item2 = self.item2.tag
        else:
            item2 = self.item2
        return "[ MTX RELATIONSHIP <{}> is <{}>'s {} ]".format(item2, item1, self.relationship_string)

    def link_second_person(self, item2):
        self.item2 = item2
        self.item2_is_person = True

