import sys
sys.path.append('../')

from datetime import datetime

class User:
    """
    schema:
        userId - int
        username - string 
        email - string
        password - string (should be salted and hashed for storing and confirming login)
        userRecipes - list with type FullRecipes
        createdDate - dateTime

        will almost definitely need more in the future
    """
    def __init__(self, userIdNum=None, userName=None, userEmail=None):
        self.userId = userIdNum if not None else 0
        self.username = userName if not None else "Test User"
        self.email = userEmail if not None else "test@example.com"
        self.password = ""
        self.userRecipes = []
        self.createdDate = datetime.now()

    def GetAllRecipeIds(self, asStr = False):
        outList = []
        for recipe in self.userRecipes:
            id = str(recipe.recipeId ) if asStr else recipe.recipeId
            outList.append(id)
        return outList