class MatrixEmail:
    def __init__(self, email, email_type, label, username, domain):
        self.email = email
        self.type = email_type
        self.label = label
        self.username = username
        self.domain = domain

    def __str__(self):
        return self.email
