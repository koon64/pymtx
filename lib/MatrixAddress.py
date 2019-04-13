class MatrixAddress:
    def __init__(self, address_type, lat, lng, country, cid, state, sid, county, town, zip_code, street_format,
                 street_name, street_suffix, number, full_address):
        self.type = address_type
        self.lat = lat
        self.lng = lng
        self.country = country
        self.cid = cid
        self.state = state
        self.sid = sid
        self.county = county
        self.town = town
        self.zip = zip_code
        self.street_format = street_format
        self.street_name = street_name
        self.street_suffix = street_suffix
        self.number = number
        self.full_address = full_address

    def __str__(self):
        return self.full_address

    def __int__(self):
        return self.number

