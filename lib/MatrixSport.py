class MatrixSport:
    sports = {
        "football": {
            "label": "Football",
            "icon": "http://icons.iconarchive.com/icons/google/noto-emoji-activities/1024/52735-american-football-icon.png",
            "positions": {
                'C': 'Center',
                'MLB': 'Middle Line Backer',
                'QB': 'Quarterback',
                'OLB': 'Outside Line Backer',
                'DT': 'Defencive Tackle',
                'T': 'Tackle',
                'G': 'Guard',
                'DG': 'Defencive Guard',
                'P': 'Punter',
                'LS': 'Longs Snapper',
                'FB': 'Full Back',
                'SS': 'Strong Safety',
                'FS': 'Free Safety',
                'PR': 'Punt Return',
                'KR': 'Kick Return',
                'K': 'Kicker',
                'RB': 'Running Back',
                'NG': 'Nose Guard',
                'DE': 'Defencive End',
                'CB': 'Corner Back',
                'OG': 'Offencive Guard',
                'OT': 'Offencive Tackle',
                'HB': 'Half Back',
                'TE': 'Tight End',
                'DB': 'Defencive Back',
                'S': 'Safety',
                'H': 'Holder',
                'WR': 'Wide Receiver',
                'SB': 'Slot Back'
            }
        },
        "cross_country": {
            "label": "Cross Country",
            "icon": "https://skylineschools.info/sites/default/files/Cross%20Country.png"
        },
        "hockey": {
            "label": "Hockey",
            "icon": "http://icons.iconarchive.com/icons/google/noto-emoji-activities/1024/52742-ice-hockey-icon.png"
        },
        "track": {
            "label": "Track & Field",
            "icon": "https://i.pinimg.com/originals/ea/2b/29/ea2b29c1ef196c1db477fd38c33927a1.png"
        },
        "indoor_track": {
            "label": "Indoor Track & Field",
            "icon": "https://i.pinimg.com/originals/ea/2b/29/ea2b29c1ef196c1db477fd38c33927a1.png"
        },
        "wrestling": {
            "label": "Wrestling",
            "icon": "https://bloximages.chicago2.vip.townnews.com/mtstandard.com/content/tncms/assets/v3/editorial/b/45/b45d1992-fe04-5fa6-a2f6-b141f3fd0964/580a871a80f00.image.jpg"
        },
        "basketball": {
            "label": "Basketball",
            "icon": "http://aux.iconspalace.com/uploads/1979824881329203199.png"
        }
    }

    def __init__(self, name):
        name = str(name).lower()
        if name in self.sports:
            self.name = name
            self.label = self.sports[name]['label']
            self.icon = self.sports[name]['icon']
            self.positions = self.sports[name]['positions'] if 'positions' in self.sports[name] else []
        else:
            raise Exception(name + " is not a supported sport")

    def __str__(self):
        return self.label
