from click import ClickException

class BadID(ClickException):
    def __init__(self, user_id: int):
        message = f"Invalid user id {str(user_id)}"
        super().__init__(message)

class PrivateProfile(ClickException):
    def __init__(self):
        message = "The profile is private"
        super().__init__(message)

class BadParameter(ClickException):
    def __init__(self):
        message = f"Bad parameter. Try to change user_id"
        super().__init__(message)