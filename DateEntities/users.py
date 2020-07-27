from datetime import datetime
from userCookBook import UserCookBook

class User:
    """
    schema:
        userId - int
        email - string
        password - string (should be salted and hashed for storing and confirming login)
        userCookbookId - int (to start one cookbook for each user, in future will allow for several)
        createdDate - dateTime

        will almost definitely need more in the future
    """
    def __init__(self):
        self.userId = 0
        self.email = "test@example.com"
        self.password = ""
        self.userCookbookId = 0
        self.createdDate = datetime.now()