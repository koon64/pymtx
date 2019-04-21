from lib.MatrixInstagramPost import MatrixInstagramPost, MatrixSocialNode


class MatrixInstagramLike(MatrixSocialNode):
    def __init__(self, person, datetime, image_url):
        super().__init__(person, datetime, "instagram", "like")
        self.image_url = image_url
        self.has_post = False
        self.post = None

    def __str__(self):
        poster_name = self.post.person.name.full if self.post is not None else "unknown"
        return "[ MTX IG LIKE | {} liked {}'s post ]".format(self.person.name.full, poster_name)

    def connect_post(self, post):
        if type(post) is MatrixInstagramPost:
            self.has_post = True
            self.post = post
            self.post.likes.append(self)

