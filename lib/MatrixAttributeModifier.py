class MatrixAttributeModifier:

    # changes text to lowercase
    def lower(self, text):
        if type(text) is str:
            return str(text).lower()
        elif type(text) is list:
            return [i.lower() for i in text]

    # changes text to uppercase
    def upper(self, text):
        if type(text) is str:
            return str(text).upper()
        elif type(text) is list:
            return [i.upper() for i in text]

    # splits into words
    def words(self, text):
        if type(text) is str:
            return str(text).split()

    # turns a list into an int
    def count(self, array):
        return len(array)

