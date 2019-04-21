from lib.MatrixSocialMediaAccount import MatrixSocialMediaAccount


class MatrixInstagramAccount(MatrixSocialMediaAccount):
    def __init__(self, user_id, name, profile_image, biography, username, private, followers, following):
        super().__init__("instagram", user_id, name, profile_image, biography)
        self.username = username
        self.private = private
        self.followers = followers
        self.following = following

    def __str__(self):
        return "[ MTX INSTAGRAM <{}> {} ({} followers) ]".format(self.username, self.name, self.followers)

