from unders import Underscore

_ = Underscore()


class MatrixPhone:
    def __init__(self, number, phone_type, label, carrier, location):
        self.number = number
        self.type = phone_type
        self.label = label
        self.carrier = carrier
        self.location = location

    def __str__(self):
        return self.formatted

    def __int__(self):
        return int(self.number)

    # formats a the phone number
    @property
    def formatted(self):
        return _.format.phone(self.number)
