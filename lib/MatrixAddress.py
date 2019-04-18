from unders import Underscore
from logging import error

_ = Underscore()


class MatrixAddress:
    def __init__(self, address_type, lat, lng, full_address, debug=False):
        self.type = address_type
        self.lat = float(lat)
        self.lng = float(lng)
        try:
            parsed_address = _.parse.address(full_address)
            self.valid_address = True
            self.country = parsed_address.country
            self.cid = parsed_address.cid
            self.state = parsed_address.state
            self.sid = parsed_address.sid
            self.locality = parsed_address.locality
            self.zip = parsed_address.zip
            self.street_format = parsed_address.street_format
            self.street_name = parsed_address.street
            self.number = parsed_address.number
            self.full_address = str(parsed_address)
        except:
            if debug:
                error('Parsing: "' + full_address + '"')
            self.valid_address = False
            self.country = None
            self.cid = None
            self.state = None
            self.sid = None
            self.locality = None
            self.zip = None
            self.street_format = None
            self.street_name = None
            self.number = "0"
            self.full_address = ""

    def __str__(self):
        return self.full_address

    def __int__(self):
        return int(self.number)

