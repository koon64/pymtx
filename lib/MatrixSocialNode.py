class MatrixSocialNode:
    def __init__(self, person, datetime, social_network, node_type):
        self.person = person
        self.matrix_instance = person.matrix_instance
        self.datetime = datetime
        self.social_network = social_network
        self.node_type = node_type
        self.matrix_instance.social_nodes.append(self)
