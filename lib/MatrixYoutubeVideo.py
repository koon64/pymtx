from lib.MatrixSocialNode import MatrixSocialNode


class MatrixYoutubeVideo(MatrixSocialNode):
    def __init__(self, matrix_instance, datetime, video_id, title, thumbnail):
        super().__init__(matrix_instance, datetime, "youtube", "video")
        self.video_id = video_id
        self.title = title
        self.thumbnail = thumbnail

    def __str__(self):
        return "[ MTX YT VID | '{}' by {} ]".format(self.title, self.person.name.full)

