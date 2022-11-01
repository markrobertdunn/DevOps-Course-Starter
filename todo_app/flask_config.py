import os


class Config:
    def __init__(self):
        """Base configuration variables."""
        self.ConnectionString = os.environ.get('ConnectionString')
        if not self.ConnectionString:
            raise ValueError("No ConnectionString set for Flask application. Did you follow the setup instructions?")
