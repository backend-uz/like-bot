import json

class LikeDB:
    def __init__(self, file_path):
        # Initialize the database
        self.file_path = file_path
        # Open the database file if it exists, otherwise create a new one
        try:
            with open(self.file_path, 'r') as f:
                self.db = json.load(f)
        except:
            self.db = {}
            with open(self.file_path, 'w') as f:
                json.dump(self.db, f)

    def save(self):
        """
        Save the database to the file
        """
        pass

    def all_likes(self, user_id):
        """
        Count all users likes
        """
        pass

    def all_dislikes(self, user_id):
        """
        Count all users dislikes
        """
        pass

    def add_like(self, user_id:str):
        """
        Add like to the database
        
        Args:
            user_id (str): telegram user id

        Returns:
            The number of likes and dislikes for the post
        """
        pass

    def add_dislike(self, user_id:str):
        """
        Add dislike to the database
        
        Args:
            user_id (str): telegram user id

        Returns:
            The number of likes and dislikes for the post
        """
        pass
            