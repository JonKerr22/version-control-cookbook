import sys
sys.path.append('../')

from datetime import datetime
from .userCookBook import UserCookBook

class User:
    """
    schema:
        userId - int
        username - string 
        email - string
        password - string (should be salted and hashed for storing and confirming login)
        userCookbooks - list with type UserCookBook
        createdDate - dateTime

        will almost definitely need more in the future
    """
    def __init__(self):
        self.userId = 0
        self.username = "Test User"
        self.email = "test@example.com"
        self.password = ""
        self.userCookbooks = [self.GetInitialEmptyCookBook()]
        self.createdDate = datetime.now()

    def GetACookBook(self, cookbookId):
        for book in self.userCookbooks:
            if(book.cookbookId == cookbookId):
                return book
        return None #returns empty if user does not contain a book with that id

    def AddExistingCookbook(self, cookbookObj):
        if(cookbookObj.cookbookId == 0 or cookbookObj.cookbookId is None):
            cookbookObj.cookbookId = len(self.userCookbooks) + 1
        cookbookObj.userId = self.userId
        self.userCookbooks.append(cookbookObj)

    def GetInitialEmptyCookBook(self):
        emptyCookBook = UserCookBook()
        emptyCookBook.userId = self.userId
        emptyCookBook.cookbookId = 1
        emptyCookBook.createdDate = datetime.now()
        emptyCookBook.allRecipes = []
        return emptyCookBook
