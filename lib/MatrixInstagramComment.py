from lib.MatrixInstagramPost import MatrixInstagramPost, MatrixSocialNode


class MatrixInstagramComment(MatrixSocialNode):
    def __init__(self, person, datetime, comment, image_url):
        super().__init__(person, datetime, "instagram", "comment")
        self.comment = comment
        self.has_post = False
        self.image_url = image_url
        self.post = None

    def __str__(self):
        return "[ MTX IG COMMENT '{}' by {} ]".format(self.comment, self.person.name.full)

    def connect_post(self, post):
        if type(post) is MatrixInstagramPost:
            self.has_post = True
            self.post = post
            self.post.comments.append(self)

