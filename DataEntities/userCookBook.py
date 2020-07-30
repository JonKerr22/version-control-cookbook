from .fullRecipe import FullRecipe
from datetime import datetime

class UserCookBook:
    """
    schema:
        cookbookId - int
        userId - int
        cookbookName - string
        allRecipes - list of type FullRecipe
        createdDate - dateTime

    """
    def __init__(self, userId=None, cookbookId=None, cookbookName=None):
        self.cookbookId = cookbookId if not None else 0
        self.userId = userId if not None else 0
        self.cookbookName = cookbookName if not None else ""
        self.allRecipes = []
        self.allRecipes.append(FullRecipe(cookbookId=self.cookbookId, recipeId=1))
        self.createdDate = datetime.now()

    def AddRecipeToCookBook(self, newRecipeObj):
        self.allRecipes.append(newRecipeObj)

    #def updateExistingRecipe(self, recipeId, )

    