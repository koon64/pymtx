class MatrixSchoolClass:
    def __init__(self, class_name, teacher, room, period):
        self.name = class_name
        self.teacher = teacher
        self.room = room
        self.period = period
        self.is_free = False
        self.students = []
        self.subject = self.get_class_type(class_name)
        self.math_level = self.get_math_level(class_name) if self.subject == "math" else None

    def __str__(self):
        return "[ MTX CLASS {} with {} P.{} ({} students) Rm. {} ]".format(self.name, self.teacher, self.period, len(self.students), self.room)

    @property
    def math_level_string(self):
        return "M{}".format(str(self.math_level + 1)) \
            if self.math_level != 0 else "S1" \
            if self.math_level is not None else ""

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)

    def get_math_level(self, class_name):
        if class_name == "Integrated Math 1":
            return 0
        level_maps = [
            "S1",
            "M2",
            "M3",
            "M4"
        ]
        counter = 0
        for level in level_maps:
            if level in class_name:
                return counter
            counter += 1

    def get_class_type(self, class_name):
        key_words = {
            "science": [
                "biology",
                "science",
                "chemistry",
                "anatomy",
                "physics",
                "forensics",
                "astronomy"
            ],
            "math": [
                "algebra",
                "geometry",
                "precalculus",
                "calculus",
                "math",
                "statistics",
                "multivar"
            ],
            "language_arts": [
                "eng",
                "english"
            ],
            "social_studies": [
                "history",
                "civics",
                "micro econ",
                "holocaust",
                "government",
                "psychology",
                "economics",
                "american",
                "amer studies",
                "anthropology",
                "indiv & fam dev"  # idk
            ],
            "sped": [
                "center",
                "aces",
                "skills",
                "reading"
            ],
            "connections": [
                "connections"
            ],
            "electives": [
                "orchestra",
                "choir",
                "ceramics",
                "child",
                "care",
                "music technology",
                "drawing",
                "business",
                "woodworking",
                "broadcasting",
                "filmmaking",
                "nutrition",
                "robotics",
                "design",
                "photography",
                "music",
                "bakery",
                "jewelry",
                "band",
                "studio art",
                "graphics",
                "yearbook",
                "journalism",
                "electronics",
                "culinary"
            ],
            "language": [
                "spanish",
                "latin",
                "chinese",
                "french"
            ],
            "health": [
                "health"
            ],
            "gym": [
                "pe grades"
            ],
            "study hall": [
                "study hall"
            ]
        }
        for subject in key_words:
            for word in key_words[subject]:
                if word in class_name.lower():
                    return subject
        return None


class MatrixSchoolFree:
    def __init__(self, period):
        self.is_free = True
        self.name = "free"
        self.period = period
        self.students = []
        self.subject = 'free'

    def __str__(self):
        return "[ MTX FREE ]"

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)

