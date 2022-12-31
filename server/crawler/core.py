import datetime

class ApplicationError(Exception):
    """Base application error class."""

    def __init__(self, msg):
        self.msg = msg