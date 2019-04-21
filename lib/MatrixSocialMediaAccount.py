class MatrixSocialMediaAccount:
    def __init__(self, social_network, user_id, name, profile_image, description):
        self.account_type = social_network
        self.id = user_id
        self.name = name
        self.profile_image = profile_image
        self.description = description

