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
    def __init__(self, userIdNum=None, userName=None, userEmail=None):
        self.userId = userIdNum if not None else 0
        self.username = userName if not None else "Test User"
        self.email = userEmail if not None else "test@example.com"
        self.password = ""
        self.userCookbooks = [self.GetInitialEmptyCookBook()]
        self.createdDate = datetime.now()

    def GetACookBook(self, cookbookId):
        for book in self.userCookbooks:
            if(book.cookbookId == cookbookId):
                return book
        return None #returns empty if user does not contain a book with that id

    def GetAllUserCookBookIds(self, asStr = False):
        outList = []
        for cookBook in self.userCookbooks:
            id = str(cookBook.cookbookId ) if asStr else cookBook.cookbookId
            outList.append(id)
        return outList

    def AddExistingCookbook(self, cookbookObj):
        if(cookbookObj.cookbookId == 0 or cookbookObj.cookbookId is None):
            cookbookObj.cookbookId = len(self.userCookbooks) + 1
        cookbookObj.userId = self.userId
        self.userCookbooks.append(cookbookObj)

    def UpdateCookBook(self, updatedCookbookObj):
        for book in self.userCookbooks:
            if(book.cookbookId == updatedCookbookObj.cookbookId):
                book = updatedCookbookObj

        return self
    def GetInitialEmptyCookBook(self):
        emptyCookBook = UserCookBook(userId=self.userId, cookbookId=1)
        emptyCookBook.allRecipes = []
        return emptyCookBook
