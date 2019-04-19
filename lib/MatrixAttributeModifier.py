class MatrixAttributeModifier:

    # changes text to lowercase
    def lower(self, text):
        if type(text) is str:
            return str(text).lower()

    # changes text to uppercase
    def upper(self, text):
        if type(text) is str:
            return str(text).upper()

    # splits into words
    def words(self, text):
        if type(text) is str:
            return str(text).split()
