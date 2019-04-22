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
        elif type(text) is list:
            all_words = []
            for i in text:
                if i is not None:
                    all_words = all_words + i.split()
            return all_words

    # turns a list into an int
    def count(self, array):
        return len(array)

