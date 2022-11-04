import os


class Config:
    def __init__(self):
        """Base configuration variables."""
        self.CONNECTIONSTRING = os.environ.get('CONNECTIONSTRING')
        if not self.CONNECTIONSTRING:
            raise ValueError("No CONNECTIONSTRING set for Flask application. Did you follow the setup instructions?")
