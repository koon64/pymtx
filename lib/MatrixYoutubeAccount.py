from lib.MatrixSocialMediaAccount import MatrixSocialMediaAccount


class MatrixYoutubeAccount(MatrixSocialMediaAccount):
    def __init__(self, user_id, name, profile_image, description, subscribers, views, video_count):
        super().__init__("youtube", user_id, name, profile_image, description)
        self.subscribers = subscribers
        self.views = views
        self.video_count = video_count

