from unders import Underscore

_ = Underscore()


class MatrixBirthdate:
    def __init__(self, date, day_of_week, timestamp, bd_formatted, bd_formatted_year, zodiac, zodiac_emoji):
        date = date.replace("-", '/')
        self.date = _.time.parse_date(date)
        self.date_string = date
        parts = date.split("/")
        if len(parts) == 3:
            self.month = parts[0]
            self.day = parts[1]
            self.year = parts[2]
        else:
            raise Exception('Invalid date, must be: 12/25/2019')
        self.dow = day_of_week
        self.timestamp = timestamp
        self.formatted = bd_formatted
        self.formatted_year = bd_formatted_year
        self.zodiac = zodiac
        self.zodiac_emoji = zodiac_emoji

    def __str__(self):
        return self.date_string

    def __int__(self):
        return int(self.timestamp)

