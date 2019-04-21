from lib.MatrixSocialNode import MatrixSocialNode


class MatrixInstagramPost(MatrixSocialNode):
    def __init__(self, person, datetime, image_url, caption, like_count, comment_count):
        super().__init__(person, datetime, "instagram", "post")
        self.image_url = image_url
        self.caption = caption
        self.like_count = like_count
        self.comment_count = comment_count
        self.comments = []
        self.likes = []
        self.tags = []

    def __str__(self):
        return "[ MTX IG POST | '{}' {} likes ]".format(self.caption, self.like_count)
